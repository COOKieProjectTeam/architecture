---
date: 2026-05-03
topic: "Sprint 02 — planning"
sprint_number: 02
sprint_dates: "YYYY-MM-DD — YYYY-MM-DD (2 недели; задать при старте)"
section: projects
ai_assisted: true
---

# Sprint 02 — planning (Recipe core)

## Sprint goal

- Вертикаль **ядра рецепта** по **CRITICAL**: [[../../requirements/SRS|FR-RS-001]], [[../../requirements/SRS|FR-RS-002]]; отображение данных **FR-DE-001 / FR-DE-002**; старт ingestion **FR-PS-001** (один рабочий путь); базовые события **FR-AN-001** там, где уже есть UI/API.

## GitHub

- **Org Project URL:** [[../../SYNC|SYNC.md]] ([Project #2](https://github.com/orgs/COOKieProjectTeam/projects/2))
- **Milestone:** `Sprint 2`

**Дорожная карта issues** (формат задач — [github-issue-format](../github-issue-format.md)):

| Рабочее название (черновик) | Repo | Основная FR | Issue |
|-----------------------------|------|-------------|-------|
| Backend: recipe сущность / CRUD / список+фильтры MVP | backend | FR-RS-001, FR-RS-002 | [BE #13](https://github.com/COOKieProjectTeam/cookie-backend/issues/13) |
| Frontend: список рецептов и фильтры MVP | frontend | FR-RS-002 | [FE #11](https://github.com/COOKieProjectTeam/cookie-frontend/issues/11) |
| Backend + frontend: карточка рецепта (минимум вкладок) | both | FR-RS-003 (если укладывается; иначе cut) | [FE #12](https://github.com/COOKieProjectTeam/cookie-frontend/issues/12), [BE #14](https://github.com/COOKieProjectTeam/cookie-backend/issues/14) |
| Backend: КБЖУ и единицы в ответах API | backend | FR-DE-001, FR-DE-002 | [BE #15](https://github.com/COOKieProjectTeam/cookie-backend/issues/15) |
| Backend: парсер / очередь / статусы — один путь FR-PS-001 | backend | FR-PS-001 | [BE #16](https://github.com/COOKieProjectTeam/cookie-backend/issues/16) |
| Frontend: отображение статуса источника (если API готово) | frontend | FR-PS-001 | [FE #13](https://github.com/COOKieProjectTeam/cookie-frontend/issues/13) |
| Analytics: событие просмотра рецепта (pipeline минимум) | backend + frontend | FR-AN-001 | [FE #14](https://github.com/COOKieProjectTeam/cookie-frontend/issues/14), [BE #17](https://github.com/COOKieProjectTeam/cookie-backend/issues/17) |

**HIGH по остатку capacity** ([[../../requirements/prioritization|prioritization]]: FR-RS-003, FR-RS-005, FR-US-002) — добавлять только если ядро S2 закрыто; **MEDIUM** в S2 без явного scope creep не обещать.

## Объём из vault

- [[../../requirements/SRS|SRS]] §3 (каталог, данные рецепта), [[../../requirements/prioritization|prioritization]]; трассировка — [[../../requirements/traceability|traceability]].

## Риски и зависимости

- FR-RS-003 (богатая карточка) может потребовать отдельного cut; держать в одной паре FE/BE с общим Companion.
- Ingest зависит от внешних источников — заложить мок или один фикстурный источник.

## HumanOnly

- 
