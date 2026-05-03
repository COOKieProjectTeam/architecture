---
date: 2026-05-03
topic: "COOKie — ЖЦ и стандарты"
section: projects
ai_assisted: true
---

# Модель жизненного цикла и стандарты

_Согласовано с единым каноном [[Knowledge/Development/Projects/MOC Projects|MOC Projects]] и мастером [[Agent Workflow — REQ+UML (мастер)|REQ+UML]] в этой папке `meta/`._

## Процесс поставки (vault-first)

1. **Спецификация и архитектура до ворот** — артефакты в vault (`requirements/*`, `architecture/*`, `meta/*`); порядок этапов — мастер REQ+UML и курсовые workflow в `Knowledge/Development/Requirements` и `Knowledge/Development/Architecture`.
2. **Ворота к реализации** — первый dev-спринт только после закрытия чек-листа готовности к реализации (архитектурный workflow); церемонии — заметки в [[../process/sprints/README|process/sprints/]].
3. **Реализация** — задачи и статусы спринта в **GitHub** (Issues / Projects); спецификации и модели остаются в vault; фаза зеркалирования — [[../SYNC|SYNC.md]].
4. **Изменения** — Change Request в [[../changes/README|changes/]], затем обновление требований / архитектуры и согласование с бэклогом.

## Продуктовые горизонты

- Сроки и фазы **MVP / roadmap** продукта — в [[../requirements/BRD|BRD]] и заметках требований; этот файл описывает **процесс**, а не календарь релизов.

## Стандарты / нормы

- ГОСТ 34 / 59795 для этого артефакта не зафиксированы; при необходимости согласовать отдельно.

См. также [[../process/methodology|методология поставки]] (ритм MVP, продуктовый контекст).

## HumanOnly

- 
