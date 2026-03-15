#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SECTION_DOMAINS = {
    "01-html": "html",
    "02-css": "css",
    "03-javascript": "javascript",
    "04-dom-и-browser": "dom-browser",
    "05-typescript": "typescript",
    "06-ui-frameworks": "ui-frameworks",
    "07-infrastructure": "infrastructure",
    "08-static-analysis": "static-analysis",
    "09-тестирование": "testing",
    "10-архитектура": "architecture",
    "11-безопасность": "security",
    "12-доступность": "accessibility",
    "13-performance": "performance",
    "14-soft-skills": "soft-skills",
}
SECTION_ID_PREFIXES = {
    "06-ui-frameworks": "ui",
    "07-infrastructure": "infra",
}
LEVEL_BY_FOLDER = {
    "00-zero": "zero",
    "10-intern": "intern",
    "20-junior": "junior",
    "30-middle": "middle",
    "40-senior": "senior",
    "50-electives": "middle",
}
LEVEL_LABELS = {
    "zero": "Нулевой блок",
    "intern": "Стажер",
    "junior": "Junior",
    "middle": "Middle",
    "senior": "Senior",
    "senior-plus": "Senior+",
}
VALID_LEVELS = set(LEVEL_LABELS)
FRONTMATTER_ORDER = [
    "id",
    "domain",
    "level",
    "title",
    "prerequisites",
    "skills",
    "outcomes",
    "tags",
    "practice_level",
]
FRONTMATTER_LIST_FIELDS = {"prerequisites", "skills", "outcomes", "tags"}
EDITORIAL_LIST_FIELDS = {"skills", "outcomes", "tags"}
TITLE_RE = re.compile(r"^#\s+(.+)$", re.MULTILINE)
NUMBER_RE = re.compile(r"^(\d+(?:\.\d+)*)")
ITEM_RE = re.compile(r"^(?:[-*]|\d+\.)\s+(.*)$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def list_lesson_paths() -> list[Path]:
    paths: list[Path] = []
    for root in SECTION_DOMAINS:
        base = REPO_ROOT / root
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if is_lesson_path(path):
                paths.append(path)
    return sorted(paths, key=sort_key)


def is_lesson_path(path: Path) -> bool:
    if path.name == "README.md":
        return False

    relative_path = path.relative_to(REPO_ROOT)
    if relative_path.parts[0] not in SECTION_DOMAINS:
        return False

    lower_stem = path.stem.lower()
    if any(marker in lower_stem for marker in ("todo", "draft", "placeholder")):
        return False

    return any(part in LEVEL_BY_FOLDER for part in relative_path.parts[1:-1])


def sort_key(path: Path) -> tuple[str, tuple[int, ...], str]:
    relative_path = path.relative_to(REPO_ROOT)
    return (
        relative_path.parts[0],
        lesson_number_tuple(extract_number_from_path(path)),
        relative_path.as_posix(),
    )


def extract_number_from_path(path: Path) -> str:
    match = NUMBER_RE.match(path.stem)
    if not match:
        raise ValueError(f"Не удалось извлечь номер урока из пути: {path}")
    return match.group(1)


def lesson_number_tuple(number: str) -> tuple[int, ...]:
    return tuple(int(part) for part in number.split("."))


def lesson_number_from_id(lesson_id: str) -> tuple[int, ...]:
    match = re.search(r"(\d+(?:\.\d+)*)$", lesson_id)
    if not match:
        raise ValueError(f"Не удалось извлечь номер урока из id: {lesson_id}")
    return lesson_number_tuple(match.group(1))


def repo_relative(path: Path) -> str:
    if path.is_absolute():
        return path.relative_to(REPO_ROOT).as_posix()
    return path.as_posix()


def load_markdown(path: Path) -> tuple[dict[str, object], str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        return {}, text

    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text

    frontmatter = parse_frontmatter(text[4:end])
    body = text[end + len("\n---\n") :]
    return frontmatter, body


def parse_frontmatter(block: str) -> dict[str, object]:
    data: dict[str, object] = {}
    current_key: str | None = None

    for raw_line in block.splitlines():
        line = raw_line.rstrip()
        if not line:
            continue

        if current_key and line.startswith("  - "):
            items = data.setdefault(current_key, [])
            if not isinstance(items, list):
                raise ValueError(f"Ожидался список у ключа {current_key}")
            items.append(parse_scalar(line[4:].strip()))
            continue

        match = re.match(r"^([a-zA-Z_][a-zA-Z0-9_-]*):(?:\s+(.*))?$", line)
        if not match:
            current_key = None
            continue

        key, value = match.groups()
        if value is None or value == "":
            data[key] = []
            current_key = key
            continue

        data[key] = parse_scalar(value.strip())
        current_key = None

    return data


def parse_scalar(raw: str) -> object:
    if raw in {"[]", "{}"}:
        return json.loads(raw)
    if raw.startswith('"') and raw.endswith('"'):
        return json.loads(raw)
    if raw.startswith("'") and raw.endswith("'"):
        return raw[1:-1]
    return raw


def render_frontmatter(data: dict[str, object]) -> str:
    lines = ["---"]
    for key in FRONTMATTER_ORDER:
        value = data.get(key, [] if key in FRONTMATTER_LIST_FIELDS else "")
        if key in FRONTMATTER_LIST_FIELDS:
            items = value if isinstance(value, list) else []
            if not items:
                lines.append(f"{key}: []")
                continue
            lines.append(f"{key}:")
            for item in items:
                lines.append(f"  - {json.dumps(str(item), ensure_ascii=False)}")
            continue

        lines.append(f"{key}: {json.dumps(str(value), ensure_ascii=False)}")

    lines.append("---")
    return "\n".join(lines)


def find_h1(body: str) -> str:
    match = TITLE_RE.search(body)
    if not match:
        raise ValueError("В уроке отсутствует H1")
    return match.group(1).strip()


def strip_numeric_prefix(value: str) -> str:
    return re.sub(r"^\d+(?:\.\d+)*\s+", "", value).strip()


def normalize_heading(raw_heading: str) -> str:
    heading = raw_heading.strip().lower().replace("ё", "е")
    heading = re.sub(r"^[^\wа-я]+", "", heading, flags=re.IGNORECASE)
    return heading


def find_section(body: str, aliases: tuple[str, ...]) -> str | None:
    lines = body.splitlines()
    collecting = False
    collected: list[str] = []

    for line in lines:
        if line.startswith("## "):
            heading = normalize_heading(line[3:])
            if collecting:
                break
            collecting = any(alias in heading for alias in aliases)
            continue

        if collecting:
            collected.append(line)

    if not collected:
        return None
    return "\n".join(collected).strip()


def first_nonempty_line(section: str | None) -> str | None:
    if not section:
        return None
    for line in section.splitlines():
        stripped = line.strip()
        if stripped:
            return stripped
    return None


def extract_list_items(section: str | None) -> list[str]:
    if not section:
        return []

    items: list[str] = []
    for line in section.splitlines():
        stripped = line.strip()
        match = ITEM_RE.match(stripped)
        if not match:
            continue
        item = clean_list_item(match.group(1))
        if is_placeholder_item(item):
            continue
        items.append(item)
    return items


def clean_list_item(value: str) -> str:
    cleaned = value.strip()
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.rstrip(" ;.")


def is_placeholder_item(value: str) -> bool:
    candidate = value.strip().lower()
    return candidate in {"...", "todo", "todo:", "tbd", "-"}


def resolve_internal_link(source: Path, target: str) -> Path | None:
    if target.startswith(("http://", "https://", "#", "mailto:")):
        return None

    target_path = target.split("#", 1)[0]
    if not target_path.endswith(".md"):
        return None

    resolved = (source.parent / target_path).resolve()
    try:
        resolved.relative_to(REPO_ROOT)
    except ValueError:
        return None
    return resolved


def extract_internal_links(source: Path, text: str) -> list[Path]:
    result: list[Path] = []
    for raw_link in LINK_RE.findall(text):
        resolved = resolve_internal_link(source, raw_link)
        if resolved is not None:
            result.append(resolved)
    return result


def dedupe(values: list[str]) -> list[str]:
    seen: set[str] = set()
    result: list[str] = []
    for value in values:
        if value in seen:
            continue
        seen.add(value)
        result.append(value)
    return result


def normalize_level(raw_level: str | None, path: Path) -> str:
    if raw_level:
        candidate = raw_level.strip().lower().replace("ё", "е")
        if "senior+" in candidate or "senior-plus" in candidate:
            return "senior-plus"
        if "senior" in candidate:
            return "senior"
        if "middle" in candidate:
            return "middle"
        if "junior" in candidate:
            return "junior"
        if "intern" in candidate or "стажер" in candidate:
            return "intern"
        if "нулевой блок" in candidate or "zero" in candidate:
            return "zero"

    relative = path.relative_to(REPO_ROOT)
    for part in reversed(relative.parts[:-1]):
        if part in LEVEL_BY_FOLDER:
            return LEVEL_BY_FOLDER[part]

    raise ValueError(f"Неизвестный уровень по пути: {repo_relative(path)}")


def build_path_index(paths: list[Path]) -> dict[Path, str]:
    index: dict[Path, str] = {}
    for path in paths:
        existing, _ = load_markdown(path)
        existing_id = existing.get("id")
        if isinstance(existing_id, str) and existing_id.strip():
            index[path.resolve()] = existing_id.strip()
            continue
        root = path.relative_to(REPO_ROOT).parts[0]
        prefix = SECTION_ID_PREFIXES.get(root, SECTION_DOMAINS[root])
        index[path.resolve()] = f"{prefix}-{extract_number_from_path(path)}"
    return index


def infer_prerequisites(path: Path, body: str, path_index: dict[Path, str], paths: list[Path]) -> list[str]:
    current_number = lesson_number_tuple(extract_number_from_path(path))
    section = find_section(body, ("что уже должно быть знакомо",))
    candidates: list[str] = []

    for linked in extract_internal_links(path, section or ""):
        linked_id = path_index.get(linked)
        if not linked_id:
            continue
        if lesson_number_from_id(linked_id) < current_number:
            candidates.append(linked_id)

    if candidates:
        return dedupe(candidates)

    previous = previous_lesson_in_folder(path, paths, path_index)
    if previous:
        return [previous]
    return []


def previous_lesson_in_folder(path: Path, paths: list[Path], path_index: dict[Path, str]) -> str | None:
    siblings = sorted(
        [item for item in paths if item.parent == path.parent and item != path],
        key=sort_key,
    )
    current_number = lesson_number_tuple(extract_number_from_path(path))
    previous: str | None = None

    for sibling in siblings:
        sibling_number = lesson_number_tuple(extract_number_from_path(sibling))
        if sibling_number < current_number:
            previous = path_index[sibling.resolve()]

    return previous


def infer_outcomes(body: str) -> list[str]:
    for aliases in (("что ты освоишь",), ("что нужно уметь",)):
        items = extract_list_items(find_section(body, aliases))
        if items:
            return items[:5]
    return []


def slugify(value: str) -> str:
    translit = str.maketrans(
        {
            "а": "a",
            "б": "b",
            "в": "v",
            "г": "g",
            "д": "d",
            "е": "e",
            "ё": "e",
            "ж": "zh",
            "з": "z",
            "и": "i",
            "й": "y",
            "к": "k",
            "л": "l",
            "м": "m",
            "н": "n",
            "о": "o",
            "п": "p",
            "р": "r",
            "с": "s",
            "т": "t",
            "у": "u",
            "ф": "f",
            "х": "h",
            "ц": "ts",
            "ч": "ch",
            "ш": "sh",
            "щ": "sch",
            "ъ": "",
            "ы": "y",
            "ь": "",
            "э": "e",
            "ю": "yu",
            "я": "ya",
        }
    )
    normalized = value.lower().translate(translit)
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    return re.sub(r"-{2,}", "-", normalized).strip("-")


def infer_fallback_skill(title: str, path: Path) -> list[str]:
    skill = slugify(strip_numeric_prefix(title))
    if skill:
        return [skill]
    return [f"lesson-{extract_number_from_path(path)}"]


def build_computed_metadata(path: Path, body: str, path_index: dict[Path, str], paths: list[Path]) -> dict[str, object]:
    domain = SECTION_DOMAINS[path.relative_to(REPO_ROOT).parts[0]]
    title = strip_numeric_prefix(find_h1(body))
    level_text = first_nonempty_line(find_section(body, ("уровень",)))
    level = normalize_level(level_text, path)

    return {
        "id": path_index[path.resolve()],
        "domain": domain,
        "level": level,
        "title": title,
        "prerequisites": infer_prerequisites(path, body, path_index, paths),
        "skills": infer_fallback_skill(title, path),
        "outcomes": infer_outcomes(body),
        "tags": [domain],
        "practice_level": level,
    }


def merge_metadata(existing: dict[str, object], computed: dict[str, object], rewrite_derived: bool = False) -> dict[str, object]:
    if rewrite_derived:
        merged = dict(computed)
        for key in EDITORIAL_LIST_FIELDS:
            value = existing.get(key)
            if isinstance(value, list) and value:
                merged[key] = value

        prerequisites = existing.get("prerequisites")
        if isinstance(prerequisites, list) and prerequisites and not merged["prerequisites"]:
            merged["prerequisites"] = prerequisites
        return merged

    merged: dict[str, object] = {}
    for key in FRONTMATTER_ORDER:
        value = existing.get(key)
        if key in FRONTMATTER_LIST_FIELDS:
            if isinstance(value, list) and value:
                merged[key] = value
                continue
        elif isinstance(value, str) and value.strip():
            merged[key] = value
            continue
        merged[key] = computed[key]
    return merged


def write_with_frontmatter(path: Path, metadata: dict[str, object], body: str) -> None:
    content = f"{render_frontmatter(metadata)}\n\n{body.lstrip(chr(10))}"
    path.write_text(content, encoding="utf-8")


def sync_files(rewrite_derived: bool) -> int:
    paths = list_lesson_paths()
    path_index = build_path_index(paths)
    updated = 0

    for path in paths:
        existing, body = load_markdown(path)
        computed = build_computed_metadata(path, body, path_index, paths)
        merged = merge_metadata(existing, computed, rewrite_derived=rewrite_derived)
        new_content = f"{render_frontmatter(merged)}\n\n{body.lstrip(chr(10))}"
        current_content = path.read_text(encoding="utf-8")
        if current_content == new_content:
            continue
        path.write_text(new_content, encoding="utf-8")
        updated += 1

    print(f"Обновлено файлов: {updated}")
    return 0


def validate_files() -> int:
    paths = list_lesson_paths()
    path_index = build_path_index(paths)
    all_ids: dict[str, Path] = {}
    errors: list[str] = []

    for path in paths:
        frontmatter, body = load_markdown(path)
        rel_path = repo_relative(path)

        if not frontmatter:
            errors.append(f"{rel_path}: отсутствует frontmatter")
            continue

        missing = [field for field in FRONTMATTER_ORDER if field not in frontmatter]
        if missing:
            errors.append(f"{rel_path}: отсутствуют поля {', '.join(missing)}")
            continue

        title = strip_numeric_prefix(find_h1(body))
        if frontmatter.get("title") != title:
            errors.append(f"{rel_path}: title не совпадает с H1")

        level = frontmatter.get("level")
        if not isinstance(level, str) or level not in VALID_LEVELS:
            errors.append(f"{rel_path}: некорректный level={level!r}")

        lesson_id = frontmatter.get("id")
        if not isinstance(lesson_id, str) or not lesson_id:
            errors.append(f"{rel_path}: отсутствует корректный id")
        elif lesson_id in all_ids:
            errors.append(f"{rel_path}: id дублируется с {repo_relative(all_ids[lesson_id])}")
        else:
            all_ids[lesson_id] = path

        domain = frontmatter.get("domain")
        if domain not in SECTION_DOMAINS.values():
            errors.append(f"{rel_path}: некорректный domain={domain!r}")

        practice_level = frontmatter.get("practice_level")
        if practice_level != level:
            errors.append(f"{rel_path}: practice_level должен совпадать с level")

        for list_field in FRONTMATTER_LIST_FIELDS:
            field_value = frontmatter.get(list_field)
            if not isinstance(field_value, list):
                errors.append(f"{rel_path}: {list_field} должен быть списком")
                continue
            if list_field in EDITORIAL_LIST_FIELDS and not field_value:
                errors.append(f"{rel_path}: {list_field} не должен быть пустым")

        prerequisites = frontmatter.get("prerequisites", [])
        if isinstance(prerequisites, list):
            for item in prerequisites:
                if item not in all_ids and item not in path_index.values():
                    errors.append(f"{rel_path}: prerequisite {item!r} не найден среди lesson id")

    if errors:
        print("Ошибки валидации:\n")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"Валидация пройдена: {len(paths)} файлов")
    return 0


def create_lesson(
    path_arg: str,
    title: str,
    extra_prereqs: list[str],
    extra_skills: list[str],
    extra_outcomes: list[str],
    extra_tags: list[str],
    force: bool,
) -> int:
    path = (REPO_ROOT / path_arg).resolve()
    try:
        relative_path = path.relative_to(REPO_ROOT)
    except ValueError:
        print("Путь должен находиться внутри репозитория", file=sys.stderr)
        return 1

    if path.exists() and not force:
        print(f"Файл уже существует: {repo_relative(path)}", file=sys.stderr)
        return 1

    if relative_path.parts[0] not in SECTION_DOMAINS:
        print("Скрипт поддерживает только доменные разделы репозитория", file=sys.stderr)
        return 1

    if not any(part in LEVEL_BY_FOLDER for part in relative_path.parts[1:-1]):
        print("Новый урок должен лежать внутри папки уровня", file=sys.stderr)
        return 1

    path.parent.mkdir(parents=True, exist_ok=True)
    number = extract_number_from_path(path)
    domain = SECTION_DOMAINS[relative_path.parts[0]]
    level = normalize_level(None, path)
    prefix = SECTION_ID_PREFIXES.get(relative_path.parts[0], domain)

    metadata = {
        "id": f"{prefix}-{number}",
        "domain": domain,
        "level": level,
        "title": title,
        "prerequisites": extra_prereqs,
        "skills": extra_skills or infer_fallback_skill(title, path),
        "outcomes": extra_outcomes or ["Сформулируй наблюдаемый результат урока"],
        "tags": dedupe([domain, *extra_tags]),
        "practice_level": level,
    }

    body = build_lesson_template(number, title, level)
    write_with_frontmatter(path, metadata, body)
    print(f"Создан файл: {repo_relative(path)}")
    return 0


def build_lesson_template(number: str, title: str, level: str) -> str:
    level_label = LEVEL_LABELS[level]
    return f"""# {number} {title}

## Уровень

{level_label}

## Кратко о теме

Коротко объясни, что это за тема и какую практическую проблему она закрывает.

## Зачем это нужно на практике

- ...
- ...
- ...

## Что уже должно быть знакомо

- ...

## 🎯 Что ты освоишь

- ...
- ...
- ...

## Что важно понять

- ...
- ...
- ...

## Частые ошибки

- ...
- ...

## 🔧 Практика

1. ...
1. ...
1. ...

## ✅ Чеклист

- [ ] ...
- [ ] ...
- [ ] ...

## Как проверить понимание

1. ...
1. ...
1. ...

## Следующий шаг развития

- ...

## 📚 Полезные материалы

- ...
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Управление frontmatter для уроков")
    subparsers = parser.add_subparsers(dest="command", required=True)

    sync_parser = subparsers.add_parser("sync", help="Добавить или обновить frontmatter во всех уроках")
    sync_parser.add_argument(
        "--rewrite-derived",
        action="store_true",
        help="Пересчитать структурные поля, сохранив уже заполненные skills/outcomes/tags",
    )

    subparsers.add_parser("validate", help="Проверить frontmatter у всех уроков")

    new_parser = subparsers.add_parser("new", help="Создать новый урок с frontmatter и базовым шаблоном")
    new_parser.add_argument("path", help="Путь до нового markdown-файла относительно корня репозитория")
    new_parser.add_argument("--title", required=True, help="Заголовок урока без номера")
    new_parser.add_argument("--prerequisite", action="append", default=[], help="Lesson id для prerequisites")
    new_parser.add_argument("--skill", action="append", default=[], help="Явно задать skill")
    new_parser.add_argument("--outcome", action="append", default=[], help="Явно задать outcome")
    new_parser.add_argument("--tag", action="append", default=[], help="Дополнительный tag")
    new_parser.add_argument("--force", action="store_true", help="Перезаписать существующий файл")
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    if args.command == "sync":
        return sync_files(rewrite_derived=args.rewrite_derived)

    if args.command == "validate":
        return validate_files()

    if args.command == "new":
        return create_lesson(
            path_arg=args.path,
            title=args.title,
            extra_prereqs=args.prerequisite,
            extra_skills=args.skill,
            extra_outcomes=args.outcome,
            extra_tags=args.tag,
            force=args.force,
        )

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
