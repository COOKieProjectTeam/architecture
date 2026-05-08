---
date: 2026-05-03
topic: "COOKie — формат GitHub Issues"
section: projects
ai_assisted: true
---

# Формат GitHub Issues

Единые правила заголовка и секций для **Issues** в [COOKieProjectTeam](https://github.com/COOKieProjectTeam) (`cookie-frontend`, `cookie-backend`). Формы в каждом репозитории — **YAML issue forms** (`.github/ISSUE_TEMPLATE/`), с акцентом UI vs API см. описания полей там.

## Источник правды

**После создания issue канонический полный текст задачи** — **только в GitHub**. Этот файл описывает структуру для форм и ревью; **не дублируйте тела issues** в vault. В vault: ссылки на `issues/N` в [[../requirements/traceability|traceability]] и дорожные карты в [[sprints/README|спринтах]].

## Заголовок

`[S-T] <Компонент>: <глагол и объект>`  
Примеры: `[S1] API: JWT login по FR-US-001`, `[S1] UI: экран входа и сессия`.

## Тело issue (Markdown; поля формы зеркалят блоки)

```markdown
## Goal

## Scope (in / out)

## Trace

- FR:
- UC: (опционально)
- NFR: (если применимо)
- Ref: https://github.com/COOKieProjectTeam/architecture/blob/main/docs/requirements/FRS.md §FR-XX

## Acceptance criteria

## Companion

- Frontend: #… | Backend: #… — ссылка на парную задачу в другом репо при вертикали

## Notes
```

**Правило:** каждая задача с привязкой к требованию содержит заполненный блок **Trace**; после появления номеров — обновляется [[../requirements/traceability|traceability]].

## Метки (предложение для org)

В ячейках таблицы не используйте `[[note|alias]]`: символ `|` ломает разметку столбцов. Ниже — обычные markdown-ссылки.

| Метка                                                         | Назначение                                                                     |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| `priority:must`                                               | MoSCoW Must / CRITICAL из [prioritization](../requirements/prioritization.md) |
| `priority:should`                                             | Should / HIGH                                                                  |
| `priority:could`                                              | Could / MEDIUM                                                                 |
| `area:frontend` / `area:backend` / `area:infra` / `area:docs` | Зона работ                                                                     |
| опционально `requirements` или `trace:FR-xx`                  | Если удобно фильтровать по FR                                                  |

Приоритеты в issue согласовываются с [prioritization](../requirements/prioritization.md), не переопределяют SRS без CR.

## HumanOnly

- 
