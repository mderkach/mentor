# 🧩 6. UI Frameworks

В этом разделе разбирается разработка интерфейсов на UI-фреймворках: компоненты, реактивность, маршрутизация, формы, состояние и обновление интерфейса.

Материал разведен по трекам внутри каждого грейда:

- `core` — общая модель темы без привязки к одному framework;
- `react` — отдельный React-путь;
- `vue` — отдельные Vue-заглушки, чтобы Vue не торчал внутри React-уроков.

`core` нужен, чтобы собрать общую инженерную модель. Framework-specific практика вынесена отдельно, чтобы React, Vue и общая теория не смешивались в одном уроке.

---

## Статус раздела

- Домен: `🟡 Частично готов`
- Уроки: `🟡 Частично готовы`
- Задачи: `⚪ В подготовке`
- Материалы: `🟡 Частично готовы`

## С чего начать

- Сначала проходи `core`, чтобы собрать общую модель UI framework-ов.
- Если идешь в React, переходи в React-трек после core-уроков.
- Vue-слой пока в переходном состоянии, поэтому не считай этот домен полностью собранным.

---

## Как читать раздел

- Сначала проходить `core`, чтобы собрать общую модель.
- Потом идти в нужный framework-трек: сейчас полноценно заполнен только `React`.
- Vue пока вынесен в отдельный стартовый слой, чтобы не смешиваться с React внутри тех же уроков.
- Сравнения с Angular / Svelte / Solid остаются в `core`, потому что это часть общей картины, а не отдельный основной трек этой итерации.

---

## Структура папок

```text
06-ui-frameworks/
  10-intern/
    core/
    react/
    vue/
  20-junior/
    core/
    react/
    vue/
  30-middle/
    core/
    react/
    vue/
  40-senior/
    core/
    react/
    vue/
```

---

## Базовый слой

### 🟢 Стажер

- [6.1 Компонентная модель UI framework-ов](./10-intern/core/6.1-компонентная-модель-ui-framework-ов.md)

### 🟡 Junior

- [6.2 Update cycle и реактивность UI framework-ов](./20-junior/core/6.2-update-cycle-и-реактивность-ui-framework-ов.md)
- [6.3 Routing architecture](./20-junior/core/6.3-routing-architecture.md)
- [6.4 Формы и валидация](./20-junior/core/6.4-формы-и-валидация.md)

### 🔵 Middle

- [6.5 Композиция компонентов и архитектурные паттерны](./30-middle/core/6.5-композиция-компонентов-и-архитектурные-паттерны.md)
- [6.6 Server state и data fetching](./30-middle/core/6.6-server-state-и-data-fetching.md)
- [6.7 Модели управления состоянием](./30-middle/core/6.7-модели-управления-состоянием.md)

### 🟣 Senior / Senior+

- [6.8 Cost model UI framework-ов](./40-senior/core/6.8-cost-model-ui-framework-ов.md)

---

## Маршрут React

### 🟢 Стажер

- [6.1 React: базовые принципы и компонентная модель](./10-intern/react/6.1-react-базовые-принципы-и-компонентная-модель.md)

### 🟡 Junior

- [6.2 React: hooks и жизненный цикл](./20-junior/react/6.2-react-hooks-и-жизненный-цикл.md)
- [6.3 React Router: routing architecture](./20-junior/react/6.3-react-router-и-routing-architecture.md)
- [6.4 React: формы и валидация](./20-junior/react/6.4-react-формы-и-валидация.md)

### 🔵 Middle

- [6.5 React: композиция и паттерны компонентов](./30-middle/react/6.5-react-композиция-и-паттерны-компонентов.md)
- [6.6 React: server state и data fetching](./30-middle/react/6.6-react-data-fetching-и-server-state.md)
- [6.7 React: state management](./30-middle/react/6.7-react-state-management.md)

### 🟣 Senior / Senior+

- [6.8 React: оптимизация приложений](./40-senior/react/6.8-react-оптимизация-приложений.md)

---

## Маршрут Vue

Пока это не полноценный Vue-трек, а отдельный стартовый слой, чтобы Vue-материал не был смешан с React.

### 🟢 Стажер

- [6.1 Vue: компонентная модель](./10-intern/vue/6.1-vue-компонентная-модель-todo.md)

### 🟡 Junior

- [6.2 Vue: reactivity, computed, watch и composables](./20-junior/vue/6.2-vue-reactivity-и-composition-api-todo.md)
- [6.3 Vue Router: routing architecture](./20-junior/vue/6.3-vue-router-todo.md)
- [6.4 Vue: формы и валидация](./20-junior/vue/6.4-vue-формы-и-валидация-todo.md)

### 🔵 Middle

- [6.5 Vue: slots, composables и provide/inject](./30-middle/vue/6.5-vue-slots-и-composables-todo.md)
- [6.6 Vue / Nuxt: server state и data fetching](./30-middle/vue/6.6-vue-nuxt-server-state-todo.md)
- [6.7 Vue: reactive state, composables и Pinia](./30-middle/vue/6.7-vue-reactive-state-и-pinia-todo.md)

### 🟣 Senior / Senior+

- [6.8 Vue: оптимизация приложений](./40-senior/vue/6.8-vue-оптимизация-todo.md)

---

## Вне раздела

- Storybook, interaction tests и visual regression вынесены в [9.2 Storybook, visual regression и interaction tests](../09-тестирование/40-senior/9.2-storybook-visual-regression-и-interaction-tests.md).

## Ожидания по уровням

| Уровень | Что должен уметь |
|---|---|
| Стажер | Понимать общую компонентную модель и уметь перейти в конкретный React-слой без смешения с другими framework-ами. |
| Junior | Различать общую framework-задачу и React-реализацию в hooks, routing и формах. |
| Middle | Проектировать composition patterns, state/server-state boundaries и reusable abstractions на уровне модели и отдельно на уровне React-реализации. |
| Senior / Senior+ | Принимать решения по UI-практикам команды и оптимизации UI как системы, не смешивая core-модель и framework-specific слой. |

---

[← На главную](../README.md)
