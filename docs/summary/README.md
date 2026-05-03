---
date: 2026-05-03
topic: "Summary — презентационная доска проекта COOKie"
section: projects
ai_assisted: true
---

# Summary / презентация

Каталог **`summary/`** — **визуальная витрина** проекта в **Excalidraw**. Содержимое доски **производное** от полных текстов в vault (см. таблицу ниже): идея, короткие **тезисы** (не полный BRD/SRS/NFR), **легенда стека**, **UML**, user flows, data flows. Изображения — при необходимости в [[../architecture/assets/README|architecture/assets]] или в репо документации после синка.

Текстовые **акторы и UC** — канон в [[../architecture/functional/use-cases|architecture/functional/use-cases]]; на доске блок «Use Case diagrams» регенерируется при необходимости: `python summary/_gen_uc_diagrams.py` из каталога проекта.

**Текстовый канон технологического стека:** [[../architecture/technical/tech-stack|architecture/technical/tech-stack]] (слои, ссылки на NFR/SRS). Блок стека на [[COOKie-v2.0.excalidraw]] — **презентационный пересказ**; при расхождениях с markdown **побеждает `tech-stack.md` + [[../requirements/NFR|NFR]] / [[../requirements/SRS|SRS]]** до CR.

Локальный файл [[COOKie-v2.0.excalidraw]] — презентационная доска (**v2.0**, раскладка после §1 REQ+UML доведена вручную). Блок **Use Case diagrams**: при регенерации только автоген‑элементов см. `summary/_gen_uc_diagrams.py` (префикс `genucd_`; перезапуск удалит и заново создаст такие элементы — если UC на доске ручные, скрипт не запускать).

**Вне презентации:** трассировка, CR, спринты — в [[../requirements/traceability|requirements]], [[../changes/README|changes]], [[../process/sprints/README|process/sprints]]. **Синк** репозитория документации с vault — только **после** стабилизации текстов в vault (включая tech stack).

## Публичная доска (Excalidraw+)

После публикации на [Excalidraw](https://excalidraw.com) (или совместимом шаринге) вставьте ссылку — чтобы презентация открывалась **без Obsidian**:

- **URL доски:** 
- **Дата публикации / комментарий:** 

Тот же URL имеет смысл продублировать в [[../SYNC|SYNC]] («Публичная презентационная доска»), если читаете доку из репозитория **architecture** без Obsidian.

## Источники содержимого в vault

| На доске (тезисы) | Полные заметки |
|-------------------|----------------|
| Идея | [[../product/overview|product/overview]], [[../requirements/BRD|requirements/BRD]] |
| Термины | [[../meta/glossary|meta/glossary]] |
| Функции | [[../requirements/SRS|requirements/SRS]] |
| Ограничения | [[../requirements/NFR|requirements/NFR]] |
| Техстек | [[../architecture/technical/tech-stack|architecture/technical/tech-stack]] |
| Use case | [[../architecture/functional/use-cases|architecture/functional/use-cases]], `summary/_gen_uc_diagrams.py` |
| Диаграммы уровнем ниже | [[../architecture/README|architecture/*]], [[../architecture/assets/README|architecture/assets]] |

## HumanOnly

- 
