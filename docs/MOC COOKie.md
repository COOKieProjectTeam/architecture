---
date: 2026-05-03
topic: "MOC — проект COOKie"
section: projects
status: seed
ai_assisted: true
preset: formal
sync_phase: dual_so_t
---

# MOC — проект COOKie

**Пресет:** `formal` (каркас из [[Template/Projects/README|Template/Projects]], `preset-formal/`).  
**Фаза зеркалирования:** `dual_so_t` — канон текста спецификаций в этом vault; опубликованный снимок в репозитории **architecture** (`docs/`); подробнее [[Knowledge/Development/Projects/COOKie/SYNC|SYNC.md]].  
**Мастер пайплайна (REQ+UML) в проекте:** [[Knowledge/Development/Projects/COOKie/meta/Agent Workflow — REQ+UML (мастер)|Agent Workflow — REQ+UML (мастер)]].  
Общий пайплайн для любого проекта — [[Knowledge/Development/Projects/MOC Projects|MOC Projects]]. Теория: [[Knowledge/Development/Requirements/Agent Workflow — от требований к спецификации|Agent Workflow — требования]] → [[Knowledge/Development/Architecture/Agent Workflow — архитектура ИС и UML|Agent Workflow — архитектура ИС и UML]]; курсы: [[Knowledge/Development/Requirements/MOC Управление требованиями|MOC «Управление требованиями»]], [[Knowledge/Development/Architecture/MOC UML Course|MOC UML]].

**Состояние требований:** первичный импорт из репозитория (дата и файл — [[Knowledge/Development/Projects/COOKie/meta/sources-and-sessions|источники и сессии]]); затем пакет согласования **концепции продукта** (2026-05-03): тариф **Pro**, интеграции 2+2, правки SRS/FRS/NFR/meta, см. журнал Wiki. **Канон смысла** — заметки в vault; **официальная Git-копия** дерева проекта и правила синхронизации — [[SYNC|SYNC.md]] (`dual_so_t`).
**GitHub Projects (org v2):** [проект «cookie»](https://github.com/orgs/COOKieProjectTeam/projects/2), к проекту привязаны репозитории `architecture`, `cookie-frontend`, `cookie-backend`.

**REQ+UML (мастер): этапы §1–§5 закрыты** на **2026-05-03**. §1: рамка, UC, канон доски [[Knowledge/Development/Projects/COOKie/summary/COOKie-v2.0.excalidraw|COOKie-v2.0.excalidraw]]; §2: [[Knowledge/Development/Projects/COOKie/meta/stakeholders|стейкхолдеры]], [[Knowledge/Development/Projects/COOKie/meta/sources-and-sessions|источники]]; §3–§4: [[requirements/verification-validation|verification-validation]] (REQ §3, REQ §4); **§5:** MoSCoW в [[requirements/prioritization|prioritization]], верификация/валидация — **REQ §5** в [[requirements/verification-validation|verification-validation]]. **§6–§7:** SoT задач = **GitHub** ([COOKieProjectTeam](https://github.com/COOKieProjectTeam)), см. **REQ §6–§7** в verification-validation; трассировка — [[requirements/traceability|traceability]], формат задач — [[process/github-issue-format|github-issue-format]], планирование — [[process/sprints/Sprint-01-planning|Sprint 01]], [[process/sprints/Sprint-02-planning|Sprint 02]]; CR — [[changes/README|журнал]] по мере использования.

## Summary / презентация

- [[Knowledge/Development/Projects/COOKie/summary/README|summary/README]] — презентация в Excalidraw (локальная доска); **канон текста стека:** [[architecture/technical/tech-stack|tech-stack]]

## Meta

- [[Knowledge/Development/Projects/COOKie/meta/requirements-framing|Рамка требований (§REQ-1)]]
- [[Knowledge/Development/Projects/COOKie/meta/glossary|Глоссарий]]
- [[Knowledge/Development/Projects/COOKie/meta/stakeholders|Стейкхолдеры]]
- [[Knowledge/Development/Projects/COOKie/meta/sources-and-sessions|Источники и сессии]]
- [[Knowledge/Development/Projects/COOKie/meta/lifecycle|ЖЦ и стандарты]]

## Требования

- [[Knowledge/Development/Projects/COOKie/requirements/BRD|BRD]]
- [[Knowledge/Development/Projects/COOKie/requirements/SRS|SRS]]
- [[Knowledge/Development/Projects/COOKie/requirements/FRS|FRS]] (опционально до UI)
- [[Knowledge/Development/Projects/COOKie/requirements/NFR|NFR]]
- [[Knowledge/Development/Projects/COOKie/requirements/prioritization|Приоритизация]]
- [[Knowledge/Development/Projects/COOKie/requirements/verification-validation|Верификация и валидация]]
- [[Knowledge/Development/Projects/COOKie/requirements/traceability|Трассировка]]

## Изменения

- [[Knowledge/Development/Projects/COOKie/changes/README|Change Request / журнал]]

## Архитектура ИС

_Заметки ниже — оглавление видов; информационная модель, программные и системные проекции в полном объёме и **пакет UML-диаграмм** дополняются по мере методологии после каркаса BRD/SRS. Визуальный дизайн экранов см. [[requirements/FRS|FRS]] (каркас) и будущие дополнения._

- [[Knowledge/Development/Projects/COOKie/architecture/README|Оглавление уровней]]
- [[Knowledge/Development/Projects/COOKie/architecture/technical/tech-stack|Технологический стек (канон текста)]]
- [[Knowledge/Development/Projects/COOKie/architecture/functional/use-cases|Функциональная]]
- [[Knowledge/Development/Projects/COOKie/architecture/information/domain-model|Информационная]]
- [[Knowledge/Development/Projects/COOKie/architecture/software/implementation-views|Программная]]
- [[Knowledge/Development/Projects/COOKie/architecture/system/deployment-views|Системная]]
- [[Knowledge/Development/Projects/COOKie/architecture/assets/README|Диаграммы / assets]]

## Продукт (обзор для стейкхолдеров)

- [[Knowledge/Development/Projects/COOKie/product/overview|Обзор продукта]]

## Методология (стартап)

- [[Knowledge/Development/Projects/COOKie/process/methodology|Методология поставки]] — ритм (2 недели), freeze на спринт, GitHub SoT задач ([[Knowledge/Development/Projects/COOKie/SYNC|SYNC]])
- [[Knowledge/Development/Projects/COOKie/process/github-issue-format|Формат GitHub Issues]] и метки
- [[Knowledge/Development/Projects/COOKie/process/sprints/README|Спринты: planning / review / retro]] — [[Knowledge/Development/Projects/COOKie/process/sprints/Sprint-01-planning|Sprint 01]], [[Knowledge/Development/Projects/COOKie/process/sprints/Sprint-02-planning|Sprint 02]]

## Репозиторий Git (опубликованное зеркало)

Локальный клон **`COOKieProjectTeam/architecture`** (`C:\Users\volde\COOK\architecture`): дерево этой документации в **`docs/`** ветка **`main`**, обновление из vault описано в [[Knowledge/Development/Projects/COOKie/SYNC|SYNC.md]].

## Связи

- [[Knowledge/Index|Knowledge/Index.md]]
- [[Knowledge/Wiki/index|Knowledge/Wiki/index.md]]

## HumanOnly

- 
