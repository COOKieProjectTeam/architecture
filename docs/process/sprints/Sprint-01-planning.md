---
date: 2026-05-03
topic: "Sprint 01 — planning"
sprint_number: 01
sprint_dates: "YYYY-MM-DD — YYYY-MM-DD (2 недели; задать при старте)"
section: projects
ai_assisted: true
---

# Sprint 01 — planning (Foundation)

## Sprint goal

- Выровнять **сквозной каркас MVP** под **CRITICAL** из [[../../requirements/prioritization|prioritization]]: аутентификация и учёт тарифных лимитов ([[../../requirements/SRS|SRS]] FR-US-001 / UC-Authenticate), общий контур **API + клиента** с CI и окружениями, минимальный health-check и задел под каталог без обязательства полноты поиска в этом же спринте (explicit cut ниже).

## GitHub

- **Org Project URL:** см. блок в [[../../SYNC|SYNC.md]] (cookie, [Project #2](https://github.com/orgs/COOKieProjectTeam/projects/2))
- **Milestone:** `Sprint 1` в `cookie-frontend` и `cookie-backend` (milestones созданы совместно с `Sprint 2`)

**Дорожная карта issues** (формат задач — [github-issue-format](../github-issue-format.md)):

| Рабочее название (черновик) | Repo | Основная FR / UC | Issue |
|-----------------------------|------|-------------------|-------|
| Репозитории: контрибьютинг, ветки, CI smoke | frontend + backend | инфра (NFR минимум) | [FE #8](https://github.com/COOKieProjectTeam/cookie-frontend/issues/8), [BE #9](https://github.com/COOKieProjectTeam/cookie-backend/issues/9) |
| Backend: пользователь и сессия / JWT контур | backend | FR-US-001 | [BE #10](https://github.com/COOKieProjectTeam/cookie-backend/issues/10) |
| Frontend: экраны регистрации / входа / сессия | frontend | FR-US-001 | [FE #9](https://github.com/COOKieProjectTeam/cookie-frontend/issues/9) |
| Backend: заглушка тарифа / лимитов для последующего Pro | backend | FR-US-001, SRS §2.2 | [BE #11](https://github.com/COOKieProjectTeam/cookie-backend/issues/11) |
| Backend: health / readiness endpoints | backend | NFR наблюдаемость (минимум) | [BE #12](https://github.com/COOKieProjectTeam/cookie-backend/issues/12) |
| Frontend: клиент конфигурации окружений (API base URL) | frontend | зависимость от API | [FE #10](https://github.com/COOKieProjectTeam/cookie-frontend/issues/10) |
| Backend: scaffold Clean Architecture + EF Core + PostgreSQL | backend | инфра | [BE #23](https://github.com/COOKieProjectTeam/cookie-backend/issues/23) |
| Frontend: styled-components ThemeProvider + GlobalStyle | frontend | инфра | [FE #25](https://github.com/COOKieProjectTeam/cookie-frontend/issues/25) |
| Frontend: Axios HTTP client + auth interceptors | frontend | зависимость от API | [FE #26](https://github.com/COOKieProjectTeam/cookie-frontend/issues/26) |
| (опционально в рамках capacity) Compose / первый локальный compose-стек | backend (+ docs) | out-of-scope если нет времени — зафиксировать cut в HumanOnly | — |

**Cut (явно не обещаем в S1 если не успеваем):** полнотека поиска по каталогу, ingest [[../../requirements/SRS|FR-PS-001]], детальный тюнинг NFR чисел.

## Объём из vault

- Требования / эпики: [[../../requirements/SRS|SRS]] FR-US-001; граница MVP — [[../../requirements/prioritization|prioritization]], BC — [[../../requirements/traceability|traceability]].
- Входные артефакты без изменений с «прошлого спринта»: n/a (первый планируемый dev-спринт после spec 2.0).

## Риски и зависимости

- Выбор PSP и webhooks может не войти в S1 — не блокировать каркас auth без явного решения в planning.
- Парные FE/BE issues: сразу проставлять **Companion** после создания второй половины.

## HumanOnly

- 
