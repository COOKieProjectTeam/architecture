---
date: 2026-05-03
topic: "COOKie — технологический стек (канон текста)"
section: projects
ai_assisted: true
---

# Технологический стек

_Этот файл — **текстовый канон** по технологическому стеку и инженерным решениям MVP. Основание: **[[../../requirements/NFR|NFR]]**, **[[../../requirements/SRS|SRS]]**, **[[../../requirements/FRS|FRS]]** и согласованность с кодовой базой. **Презентация** ([[../../summary/README|summary/README]]) и доска в Excalidraw — **производные / суммирующие** визуальные артефакты: их обновляют **после** правок в vault и здесь, а не наоборот._

Правило при расхождении: версии зависимостей и паттерны — **эта заметка + соответствие репозиториям**; продуктовые обязательства — SRS/NFR. Любое изменение требует обновления этой страницы (и при необходимости CR к спеки) и затем короткой подгонки блока стека на презентации.

## Краткий контур

**COOKie — веб-сервис:** Next.js (фронт) + ASP.NET Core 8 (бэкенд, модульный монолит) + PostgreSQL 15 (+ Redis 7 + S3-совместимое хранилище). Протокол: **REST + JSON**, JWT (Bearer); контракт: **swagger.json** (ASP.NET Core). В dev фронта — **MSW** против `/api/v1/*` по общему swagger.

## 1. Таблица слоёв, выбор и обоснование

Внутри таблицы — обычные markdown-ссылки, без wikilink-алиасов с `|` (ломает рендер столбцов).

| Слой | Итоговый выбор | Рассмотренные альтернативы | Почему итог |
|------|----------------|-------------------------|-------------|
| Frontend FW | **Next.js 14** (App Router) | Plain React SPA | Основа — **React**: SSR / ISR / RSC, file-based routing, экосистема Next |
| Язык фронта | **TypeScript 5** + React 18 | Plain JS; Vue; Svelte | Типобезопасность, связка с Next |
| State / data | **TanStack Query 5** + **Zustand 4** | Redux Toolkit; SWR; только Context | Кэш и invalidation REST; Zustand без лишнего boilerplate |
| UI / стили | **styled-components 6** (CSS-in-JS, ThemeProvider) | Tailwind; CSS Modules; Emotion | Стили рядом с компонентом |
| Формы / валидация на клиенте | **React Hook Form 7** + **Zod 3** | Formik + Yup | Uncontrolled-сценарии; типы из Zod |
| HTTP-клиент | **Axios 1** + interceptors | fetch; ky | Единые interceptors (JWT refresh, ошибки) |
| Backend FW | **ASP.NET Core 8** (modular monolith) | *(требование курсовой без замены заявленной пары FW)* | Производительность .NET 8; модульный монолит |
| ORM | **Entity Framework Core 8** | Dapper; raw SQL | LINQ + миграции; bulk в EF Core 8 |
| Auth (бэк) | **ASP.NET Identity** + **JWT** + **OAuth2** (Yandex ID, T-ID) | IdentityServer; Auth0 | Провайдеры согласованы с [SRS](../../requirements/SRS.md) (FR-US-* / OAuth) |
| Validation (бэк) | **FluentValidation** | DataAnnotations | Правила отдельно от моделей, тестируемо |
| БД | **PostgreSQL 15** | MySQL; MongoDB | JSONB под nutrition; GIN полнотекста RU; ACID |
| Кэш | **Redis 7** | MemoryCache; Memcached | TTL, паттерны кэша и rate-limit |
| Хранилище медиа | **Yandex Object Storage** (S3-совм. API, регион **ru-central1**, bucket образца **cookie-recipes-images**) | Локальный диск; Cloudinary | S3 API в одном облаке с инфрой; пресейны TTL 1ч |
| Протокол обмена | **REST + JSON**, JWT в `Authorization` | GraphQL; gRPC | swagger.json как контракт, проще поддерживать MVP |
| Мокирование API (dev) | **MSW** + общий **swagger.json** | json-server; nock | Service Worker, тот же URL что prod; контракт = swagger |

## 2. Клиент (Next.js App Router)

Принята **FSD-подобная** раскладка каталогов:

- **`app/`** — маршруты, layouts (**RSC** + клиентские границы).
- **`features/`** — auth, recipe-search, recipe-detail, favorites, rating, profile-stats.
- **`entities/`** — recipe, user, nutrition.
- **`shared/api/`** — axios, interceptors, query-keys.
- **`shared/ui/`** — базовые UI на styled-components + ThemeProvider.
- **`shared/lib/`** — Zod-схемы, formatters, hooks.

Рендеринг: SSR / ISR / RSC; **next/image** для изображений с Object Storage (**WebP/AVIF**, on-demand resize, lazy); **next/font** (self-hosted). Иконки: **Lucide React** (tree-shaking). Примеры маршрутов: `/`, `/login`, `/register`, `/recipes`, `/recipes/[slug]`, сегменты с JWT (**/profile**, **/favorites**, **/settings**), админ **/admin/**\*. Детализацию экранов и навигации вести в [FRS](../../requirements/FRS.md); на презентации в summary — только сжатый набросок в соответствии с каноном.

**MSW:** перехват `/api/v1/*` в dev; контракт = swagger ASP.NET Core; в production выключено (`NODE_ENV`).

Аналитика в браузере: пакет **web-vitals** → `POST /api/v1/metrics` (sendBeacon).

## 3. Сервер приложений (ASP.NET Core 8)

**Слои (modular monolith):**

- **Interface:** AuthController, RecipesController, FavoritesController, RatingsController, UsersController, AdminController, UploadsController, MetricsController, ErrorsController и др.
- **Application:** RecipeSearchService, NutritionCalculator, FavoritesService, StatsService, AuthService, ImageService …
- **Domain:** Recipe, User, Favorite, Rating, Session, ErrorLog, MetricEvent; value objects Nutrition, DietaryTags, Allergens.
- **Infrastructure:** репозитории на **EF Core**, `IFileStorage` → **S3 (AWS SDK for .NET, PutObject / presigned GET)**, `ICacheStore` → **Redis** (**StackExchange.Redis**).

**Middleware / cross-cutting:** JwtAuth, **FluentValidation**, ExceptionHandling, **RequestLogging** (**Serilog**), Metrics, CORS.

Ответы API: JSON; схема **refresh-токена** и cookies — уточнять в API-контракте и коде (согласовать с [SRS](../../requirements/SRS.md) FR-US-*). Health: `GET /health/live`, `GET /health/ready` (ping PostgreSQL + Redis); вне процесса — периодическая проверка и оповещение (напр. SMTP при деградации).

Обработка ошибок: центральный middleware → JSON-лог **Serilog** + запись в **Postgres `error_logs`**; корреляция **W3C traceparent** / `X-Trace-Id`; retention **30 дней**.

## 4. Хранилища данных

**PostgreSQL 15**

- Основные сущности: users, recipes, ingredients, user_favorites, user_ratings, sessions, **error_logs**, **metrics_events** (partition по дате, retention порядка 30 дней для метрик).
- **JSONB** для nutrition / агрегатов по рецепту; **GIN** полнотекст (**RU**) для поиска.

**Redis 7**

- Кэши: например популярные рецепты (TTL порядка 30 мин), `search:{hash}` (TTL порядка 5 мин), **refresh_blacklist**, счётчики rate-limit.

**Object Storage**

- Префиксы вроде `cookie-recipes-images/` (thumb / medium / large, WebP/JPEG по сценарию), `cookie-avatars/`.
- Доступ: IAM service account TLS; загрузки от админ-потока.

**Клиентское хранилище (браузер):** краткоживущий access (память), **HttpOnly** cookie для refresh, localStorage для theme/UI и т.п. — согласовать с реализацией и [NFR §5.4 / SEC](../../requirements/NFR.md).

## 5. Потоки данных и статика (ключевые сценарии)

Примеры цепочек:

- Список рецептов: Browser → Next (SSR) → API → Redis → Postgres → снова Redis (TTL) → JSON → кэш TanStack Query → UI.
- Карточка: ISR → API → Postgres; картинки через **next/image** с URL Object Storage.
- Избранное: `POST …/favorite` с JWT → JwtAuth → FavoritesService → Postgres → `204` → invalidate query keys.
- КБЖУ: админские POST/PATCH → NutritionCalculator → сохранение готового JSONB в recipes.
- Статика `/_next/static`: nginx / **Yandex ALB**, длинный `Cache-Control` для хэшированных ассетов.

## 6. Облако и внешние сервисы

- **Yandex Managed PostgreSQL** / **Managed Redis** (целевая операционная схема для MVP контура при развёртывании в облаке Yandex).
- **Yandex Object Storage** (S3 API); единое облако с VM при необходимости.
- OAuth-провайдеры **Yandex ID**, **T-ID** — согласовано с SRS.

## 7. Согласование с SRS / NFR (важно)

Спека продукта в **[[../../requirements/NFR|NFR]]** описывает **целевой** масштаб: микросервисы, **Kubernetes** / **HPA**, **ClickHouse** для аналитики, стек **Prometheus / Grafana / ELK / Jaeger**, отдельно **imgproxy** для превью изображений, **Firebase FCM**, расширенный набор интеграций.

**Эта заметка описывает инженерный контур текущего задокументированного решения:** модульный монолит **ASP.NET Core 8**, **Next.js**, managed PostgreSQL/Redis/Object Storage у Yandex, метрики через **middleware + Postgres metrics_events**, дашборд **recharts** в админке, ошибки через Postgres + Serilog — без необходимости на этом шаге выносить каждый блок в Kubernetes.

| Тема NFR / SRS | Продуктовая цель | Текущий инженерный контур | Дальнейшие шаги |
|----------------|------------------|----------------------|----------------|
| Микросервисы / K8s | NFR-SC | Один монолит API | Декомпозиция по ADR после нагрузки |
| ClickHouse для аналитики | NFR-SC | Агрегаты в Postgres + recharts для админа | Вынести поток событий при росте |
| imgproxy | NFR-PF-005 | next/image поверх S3 | При необходимости слой imgproxy перед S3/CDN |
| Prometheus / ELK / Jaeger | NFR-OBS | Serilog + таблицы + web-vitals | Подключать по необходимости SLO |

До явного решения любое расхождение трактовать так: **требования к продукту остаются в SRS/NFR**; реализация и версии инструментов — в этой заметке и в кодовых репозиториях.

## Связь с репозиториями GitHub

- [COOKieProjectTeam — cookie-frontend](https://github.com/COOKieProjectTeam/cookie-frontend), [cookie-backend](https://github.com/COOKieProjectTeam/cookie-backend): фактический `package.json` / `.csproj` может слегка отличаться по минор-м версиям — выровнять таблицы §1 здесь после спринта.

## Программное и системное видение (UML-пайплайн)

Детали пакетов и развёртывания см. заготовки [[../software/implementation-views]] и [[../system/deployment-views]], ADR при появлении.

## Связь с презентацией (summary)

После правок здесь поддерживать **[[../../summary/README|summary/README]]** и визуальную доску в согласии с этим каноном: краткий блок «Стек», легенда слоёв, без полного переноса таблиц. Доска — резюме для аудитории, не источник правды для спеки или кода.

## HumanOnly

- После синхронизации версий зависимостей в репозиториях — обновить миноры в таблице §1.
