# COOKie — архитектурное зеркало документации

Центральный репозиторий [COOKieProjectTeam/architecture](https://github.com/COOKieProjectTeam/architecture): официально опубликованная копия дерева документации проекта **COOKie** каталог **`docs/`** (ветка **`main`**).

**Источник правды:** Obsidian **`Knowledge/Development/Projects/COOKie/`** — правите там, затем обновляйте здесь тем же деревом через PR по политике **`dual_so_t`** в [`docs/SYNC.md`](docs/SYNC.md) (ветка для синка любая временная).

---

## О продукте

Выжимка и границы MVP — [`docs/product/overview.md`](docs/product/overview.md); спеки — [`docs/requirements/`](docs/requirements/) (`BRD`, `SRS`, …).

---

## Код и задачи


| Репозиторий                                                             | Роль                      |
| ----------------------------------------------------------------------- | ------------------------- |
| [cookie-frontend](https://github.com/COOKieProjectTeam/cookie-frontend) | клиент MVP                |
| [cookie-backend](https://github.com/COOKieProjectTeam/cookie-backend)   | API                       |
| **architecture**                                                        | этот снимок в **`docs/`** |


- Орг-проект (Projects v2) **«cookie»** — [ссылка](https://github.com/orgs/COOKieProjectTeam/projects/2); полный процесс: [`docs/process/github-project-cookie.md`](docs/process/github-project-cookie.md)
- Трассировка требование ↔ GitHub Issue: [`docs/requirements/traceability.md`](docs/requirements/traceability.md)
- Формат задач: [`docs/process/github-issue-format.md`](docs/process/github-issue-format.md)
- Специфический чек‑лист SoT / CRM / спринт: см. блок **REQ §6–§7** в [`docs/requirements/verification-validation.md`](docs/requirements/verification-validation.md).

---

## Входные точки по `docs/`


| Область                                              | Файл                                                                                        |
| ---------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| Оглавление проекта                                   | [`docs/MOC COOKie.md`](docs/MOC%20COOKie.md)                                                |
| Синхронизация vault↔repo, конфликты, версионирование | [`docs/SYNC.md`](docs/SYNC.md)                                                              |
| Требования и верификация                             | [`docs/requirements/`](docs/requirements/), в первую очередь `SRS`, `verification-validation.md` |
| Projects v2 **«cookie»** (доска, секреты, метки Area) | [`docs/process/github-project-cookie.md`](docs/process/github-project-cookie.md)             |


Остальной каталог («архитектура ИС», `meta`, `process`, `changes`, `summary`) — см. оглавление в **MOC** и в [`docs/architecture/README.md`](docs/architecture/README.md).

---

## Наследие в корне

`CONTRIBUTING` / `ORGANIZATION` — справочно; канонический процесс — в **`docs/process/`** и SYNC.
