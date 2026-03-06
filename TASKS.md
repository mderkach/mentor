# Практические задачи 2026

Задачи взяты из листа `Задачи 2026`.

## Верстка и UI

### 1. Верстка экрана по макету

Анализирует макет, выделяет семантическую структуру, выбирает layout-модель, верстает экран с адаптивом, проверяет доступность и кросс-браузерность.

### 2. Сборка формы с валидацией

Проектирует структуру формы, связывает label и поля, добавляет клиентскую валидацию, сообщения об ошибках, keyboard navigation и UX сценарии.

## CSS

### 3. Реализация адаптивной сетки

Выбирает между flex/grid, строит layout с breakpoint или container queries, учитывает переполнение и reflow.

### 4. Поддержка темизации

Вводит design tokens, CSS custom properties, dark mode/light-dark(), проверяет наследование и fallback.

## JavaScript

### 5. Реализация интерактивной логики

Описывает состояние, события и побочные эффекты, пишет устойчивую логику без гонок и утечек.

### 6. Работа с асинхронностью

Запускает запросы параллельно, управляет отменой через AbortController, обрабатывает ошибки и loading states.

## DOM и Browser

### 7. Интеграция с Browser API

Выбирает подходящий Web API, учитывает permission model, обрабатывает fallback и ошибки среды.

## TypeScript

### 8. Моделирование контрактов данных

Описывает DTO и доменные модели, вводит discriminated unions и runtime validation.

### 9. Ужесточение типизации legacy-модуля

Включает strict-правила постепенно, устраняет any, добавляет type guards и снижает риск регрессий.

## React / UI Framework

### 10. Создание компонентной фичи

Декомпозирует фичу на компоненты и hooks, разделяет presentation/state, добавляет тесты.

### 11. Оптимизация рендеринга

Измеряет причину лишних рендеров, оптимизирует state colocation, memoization и virtualization.

## State Management

### 12. Проектирование client state

Определяет границы стора, минимизирует дублирование, вводит selectors и избегает derived-state bugs.

### 13. Работа с server state

Использует query keys, cache invalidation, optimistic updates и обработку ошибок/ретраев.

## Routing

### 14. Проектирование маршрутизации

Разбивает приложение на маршруты, layout routes, guards, lazy routes и deep links.

## HTTP

### 15. Интеграция с внешним API

Проектирует слой запросов, обработку ошибок, авторизацию, типизацию и retry/cancel policy.

## Тестирование

### 16. Покрытие модуля тестами

Выбирает уровень теста, пишет unit/integration/e2e, стабилизирует flaky-поведение и CI прогон.

### 17. UI regression контроль

Поднимает story, interaction test или visual regression и встраивает проверку в pipeline.

## Архитектура

### 18. Рефакторинг модуля по FSD

Выделяет public API, чистит зависимости между слоями, переносит shared-код и упрощает импортную карту.

### 19. Внедрение Clean Architecture

Выделяет use cases, границы между доменом и UI, отделяет DTO и инфраструктуру.

### 20. Интеграция микрофронтенда

Настраивает host/remote, контролирует shared deps, контракт событий и изоляцию CSS/роутинга.

## Infrastructure

### 21. Настройка сборки

Конфигурирует Vite/Webpack, env, code splitting, source maps и bundle analyzer.

### 22. Настройка монорепозитория

Строит workspace, affected pipeline, кэширование и правила владения пакетами.

### 23. CI/CD пайплайн

Собирает pipeline для lint/test/build/deploy, настраивает кеши, артефакты и rollback strategy.

## Static Analysis

### 24. Настройка стандартов кода

Вводит ESLint/Stylelint/Prettier/Oxlint/Biome, husky и commit checks без лишнего шума.

## Browser / Debugging

### 25. Диагностика утечки памяти

Снимает heap snapshot, ищет retainers, локализует listener leak или неочищенный cache.

## Performance

### 26. Оптимизация Core Web Vitals

Анализирует LCP/CLS/INP, устраняет bottleneck в сети, рендере или hydration.

## Безопасность

### 27. Защита клиентского приложения

Проверяет XSS/CSP/token storage/postMessage/cors assumptions и устраняет риски.

## Доступность

### 28. Accessibility review фичи

Проверяет семантику, фокус, формы, контраст, screen reader flow и ARIA только где нужно.

## Soft Skills

### 29. Архитектурное решение

Фиксирует ADR, синхронизируется со смежниками, объясняет trade-offs и план миграции.

### 30. Код-ревью и менторинг

Даёт конкретную обратную связь, формирует критерии качества и ведёт младшего разработчика до результата.
