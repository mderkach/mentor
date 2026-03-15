# 🧩 6. UI Frameworks

В этом разделе разбирается разработка интерфейсов на UI-фреймворках: компоненты, реактивность, маршрутизация, формы, состояние и обновление интерфейса.

> 🚧 🚧 🚧
>
> Раздел в развитии. Состав уроков и глубина тем будут еще уточняться.
>
> 🚧 🚧 🚧

Материал разделен на три части внутри каждого уровня:

- `core` — общая часть без привязки к одному фреймворку;
- `react` — отдельный маршрут по React;
- `vue` — отдельный стартовый слой по Vue.

Сначала полезно понять общую модель, а потом смотреть, как она выражается в конкретном фреймворке. Так React, Vue и общие принципы не смешиваются в одну кашу.

---

## Статус раздела

- Домен: `🟡 Частично готов`
- Уроки: `🟡 Частично готовы`
- Задачи: `⚪ В подготовке`
- Материалы: `🟡 Частично готовы`

## С чего начать

- Сначала проходи `core`, чтобы собрать общую модель UI-фреймворков.
- Если идешь в React, переходи в React-маршрут после общей части.
- Vue-слой пока в переходном состоянии, поэтому не считай этот раздел полностью собранным.

---

## Как проходить раздел

- Сначала проходи `core`, чтобы собрать общую модель.
- Потом иди в нужный маршрут: сейчас полноценно заполнен только `React`.
- Vue пока вынесен в отдельный стартовый слой, чтобы не смешиваться с React в тех же уроках.
- Сравнения с Angular / Svelte / Solid остаются в `core`, потому что это часть общей картины, а не отдельный основной маршрут этой итерации.

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

## Общая часть

### 🟢 Стажер

- [6.1 Компонентная модель UI framework-ов](./10-intern/core/6.1-компонентная-модель-ui-framework-ов.md)

### 🟡 Junior

- [6.2 Цикл обновления и реактивность в UI-фреймворках](./20-junior/core/6.2-update-cycle-и-реактивность-ui-framework-ов.md)
- [6.3 Архитектура маршрутизации](./20-junior/core/6.3-routing-architecture.md)
- [6.4 Формы и валидация](./20-junior/core/6.4-формы-и-валидация.md)

### 🔵 Middle

- [6.5 Композиция компонентов и архитектурные паттерны](./30-middle/core/6.5-композиция-компонентов-и-архитектурные-паттерны.md)
- [6.6 Server state и загрузка данных](./30-middle/core/6.6-server-state-и-data-fetching.md)
- [6.7 Модели управления состоянием](./30-middle/core/6.7-модели-управления-состоянием.md)

### 🟣 Senior / Senior+

- [6.8 Цена обновлений и рендера в UI-фреймворках](./40-senior/core/6.8-cost-model-ui-framework-ов.md)

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
| Стажер | Понимать общую компонентную модель и уметь перейти в конкретный React-слой, не смешивая его с другими фреймворками. |
| Junior | Различать общую задачу UI-фреймворка и React-реализацию в hooks, маршрутизации и формах. |
| Middle | Проектировать паттерны композиции, границы состояния и переиспользуемые абстракции на уровне общей модели и отдельно на уровне React-реализации. |
| Senior / Senior+ | Принимать решения по UI-практикам команды и оптимизации интерфейса как системы, не смешивая общую модель и особенности конкретного фреймворка. |

---

[← На главную](../README.md)
