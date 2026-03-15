# 🛠 7. Infrastructure

Этот раздел про инфраструктуру frontend-проекта: как код устанавливается, собирается, проверяется, выпускается и поддерживается без ручного хаоса.

> 🚧 🚧 🚧
>
> Раздел в развитии. Состав уроков и глубина тем будут еще уточняться.
>
> 🚧 🚧 🚧

Внутри каждого грейда есть:

- `core` — общая часть, чтобы понять инженерную задачу целиком;
- отдельные папки по инструментам или типам инструментов: `package-manager`, `git`, `vite`, `ci`, `workspaces-monorepo`, `delivery` и т.д.

Сначала полезно понять общую инженерную проблему в `core`, а потом разбирать конкретный инструмент. Иначе знание одной команды в CLI быстро маскируется под понимание инфраструктуры целиком.

---

## Статус раздела

- Домен: `✅ Готов`
- Уроки: `✅ Готовы`
- Задачи: `⚪ В подготовке`
- Материалы: `🟡 Частично готовы`

## С чего начать

- Если слабо понимаешь `package.json`, scripts и базовый Git-цикл, начни с нулевого блока и стажерского слоя.
- Сначала проходи `core`, потом углубляйся в конкретные инструменты.
- Не путай знание одного CLI с пониманием инфраструктурной модели целиком.

---

## Структура папок

```text
07-infrastructure/
  00-zero/
    core/
    node-package-manager/
  10-intern/
    core/
    package-manager/
    git/
  20-junior/
    core/
    package-manager/
    vite/
    ci/
  30-middle/
    core/
    build-tools/
    ci-release/
    workspaces-monorepo/
  40-senior/
    core/
    monorepo-orchestration/
    delivery/
    team-rules/
```

---

## Общая часть

### ⚪ Нулевой блок

- [0.0.1 Рабочее окружение frontend-проекта](./00-zero/core/0.0.1-рабочее-окружение-frontend-проекта.md)

### 🟢 Стажер

- [7.1 `package.json`, scripts и lockfile как контракт проекта](./10-intern/core/7.1-package-json-scripts-и-lockfile-как-контракт-проекта.md)
- [7.2 История изменений и инженерная дисциплина](./10-intern/core/7.2-история-изменений-и-инженерная-дисциплина.md)

### 🟡 Junior

- [7.3 Управление зависимостями и обновления без хаоса](./20-junior/core/7.3-управление-зависимостями-и-обновления-без-хаоса.md)
- [7.4 Сборка проекта и переменные окружения](./20-junior/core/7.4-build-systems-и-env.md)
- [7.5 CI как цепочка проверок и артефактов](./20-junior/core/7.5-ci-как-pipeline-и-обязательные-проверки.md)

### 🔵 Middle

- [7.6 Code splitting, source maps и разбор проблем сборки](./30-middle/core/7.6-code-splitting-source-maps-и-диагностика-сборки.md)
- [7.7 Workspaces, устройство monorepo и граф зависимостей](./30-middle/core/7.7-workspaces-границы-monorepo-и-dependency-graph.md)
- [7.8 Preview-окружения, кеш и выпуск версий](./30-middle/core/7.8-preview-environments-cache-и-release-flow.md)

### 🟣 Senior / Senior+

- [7.9 Координация сборки и проверок на масштабе команды](./40-senior/core/7.9-orchestration-на-масштабе-команды.md)
- [7.10 Стратегия поставки и безопасность выкладки](./40-senior/core/7.10-стратегия-поставки-и-безопасность-выкладки.md)
- [7.11 Правила качества инфраструктуры команды](./40-senior/core/7.11-правила-качества-инфраструктуры-команды.md)

---

## Маршруты по инструментам

### `Node.js / package manager`

- [0.0.1 Node.js и package manager](./00-zero/node-package-manager/0.0.1-nodejs-и-package-manager.md)
- [7.1 npm / pnpm / yarn: `package.json`, scripts и lockfile](./10-intern/package-manager/7.1-package-json-scripts-и-lockfile.md)
- [7.3 npm / pnpm / yarn: semver и обновления без хаоса](./20-junior/package-manager/7.3-semver-и-обновления-без-хаоса.md)

### `Git`

- [7.2 Git: базовый цикл изменений](./10-intern/git/7.2-git-базовый-цикл-изменений.md)

### `Vite / build tools`

- [7.4 Vite: env и базовая сборка frontend-приложения](./20-junior/vite/7.4-vite-env-и-базовая-сборка-frontend-приложения.md)
- [7.6 Build tools: code splitting, source maps и разбор проблем сборки](./30-middle/build-tools/7.6-code-splitting-source-maps-и-разбор-проблем-сборки.md)

### `CI / release`

- [7.5 CI: lint, test, build и артефакты](./20-junior/ci/7.5-ci-lint-test-build-и-артефакты.md)
- [7.8 CI / hosting: cache, preview environments и release flow](./30-middle/ci-release/7.8-ci-cache-preview-environments-и-release-flow.md)

### `Workspaces / monorepo`

- [7.7 Workspaces: пакетные границы и dependency graph](./30-middle/workspaces-monorepo/7.7-workspaces-и-dependency-graph.md)
- [7.9 Nx / Turborepo: orchestration и affected graph](./40-senior/monorepo-orchestration/7.9-nx-turborepo-и-affected-graph.md)

### `Delivery`

- [7.10 Delivery: rollback, feature flags, canary и контейнеры](./40-senior/delivery/7.10-rollback-feature-flags-canary-и-контейнеры.md)

### `Team rules`

- [7.11 Стандарты команды: правила, проверки и зоны ответственности](./40-senior/team-rules/7.11-стандарты-команды-и-обязательные-проверки.md)

---

## Как проходить раздел

- Сначала проходи `core`, чтобы понять саму инженерную проблему.
- Потом иди в нужный инструментальный маршрут.
- Не путай `core` и конкретный инструмент: если идешь в Vite, это не означает, что ты понял сборку проекта целиком.
- Не смешивай инструменты в одном уроке, если задача маршрута — пройти конкретный путь по одному инструменту.

## Ожидания по уровням

| Уровень | Что должен уметь |
|---|---|
| Нулевой блок | Поднять воспроизводимое окружение и понимать, где заканчивается локальная магия и начинается рабочий контракт проекта. |
| Стажер | Читать `package.json`, держать базовый Git-цикл и видеть разницу между общей инженерной задачей и конкретной командой или CLI. |
| Junior | Объяснять цепочку сборки, управление зависимостями и обязательные проверки без привязки к одному инструменту, а потом отдельно пройти Vite/CI-слой. |
| Middle | Разбираться в диагностике сборки, workspaces, кеше и выпуске версий как в инженерных системах и отдельно как в конкретных наборах инструментов. |
| Senior / Senior+ | Проектировать координацию сборки, выпуск и правила команды так, чтобы общая модель и инструментальная реализация не смешивались. |

---

[← На главную](../README.md)
