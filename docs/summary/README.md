---
date: 2026-05-03
topic: "Summary — презентационная доска проекта COOKie"
section: projects
ai_assisted: true
---

# Summary / презентация

Каталог **`summary/`** — **визуальная витрина** проекта в **Excalidraw**. На [[COOKie-v2.0.excalidraw]] две роли совмещены:

1. **Презентация** — **легенда стека**, схемы потоков, **генерируемые Use Case‑диаграммы** (`genucd_`).
2. **Структурный конспект спеки** без путей к файлам на холсте — вертикальная колонка **Excalidraw Frames** с ID (BC-*, MET-*, FR-*, NFR‑категории, процесс, MoSCoW, REQ+UML): элементы префикса **`gensum_*`**, патч‑скрипт `summary/_expand_doc_frames.py` (идемпотентный повторный запуск).

Полный текст артефактов остаётся в vault — таблица источников ниже. Конспект на доске **не заменяет** BRD/SRS/NFR; при расхождении побеждает markdown (**[[../architecture/technical/tech-stack|tech-stack]]**, **[[../requirements/NFR|NFR]]**, **[[../requirements/SRS|SRS]]**) до CR.

Текстовые **акторы и UC** — канон в [[../architecture/functional/use-cases|architecture/functional/use-cases]]; регенерация UC‑овала: из каталога проекта **`python summary/_gen_uc_diagrams.py`**, затем обязательно **`python summary/_expand_doc_frames.py`** — чтобы восстановить `frameId` и рамку `gensum_frm_use_cases` у `genucd_*`.

Локальный файл [[COOKie-v2.0.excalidraw]] — презентационная доска (**v2.0**, раскладка после §1 REQ+UML доведена вручную). Если UC‑блок дополняли вручную (ид не `genucd_*`), **`_gen_uc_diagrams.py` не запускать** — иначе ручное будет не затронуто, но автоген пересоздастся.

**Вне презентации:** трассировка, CR, спринты — в [[../requirements/traceability|requirements]], [[../changes/README|changes]], [[../process/sprints/README|process/sprints]]. **Синк** репозитория документации с vault — только **после** стабилизации текстов в vault (включая tech stack).

Файлы сцен **`*.excalidraw`** хранятся **только в Obsidian vault**; в этот репозиторий они **не коммитятся** — см. [SYNC.md](../SYNC.md) (раздел «Ручной экспорт зеркала») и шаблон `docs/summary/*.excalidraw` в `.gitignore`.

## Публичная доска (Excalidraw+)

После публикации на [Excalidraw](https://excalidraw.com) (или совместимом шаринге) вставьте ссылку — чтобы презентация открывалась **без Obsidian**:

- **URL доски:** <https://excalidraw.com/#json=Wh22vr-9c91ura4eF_844,uFBULH0-tdGJshA5oz164w>
- **Дата публикации / комментарий:** 2026-05-04 — витрина на Excalidraw+; **пока прежняя** опубликованная версия (не совпадает пословно с последним локальным [[COOKie-v2.0.excalidraw]] в vault).

Тот же URL имеет смысл продублировать в [[../SYNC|SYNC]] («Публичная презентационная доска»), если читаете доку из репозитория **architecture** без Obsidian.

**Импорт сцены в браузер на [excalidraw.com](https://excalidraw.com):**

- **Статус (2026‑05):** у автора при импорте локальных `COOKie-v2.0*.excalidraw` в веб по-прежнему появляется `Error: invalid file`; разбор и исправление **отложены**. Локальная структура JSON при этом проходит скрипт `_debug_excalidraw_import.py` (это не эквивалент успешному импорту в браузере).
- Открывать сцену через **Open** загрузкой файла, а не через импорт **Library** (библиотека ждёт формат `excalidrawlib`).
- При необходимости попробуйте производный **`COOKie-v2.0.web.excalidraw`** (без `type: frame` и `frameId`) — записывает `summary/_export_excalidraw_web_flat.py`, вызывается автоматически после `python summary/_expand_doc_frames.py`.
- Проверки JSON из CLI: `python summary/_debug_excalidraw_import.py` и при необходимости дополнительные пути файлов.

## Источники содержимого в vault

| На доске (конспект / тезисы) | Полные заметки |
|-------------------|----------------|
| Оглавление + разделы по Frame | тот же набор, что строки ниже; скрипт `summary/_expand_doc_frames.py` |
| Идея, продукт, стейкхолдеры | [[../product/overview|product/overview]], [[../requirements/BRD|requirements/BRD]], [[../meta/stakeholders|meta/stakeholders]] |
| Термины | [[../meta/glossary|meta/glossary]] |
| Функции (FR, родительские ID) | [[../requirements/SRS|requirements/SRS]] |
| Ограничения | [[../requirements/NFR|requirements/NFR]] |
| Приоритеты MVP / MoSCoW | [[../requirements/prioritization|prioritization]] |
| Процесс, верификация/валидация, REQ+UML кратко | [[../process/methodology|process/methodology]], [[../requirements/verification-validation|verification-validation]] |
| Техстек | [[../architecture/technical/tech-stack|architecture/technical/tech-stack]] |
| Use case | [[../architecture/functional/use-cases|architecture/functional/use-cases]], `summary/_gen_uc_diagrams.py` + см. последовательность с `_expand_doc_frames.py` выше |
| Диаграммы уровнем ниже | [[../architecture/README|architecture/*]], [[../architecture/assets/README|architecture/assets]] |

## HumanOnly

- 
