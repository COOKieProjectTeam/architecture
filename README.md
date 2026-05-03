# COOKie — архитектурное зеркало и документация

Центральный репозиторий организации [COOKieProjectTeam/architecture](https://github.com/COOKieProjectTeam/architecture) для **ветки документации и архитектурных текстов продукта COOKie** в режиме **Obsidian Vault → этот репозиторий** (детально — ниже и в дереве документации).

English: canonical wording of requirements and architecture notes is authored in Obsidian (`Knowledge/Development/Projects/COOKie/`); this repo publishes the same structure under **`docs/`** via PRs unless the team formally enables two-way edits (`dual_so_t` — see [`docs/SYNC.md`](docs/SYNC.md)).

---

## О продукте (выжимка)

**COOKie** — комплексное веб-приложение для осознанного **плана питания** и управления каталогом **рецептов** с **КБЖУ**, заготовкой под интеграции со службами доставки (**Pro**) и сбором базовых событий аналитики. Расшифровка вижна, ограничения MVP vs Phase 2–3 и тарификация **Free/Pro** — в [`docs/product/overview.md`](docs/product/overview.md) и в блоке спецификаций ([`requirements/SRS`](docs/requirements/SRS.md), BRD/NFR/FRS в том же каталоге).

---

## Связка с кодом и задачами

| Репозиторий       | Роль |
|-------------------|------|
| [cookie-frontend](https://github.com/COOKieProjectTeam/cookie-frontend) | клиент MVP |
| [cookie-backend](https://github.com/COOKieProjectTeam/cookie-backend)  | API и домен |
| **architecture** (этот) | текстовые спеки, архитектура ИС, процесс |

- **Kanban организации:** [Project #2 (cookie)](https://github.com/orgs/COOKieProjectTeam/projects/2)
- Трассировка требование ↔ задача GitHub — [`docs/requirements/traceability.md`](docs/requirements/traceability.md)
- Формат issue — [`docs/process/github-issue-format.md`](docs/process/github-issue-format.md)
- Спринты (пример): [`docs/process/sprints/Sprint-01-planning.md`](docs/process/sprints/Sprint-01-planning.md), [`Sprint-02-planning.md`](docs/process/sprints/Sprint-02-planning.md)

---

## Навигация по `docs/`

На GitHub всё оглавление с **wikilink-ами как в Obsidian** читается лучше в IDE или в Vault; здесь указаны главные точки входа под **Markdown-URLs**:

| Область | Входная заметка / файл |
|---------|-------------------------|
| Оглавление проекта и статус методологии | [`docs/MOC COOKie.md`](docs/MOC%20COOKie.md) |
| Зеркалирование vault ↔ repo, версии док-пакета, GitHub-связки | [`docs/SYNC.md`](docs/SYNC.md) |
| Требования | [`docs/requirements/BRD.md`](docs/requirements/BRD.md), [`SRS`](docs/requirements/SRS.md), [`FRS`](docs/requirements/FRS.md), [`NFR`](docs/requirements/NFR.md), приоритеты [`prioritization.md`](docs/requirements/prioritization.md), верификация [`verification-validation.md`](docs/requirements/verification-validation.md) |
| Архитектура ИС | [`docs/architecture/README.md`](docs/architecture/README.md), [`tech-stack.md`](docs/architecture/technical/tech-stack.md), use cases / deployment — рядом в том же дереве |
| Мета | [`docs/meta/glossary.md`](docs/meta/glossary.md), стейкхолдеры, источники, жизненный цикл (`docs/meta/`) |
| Процесс | методология спринта, формат задач (`docs/process/`), шаблоны review/retro в `docs/process/sprints/` |
| Журнал CR | [`docs/changes/README.md`](docs/changes/README.md) |
| Summary / презентация доски | [`docs/summary/README.md`](docs/summary/README.md) (тяжёлую доску `.excalidraw` из vault в Git не обязательно класть без договорённости) |

---

## Куда класть содержательные правки

1. **Первая остановка** — дерево **`Knowledge/Development/Projects/COOKie/`** в Obsidian (BRD/SRS/архитектура/спринт-планы/traceability при необходимости).
2. **Второе** — копируете содержимое этой папки в **`docs/`** этого клона, с **той же относительной структурой** (экспорт из vault сохранил соглашение: `SRS.md` ⇒ `architecture/docs/requirements/SRS.md` и т.д.).
3. Оформление **pull request в `main`** (частая рабочая ветка: `docs/sync-obsidian-cookie` или аналог).

Локально удобно держать рядом, например:  
`…\Documents\Obsidian Vault\Knowledge\Development\Projects\COOKie\` · `…\COOK\architecture\docs\`.

**Исключения при копировании:** по желанию не переносить `summary/*.excalidraw` или служебные скрипты — см. блок «Исключить из зеркала» в [`docs/SYNC.md`](docs/SYNC.md).

Подробнее о фазах **`vault_only`** и **`dual_so_t`**, таблице соответствия файлов vault↔repo и правилах при конфликтах см. в [`docs/SYNC.md`](docs/SYNC.md).

---

## Что после merge этого репозитория (ориентиры плана проекта COOKie)

После того как PR с деревом документации влит в `main`, имеет смысл:

**Пункт 5 — формально включить зеркально-двухстороннюю политику (по готовности команды):**

- Проставить в [`docs/SYNC.md`](docs/SYNC.md) вверху чеклисты фазы **`dual_so_t`**, когда согласовали режим редактирования (смысл уже расписан в разделах **«Конфликты и приоритет»** и **«Синхронизация после перехода на dual_so_t»** в том же файле).
- Аналогично обновить чеклист в копии **SYNC** в Obsidian, чтобы два источника не расходятся семантически.

**Пункт 6 — выровнять operational SoT-декларации:**

- Пройти [`docs/requirements/verification-validation.md`](docs/requirements/verification-validation.md) (блок REQ по источникам правды / GitHub) и при необходимости добавить строку про зеркальный `architecture` уже как опубликованный снимок.
- В [`docs/MOC COOKie.md`](docs/MOC%20COOKie.md) сменить `sync_phase`/описание, если вы вышли из чистого `vault_only`.

---

## Прочее в корне репозитория (наследие)

Каталог **`diagrams/`**, **`archive/`**, а также статичные **`LICENSE`**, возможно исторические **`CONTRIBUTING.md`** / **`ORGANIZATION.md`** — не являются источником канона набора документации **пакета 2.x**. Их имеет смысл либо оставить как архив диаграмм PlantUML из старых версий пайплайна (с отсылкой из SRS там, где упомянут временный файл схемы БД), либо аккуратно перенести в `archive/`. Навигация для команды задаётся оглавлениями **`docs/`** выше.

---

## Автоматизация

Проверки **markdown**, **сломанных http-ссылок** и синтаксиса **PlantUML** в этом репозитории **отключены** намеренно: качество и полнота спецификации задаются в Obsidian и ревью PR. При желании ограниченную проверку можно вернуть отдельным workflow позже.
