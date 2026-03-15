# ✅ 8. Static Analysis

В этом разделе разбираются линтеры, форматтеры и другие автоматические проверки, которые помогают находить проблемы до ревью и CI.

Фокус раздела:

- formatter и linter как быстрый feedback loop, а не как вкусовая война;
- rule engines и ownership правил;
- локальный quality loop до CI;
- typed linting, suppressions, false positives и цена rule noise;
- custom rules, AST traversal и codemods;
- governance автоматических проверок на уровне команды.

Важно: этот домен сознательно ограничен ядром статического анализа. Source maps, observability, env/secrets и security-заголовки вынесены в соседние разделы, чтобы не смешивать разные классы инженерных проблем.

---

## Статус раздела

- Домен: `✅ Готов`
- Уроки: `✅ Готовы`
- Задачи: `⚪ В подготовке`
- Материалы: `🟡 Частично готовы`

## С чего начать

- Если неуверенно чувствуешь себя в Git, scripts и CI, сначала вернись в [7. Infrastructure](../07-infrastructure/README.md).
- Иди по уровням: от базового feedback loop к suppressions, custom rules и governance.
- Держи в голове границу: static analysis не заменяет typecheck, tests и runtime-диагностику.

---

## Как учиться в этом разделе

- Идти по уровням: **Стажер -> Junior -> Middle -> Senior / Senior+**.
- Не учить инструменты как список названий. Каждый урок должен отвечать на вопрос: какой риск снижает этот слой проверки.
- Сначала собрать модель feedback loop и ownership инструментов, потом лезть в suppressions, custom rules и governance.
- Держать в голове ограничение: static analysis не заменяет typecheck, tests, build diagnostics и security review.

---

## Ownership Map

| Тема | Что изучаем в `08-static-analysis` | Где лежит глубокая часть |
|---|---|---|
| ESLint, typescript-eslint, Stylelint, Prettier, Biome, Oxlint, hooks, commitlint | Fast feedback, ownership правил, локальный quality loop и governance | Внутри `08-static-analysis` |
| Source maps и bundle diagnostics | Где заканчивается static analysis и начинается build/runtime diagnostics | [7.6 Code splitting, source maps и диагностика сборки](../07-infrastructure/30-middle/core/7.6-code-splitting-source-maps-и-диагностика-сборки.md) |
| Env separation, secrets, rollout safety | Где quality tooling упирается в delivery и security boundary | [7.4 Build systems и env](../07-infrastructure/20-junior/core/7.4-build-systems-и-env.md), [7.10 Стратегия поставки и безопасность выкладки](../07-infrastructure/40-senior/core/7.10-стратегия-поставки-и-безопасность-выкладки.md), [11.1 Безопасность фронтенда](../11-безопасность/11.1-безопасность-фронтенда.md) |
| CSP, SRI и security headers | Эти темы важны как quality gates, но домен у них security, а не static analysis | [11.1 Безопасность фронтенда](../11-безопасность/11.1-безопасность-фронтенда.md) |
| Observability pipeline, Sentry source maps, OpenTelemetry | Автоматические сигналы качества после выкладки, а не только статическая проверка до неё | [13.1 Производительность фронтенда](../13-performance/13.1-производительность-фронтенда.md) |

---

## Core Track

### 🟢 Стажер

- [8.1 Линтинг и форматирование как быстрый feedback loop](./10-intern/8.1-линтинг-и-форматирование-как-быстрый-feedback-loop.md)

### 🟡 Junior

- [8.2 ESLint, typescript-eslint, Stylelint и flat config](./20-junior/8.2-eslint-typescript-eslint-stylelint-и-flat-config.md)
- [8.3 Prettier, Biome, Oxlint и стратегия автоматических правил](./20-junior/8.3-prettier-biome-oxlint-и-стратегия-автоматических-правил.md)
- [8.4 Локальный quality loop: lint-staged, Husky, commitlint и pre-PR проверки](./20-junior/8.4-локальный-quality-loop-lint-staged-husky-commitlint-и-pre-pr-проверки.md)

### 🔵 Middle

- [8.5 Typed linting, suppressions и диагностика шумных правил](./30-middle/8.5-typed-linting-suppressions-и-диагностика-шумных-правил.md)

### 🟣 Senior / Senior+

- [8.6 Custom ESLint rules, AST traversal и codemods](./40-senior/8.6-custom-eslint-rules-ast-traversal-и-codemods.md)
- [8.7 Quality bar статического анализа и governance команды](./40-senior/8.7-quality-bar-статического-анализа-и-governance-команды.md)

## ✅ Ожидания по уровням

| Уровень | Что должен уметь |
|---|---|
| Стажер | Понимать, зачем нужны formatter и linter, где они живут в проекте и почему они не заменяют tests и typecheck. |
| Junior | Уверенно настраивать и использовать ESLint/Stylelint/formatter-стратегию, собирать local quality loop и не путать ownership инструментов. |
| Middle | Эксплуатировать систему проверок на масштабе проекта: suppressions, false positives, typed linting, performance и доверие команды к tooling. |
| Senior / Senior+ | Формировать quality bar команды, внедрять custom rules и codemods там, где это действительно снижает стоимость изменений и удерживает архитектурные границы. |

---

[← На главную](../README.md)
