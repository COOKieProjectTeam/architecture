# GitHub Project v2 «cookie» (COOKie)

Единый org-level **Projects v2** для всего продукта: **issues и PR из привязанных репозиториев** (`architecture`, `cookie-frontend`, `cookie-backend`) попадают в один поток работ.

## URL

https://github.com/orgs/COOKieProjectTeam/projects/2  

Краткая ссылка также в корневом [README архитектурного репозитория](../../README.md) и одной строкой в Obsidian MOC проекта (`MOC COOKie`).

## Представления (рекомендуемые)

1. **Table** (`View 1` или переименовать в `Backlog`) — список с фильтрами по репозиторию, статусу, области.
2. **Board / Kanban** — группировка по системному полю **Status**. Колонки по смыслу:
   - **Todo**
   - **In progress**
   - **In review**
   - **Done**

При расхождении с уже выбранными на проекте опциями **Status**, выровняйте названия в UI один раз под эту шкалу (или переименуйте колонки доски так, чтобы команда понимала и не дублировала два «готово»).

## Область (Area): метки Issues

Отдельное single-select поле в Project необязательно: в организации уже используются метки задач **`area:frontend`**, **`area:backend`**, **`area:infra`**, **`area:docs`** (зеркально в frontend и backend). Ставьте **ровно одну** `area:*` там, где ясно, куда относится работа — так проще фильтровать backlog и понимать, какое репозиторию «владеет» вертикалью.

При желании добавьте в Project пользовательское поле **Area** и синхронизируйте с метками вручную или позже через GraphQL‑автоматизацию — но **источник дисциплины по умолчанию** — именно метки.

## Связка с задачами

- После создания issue **канонический текст** остаётся в GitHub: см. [github-issue-format](github-issue-format.md), блоки **Goal / Scope / Trace / Acceptance / Companion**.
- Репозиторий **architecture** связан с проектом: для задач только по документации/диаграммам используйте **`area:docs`** (метка на issue в этом репо).

## Автоматизация (cookie-frontend, cookie-backend)

В этих двух кодовых репозиториях должен быть workflow **Add issue to COOK org project** (см. эталонный YAML ниже): при **`issues:opened`** карточка добавляется в проект №2 через [actions/add-to-project](https://github.com/actions/add-to-project).

### Если `git push` отвергает файл в `.github/workflows/`

При push по **HTTPS**, если OAuth-токен не имеет scope **`workflow`**, GitHub возвращает ошибку вида *refusing to allow an OAuth App to create or update workflow … without `workflow` scope*.

**Варианты:** интерактивно `gh auth refresh -h github.com -s workflow -s repo -s read:org`, затем снова `git push`; либо **классический PAT** со scope **`workflow`** и **`repo`**; либо создать тот же файл через UI репозитория (**Add file**), скопировав YAML из блока ниже.

### Эталон `.github/workflows/add-issue-to-org-project.yml`

Идентично для **cookie-frontend** и **cookie-backend**:

```yaml
name: Add issue to COOK org project

on:
  issues:
    types:
      - opened

jobs:
  add-to-org-project-cookie:
    name: Org project cookie (#2)
    runs-on: ubuntu-latest
    steps:
      - uses: actions/add-to-project@v1.0.2
        with:
          project-url: https://github.com/orgs/COOKieProjectTeam/projects/2
          github-token: ${{ secrets.ADD_TO_PROJECT_PAT }}
```

### Секрет

Создайте в репозитории (**Settings → Secrets and variables → Actions**) секрет **`ADD_TO_PROJECT_PAT`**.

Стандартный **`GITHUB_TOKEN` при push/issue в репо обычно не имеет** прав на запись в org-level Project «cookie», поэтому нужен классический **PAT** или **fine-grained PAT** пользователя/org с доступом:

- **Classic PAT:** включите scope **`repo`** и **`write:project`** (для добавления элементов организационному проекту; при недостаче прав см. официально заявленную пару **`read:project`** + **`project`** или полный доступ к классической группе *project*, в зависимости от вашей конфигурации org).
- **Fine-grained:** выберите org **COOKieProjectTeam**, нужные кодовые репозитории и чтение/запись **Projects**.

Без этого секретa job завершится ошибкой авторизации до тех пор, пока PAT не будет добавлен (это осознанно, чтобы секрет явно конфигурировался владельцем org/repo).

Токены **не коммитьте** и не добавляйте в workflow как plain text.

### Проверка за ~1 минуту

1. Убедитесь, что `ADD_TO_PROJECT_PAT` задан для репозитория с workflow.
2. Создайте тестовый issue без merge в код (можно потом удалить закрытием не мержа).
3. Откройте [проект #2](https://github.com/orgs/COOKieProjectTeam/projects/2) и убедитесь, что карточка появилась в Table и на Board (может потребоваться обновить фильтры по репозиторию).

### GraphQL без `actions/add-to-project`

Если CLI (`gh`) на машине имеет нужные scopes (напр. **`read:project`**, чтобы читать `projectV2`), можно получить `node id` проекта мутациями через `gh api graphql` и задавать дополнительные поля после `addProjectV2ItemByContentId`: потребует хранить **NODE ID** пользовательских полей/опций. Для машины пользователя см. ошибку недостачи scopes — расширьте токен `gh auth login`.

## Спецификация и код

Не дублировать текст SRS целиком в проекте. Источники правды: **Obsidian vault** + **поля задачи/issue** + swagger и «золотые пути» в соответствующем репозитории после появления кода backend.
