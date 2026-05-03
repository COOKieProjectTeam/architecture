---
date: 2026-05-03
topic: "SYNC — COOKie: vault и репозиторий"
ai_assisted: true
---

# SYNC — зеркалирование vault и репозитория

**Проект:** COOKie  
**Последнее обновление записи:** 2026-05-03 (REQ §4: версионирование vault; таблица соответствия — фактический перенос v1 в vault).

## Текущая фаза

- [x] `vault_only` — правки спецификаций и архитектуры **только** в Obsidian vault (`Knowledge/Development/Projects/COOKie/`).
- [ ] `dual_so_t` — vault и репозиторий оба источники правды; действуют таблица путей и правило конфликтов ниже.

## Фаза `vault_only` (заполнять до переноса в репо)

- **Зеркало / витрина на диске (справочно):** локальный клон [репозитория `architecture`](https://github.com/COOKieProjectTeam/architecture), ориентир пути `C:\Users\volde\COOK\architecture` (HTTPS: `https://github.com/COOKieProjectTeam/architecture.git`). Экспорт из vault выполняется вручную по договорённости; см. блок «Ручной экспорт зеркала» и `dual_so_t` ниже.
- **Правило:** не редактировать файлы документации в репо от имени этого workflow, пока фаза не сменена (кроме явного запроса).

## Фаза `dual_so_t` (после переноса / договорённости)

### Таблица соответствия

Логический **монолит требований** в дереве `docs/requirements/` репозитория: имя файла, версия и дата импорта — [[meta/sources-and-sessions|источники и сессии]]. До `dual_so_t` ведущая копия — заметки vault.

| Артефакт (vault) | Путь в репозитории | Примечание |
|------------------|-------------------|------------|
| `requirements/BRD.md` | Монолит требований (репо, см. источники) | §1.2 scope, §2.1 BC-*, §10 продуктовые метрики |
| `requirements/SRS.md` | то же | §1.1 цель, §2.2 роли, §3–4 FR, §6 данные, §7 интеграции; §8 — отсылка к NFR |
| `requirements/FRS.md` | то же | §9 UI |
| `requirements/NFR.md` | то же | §5 NFR, §8 доп. безопасность |
| `meta/glossary.md` | то же | §1.3 + приложения A/B |
| `requirements/prioritization.md` | то же | Агрегация приоритетов из FR |
| `requirements/traceability.md` | то же | BC ↔ FR/NFR (стартовая матрица) |
| `requirements/verification-validation.md` | то же | Критерии проверяемости по workflow |
| `architecture/technical/tech-stack.md` | `docs/architecture/technical/` (или зеркало `architecture/` в целевом репо) | Свод технологического стека из NFR/SRS; доска summary — производная |

### Синхронизация документации с vault

После завершения **всех** правок текстовых артефактов в vault (в т. ч. `architecture/technical/tech-stack.md` и блоков презентации summary) имеет смысл выполнять экспорт зеркала в целевой репозиторий документации **одним проходом**. До этого момента ведущая копия — только vault (`vault_only`).

### Конфликты и приоритет

| Ситуация | Приоритет | Что делать |
|----------|-----------|------------|
| Расходится **смысл текста спецификации** или канонической архитектурной записи между vault и деревом этого репозитория без явной договорённости | Заметки в **Obsidian** (`Knowledge/Development/Projects/COOKie/`) | Истину фиксируем в vault; в `architecture` попадает только через экспорт (PR). Прямых «тихих» правок только в этом репо без отражения в vault допускать не следует. |
| Расходится только **разметка ссылок** (wikilink в Obsidian против относительных путей на GitHub) | Не ошибка содержательная | Выравниваем в vault; экспорт сохранит структуру `docs/`; точечную читаемость на GitHub дорабатываем там же или в этом PR. |
| Расходятся **номера задач / статусы** в `requirements/traceability` или спринтовых таблицах и факт в **GitHub Issues / Project / milestone** | **GitHub** | Истина по задачам — там; трассировка в документации обновляется под факт или следующим синком из vault после правки там. |

### Синхронизация после перехода на `dual_so_t`

1. Изменение требования или описания решения по канону проекта → сначала **правка соответствующей заметки в vault**, затем **обновление `docs/`** в этом репозитории одним коммитом/PR по тому же относительному пути (копированием из vault).  
2. Репозиторий **не** расширяет монолит SRS/BRD и т.д. обходными коммитами без зеркальных правок vault. Исключения — только с явным решением соавторов («hotfix описания ошибки readme» ≤ 2 абзацев) с немедленным дублем в vault.  
3. **Версионирование** набора документации — по таблице ниже «Версионирование спецификации»; принятые пакеты правок после MVP до **3.x** не поднимать без отдельного решения.  
4. Бэклог и текст задачи **не переносить** целиком в документацию; формат задач — `process/github-issue-format.md`; трассировка — `requirements/traceability.md`.

**Когда включать чеклист `dual_so_t`:** после того как команда зафиксировала переход из одностороннего зеркала (например, после merge PR с полным деревом документации в `main`) и операционно может соблюдать таблицы выше.

Если сводная доска из `summary/` опубликована на [Excalidraw](https://excalidraw.com) (или совместимом сервисе), продублируйте URL здесь — чтобы в репозитории была та же ссылка, что в `summary/README.md`.

| Поле | Значение |
|------|----------|
| **URL доски (Excalidraw+)** | |

## Версионирование спецификации (канон vault)

Цифры версии относятся к **пакету документации в vault** (не к номеру релиза продукта), пока действует фаза `vault_only`.

| Milestone | Версия | Смысл |
|-----------|--------|--------|
| Снимок только в репозитории (до переноса) | **0.5** | исторический ориентир в репо `architecture` (локально `…\COOK\architecture`) |
| Первый перенос в Obsidian vault | **1.0** | разбиение по заметкам BRD/SRS/… |
| Текущая линия (пакет 2026-05-03, доска summary) | **2.0** | в т. ч. [`COOKie-v2.0.excalidraw`](./summary/COOKie-v2.0.excalidraw) |
| После каждого **принятого CR** до конца MVP | **2.1**, **2.2**, … | повышается **только минор**; запись в [CR / журнал](./changes/README.md) |

**Мажорную** версию (**3.x**) не повышать до конца MVP без отдельного решения. Краткая фиксация дублируется в [verification-validation](./requirements/verification-validation.md), блок **REQ §4**.

## Интеграция с GitHub (спринты, Kanban)

**Организация:** [COOKieProjectTeam](https://github.com/COOKieProjectTeam). Репозитории:

| Репозиторий       | Base URL |
|-------------------|----------|
| cookie-frontend   | https://github.com/COOKieProjectTeam/cookie-frontend |
| cookie-backend    | https://github.com/COOKieProjectTeam/cookie-backend |
| architecture      | https://github.com/COOKieProjectTeam/architecture |

SSH (шаблон): `git@github.com:COOKieProjectTeam/<repo>.git` — при недоступном SSH использовать HTTPS URL из таблицы.

**Источники правды**

- **Тексты спецификаций:** этот vault (`Knowledge/Development/Projects/COOKie/`), фаза **`vault_only`** не снимается на этом шаге.
- **Бэклог и спринт (задачи):** **GitHub Issues** (+ по мере настройки Org-level **GitHub Project**). **Полное содержание задачи** (Goal, Scope, acceptance criteria, заметки) после создания issue — **только в GitHub**. В vault хранятся ссылки и дорожная карта: [[requirements/traceability|traceability]], файлы [[process/sprints/README|спринтов]] — без копирования тел issues.
- **URL Org Project:** [cookie (Project #2)](https://github.com/orgs/COOKieProjectTeam/projects/2)
- **Milestone = спринт:** планируются **`Sprint 1`**, **`Sprint 2`** в кодовых репозиториях; устаревшие недельные milestone’ы из наследия удалены или закрыты.
- **Метки трассировки:** см. [[process/github-issue-format|github-issue-format]] (предложение: `priority:must` / `priority:should` / `priority:could`, `area:frontend` / `area:backend` / `area:infra` / `area:docs`).

**Наследие:** открытый бэклог репозиториев организации **удалён** как несоответствующий пакету спецификации **2.0**; канон новых задач — спринтовые планы + трассировка + issues в GitHub.

Таблица **требование ↔ issue** — в [[requirements/traceability|traceability]]. В каждом issue — блок **Trace** (FR/UC/NFR и путь к vault) по [[process/github-issue-format|github-issue-format]]; полный текст SRS в issue не дублировать.

## Документация 2.0 и репозиторий `architecture`

Ведущая копия требований и проектных заметок COOKie в vault. Репозиторий **`architecture`** — зеркало / витрина для Git и внешних читателей; **синхронизация vault ↔ `architecture`** и переключение **`dual_so_t`** (ветка/правила конфликтов монолита в репо) — отдельное решение при переходе фазы (см. таблицу соответствия выше).

### Ручной экспорт зеркала (ветка `docs/sync-obsidian-cookie`)

- **Целевая ветка** в [architecture](https://github.com/COOKieProjectTeam/architecture): `docs/sync-obsidian-cookie` (локально: после `fetch`, `checkout` этой ветки; открыть PR в `main` при следующем экспорте).
- **Структура копирования из vault:** содержимое **`Knowledge/Development/Projects/COOKie/`** (все файлы и подпапки) кладётся в **`docs/`** корня репозитория `architecture`, с сохранением относительных путей (например `requirements/SRS.md` → `<repo>/docs/requirements/SRS.md`). После включения **`dual_so_t`** при необходимости свести дерево репозитория с монолитом по **таблице соответствия** выше.
- **Исключить из зеркала** при массовом копировании: тяжёлый файл [`summary/COOKie-v2.0.excalidraw`](./summary/COOKie-v2.0.excalidraw); канон доски для команды остаётся в vault, публикация — через блок «Публичная презентационная доска» выше. Привязка требований к задачам — [`requirements/traceability.md`](requirements/traceability.md) и планирование спринтов.

## HumanOnly

### Договорённости по проекту

- **REQ §2 (стейкхолдеры / источники / сбор)** закрывается артефактами `meta/stakeholders.md` и `meta/sources-and-sessions.md`; **RACI** — компактный пресет (матрица не ведётся до расширения круга ответственных). Запись сессий и методов — в `sources-and-sessions`, хронология в [[Knowledge/Wiki/log]].
