# ⚡ 3. JavaScript

Это не раздел "про синтаксис". Это трек про то, как JavaScript реально ведёт себя в коде:

- как работают данные, циклы и методы массивов;
- почему похожие конструкции делают не одно и то же;
- как устроены async-flow, Event Loop и очереди задач;
- где начинаются утечки, runtime-pressure и архитектурные границы;
- какие встроенные и advanced API реально полезны инженеру.

> 🚧 🚧 🚧
>
> Раздел в активной переработке: маршрут уже собран, но формулировки и глубина отдельных тем еще будут усиливаться.
>
> 🚧 🚧 🚧

---

## Статус раздела

- Домен: `✅ Готов`
- Уроки: `✅ Готовы`
- Задачи: `⚪ В подготовке`
- Материалы: `🟡 Частично готовы`

## С чего начать

- Если неуверенно чувствуешь себя в HTML и CSS, не пытайся учить JavaScript как изолированный язык.
- Иди последовательно: `Нулевой блок -> Стажер -> Джун -> Мидл -> Сеньор`.
- На middle и senior-уровне смотри не только на синтаксис, а на runtime-модель, scheduling и границы языка.

---

## Как учиться в этом разделе

- Иди по уровням: **Нулевой блок -> Стажер -> Джун -> Мидл -> Сеньор**.
- На intern/junior-слое цель простая: собрать нормальную модель языка без магии.
- На middle-слое важно начать различать похожие механизмы: `for...in` vs `for...of`, `Object` vs `Map`, `Promise` vs timers, `JSON` vs `structuredClone`.
- На senior-слое JavaScript уже читается как runtime-домен: scheduling, metaprogramming, GC-sensitive APIs, quality bar.
- Держи в голове ещё один фильтр: что здесь обычно понимают неправильно, где это ломается в проде и чем этот механизм отличается от соседних.
- Если плавает картина браузерного рантайма, полезно идти параллельно с [4.0 Браузер: от URL до пикселя](../04-dom-и-browser/30-middle/4.0-браузер-от-url-до-пикселя-network-fetch-render.md).

---

## ⚪ Нулевой блок

- [0.0.1 JavaScript в DevTools: console, breakpoints, scope и async stacks](./00-zero/0.0.1-JavaScript-в-DevTools-console-breakpoints-scope-async-stacks.md)

---

## 🟢 Стажер

- [3.1 Переменные, hoisting и temporal dead zone](./10-intern/3.1-переменные-hoisting-и-temporal-dead-zone.md)
- [3.2 Типы, coercion и equality](./10-intern/3.2-типы-coercion-и-equality.md)
- [3.3 Условия, циклы и control flow](./10-intern/3.3-условия-циклы-и-control-flow.md)
- [3.4 Функции, параметры и destructuring](./10-intern/3.4-функции-параметры-и-destructuring.md)
- [3.5 Объекты и массивы: базовый уровень](./10-intern/3.5-объекты-и-массивы-базовый-уровень.md)

---

## 🟡 Джун

- [3.6 Методы массивов и преобразование данных](./20-junior/3.6-методы-массивов-и-преобразование-данных.md)
- [3.7 Closures, scope chain и this](./20-junior/3.7-closures-scope-chain-и-this.md)
- [3.8 Объектная модель: prototype, class и descriptors](./20-junior/3.8-объектная-модель-prototype-class-и-descriptors.md)
- [3.9 Ошибки, throw и fail-fast patterns](./20-junior/3.9-ошибки-throw-и-fail-fast-patterns.md)
- [3.10 ESM-модули, import/export и code splitting](./20-junior/3.10-esm-модули-import-export-и-code-splitting.md)
- [3.11 Promise, async/await и управление асинхронностью](./20-junior/3.11-promise-async-await-и-управление-асинхронностью.md)

---

## 🔵 Мидл

- [3.12 Event Loop, microtasks, timers и requestAnimationFrame](./30-middle/3.12-event-loop-microtasks-timers-и-requestanimationframe.md)
- [3.13 Iterators, generators и async iteration](./30-middle/3.13-iterators-generators-и-async-iteration.md)
- [3.14 Встроенные структуры и границы данных: Map, Set, JSON, Symbol и structuredClone](./30-middle/3.14-встроенные-структуры-и-границы-данных-map-set-json-symbol-и-structuredclone.md)
- [3.15 Память, ссылки, утечки и профилирование](./30-middle/3.15-память-ссылки-утечки-и-профилирование.md)
- [3.16 Composition, immutability и functional-подход в JS](./30-middle/3.16-composition-immutability-и-functional-подход-в-js.md)

---

## 🟣 Сеньор / Senior+

- [3.17 Алгоритмы и структуры данных для прикладного JavaScript](./40-senior/3.17-алгоритмы-и-структуры-данных-для-прикладного-javascript.md)
- [3.18 Runtime-паттерны: memoization, debounce, throttle, pub/sub и FSM](./40-senior/3.18-runtime-паттерны-memoization-debounce-throttle-pub-sub-и-fsm.md)
- [3.19 JavaScript Quality Bar, code conventions и архитектурные границы](./40-senior/3.19-javascript-quality-bar-code-conventions-и-архитектурные-границы.md)
- [3.20 Proxy, Reflect и границы metaprogramming](./40-senior/3.20-proxy-reflect-и-границы-metaprogramming.md)
- [3.21 Advanced scheduling: priorities, yielding и rendering budgets](./40-senior/3.21-advanced-scheduling-priorities-yielding-и-rendering-budgets.md)
- [3.22 WeakRef, FinalizationRegistry и GC-sensitive patterns](./40-senior/3.22-weakref-finalizationregistry-и-gc-sensitive-patterns.md)

## ✅ Ожидания по уровням

| Уровень | Что должен уметь |
|---|---|
| Нулевой блок | Отлаживать код через console, breakpoints, scope inspection и async stack до правок в файле. |
| Стажер | Понимать модель выполнения языка: переменные, типы, ветвления, циклы, функции, объекты и массивы. |
| Джун | Уверенно работать с модулями, ошибками, массивами, контекстом вызова и асинхронностью в production-коде. |
| Мидл | Понимать Event Loop, итераторы, встроенные структуры, память, профилирование и различия между похожими runtime-механизмами. |
| Сеньор / Senior+ | Проектировать runtime-паттерны, выбирать структуры данных, работать с metaprogramming/scheduling/GC-sensitive API и формировать JavaScript-стандарты команды. |

---

[← На главную](../README.md)
