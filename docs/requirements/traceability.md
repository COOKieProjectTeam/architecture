---
date: 2026-05-03
topic: "COOKie — трассировка"
section: projects
ai_assisted: true
---

# Трассировка требований

_Стартовая матрица «бизнес → система». Расширять связями на тесты и задачи по мере появления артефактов. В таблице используются обычные markdown-ссылки, чтобы не ломать разметку столбцов._

**Колонки «Issue (frontend)» и «Issue (backend)»:** ссылки вида `https://github.com/COOKieProjectTeam/cookie-frontend/issues/N` и `…/cookie-backend/issues/N` после заведения задач; до этого «—». Тело задачи в GitHub — по [формату issue](../process/github-issue-format.md); блок **Trace** (FR, путь к vault) обязателен для связки с требованиями.

Полноценная **информационная (доменная) модель**, набор **UML-диаграмм** (активность, DFD, компоненты, развёртывание и т.д.) и **визуальный дизайн** по FRS вносятся в документацию **отдельными этапами позже** — по мере методологии и привязки к issues. В этой матрице не требуется ссылаться на ещё не готовые виды; связь с задачами добавляйте, когда артефакт появился.

| REQ ID | Артефакт / модель | Issue (frontend) | Issue (backend) | Примечание |
|--------|-------------------|------------------|-----------------|------------|
| BC-001 | [BRD BC-001](./BRD.md), [SRS §1–3](./SRS.md), рост/воронка | — | — | Ориентир ~1000 users / 4 мес MVP (BRD); при декомпозиции — epic в `architecture` или rollup |
| BC-002 | [SRS §2 US/тариф](./SRS.md); [BRD MET-PROD-002](./BRD.md) | — | [cookie-backend#11](https://github.com/COOKieProjectTeam/cookie-backend/issues/11) | Заглушка тарифа/лимитов MVP (Sprint 1) |
| BC-003 | [SRS §7 интеграции](./SRS.md); FR-OR, INT-API-006 | — | — | Минимум 2 ритейлера + 2 службы доставки |
| — (качество) | [NFR §5 PF/SC/AV](./NFR.md) | — | — | Масштаб и SLO под рост |
| FR-RS-001 … | Текст SRS, [use cases](../architecture/functional/use-cases.md) (рамка сценариев); UC↔FR — [verification-validation](./verification-validation.md) REQ §3 | [cookie-frontend#11](https://github.com/COOKieProjectTeam/cookie-frontend/issues/11), [cookie-frontend#12](https://github.com/COOKieProjectTeam/cookie-frontend/issues/12) | [cookie-backend#13](https://github.com/COOKieProjectTeam/cookie-backend/issues/13), [cookie-backend#14](https://github.com/COOKieProjectTeam/cookie-backend/issues/14), [cookie-backend#15](https://github.com/COOKieProjectTeam/cookie-backend/issues/15) | Список/карточка рецепта + КБЖУ в API (Sprint 2); диаграммы UC/UML дополняются позже без смены границ FR |
| FR-PS-001 | [SRS](./SRS.md) §3 ingestion | [cookie-frontend#13](https://github.com/COOKieProjectTeam/cookie-frontend/issues/13) | [cookie-backend#16](https://github.com/COOKieProjectTeam/cookie-backend/issues/16) | MVP путь источников (Sprint 2) |
| FR-AN-001 | [SRS](./SRS.md) § analytics / события | [cookie-frontend#14](https://github.com/COOKieProjectTeam/cookie-frontend/issues/14) | [cookie-backend#17](https://github.com/COOKieProjectTeam/cookie-backend/issues/17) | Событие просмотра рецепта (Sprint 2) |
| FR-US-001 (каркас S1) | [SRS §2 пользователь / сессии](./SRS.md) | [cookie-frontend#9](https://github.com/COOKieProjectTeam/cookie-frontend/issues/9) | [cookie-backend#10](https://github.com/COOKieProjectTeam/cookie-backend/issues/10) | Регистрация/вход/JWT MVP (Sprint 1); см. также инфра-issues ниже по планированию спринта |
| — (инфра S1) | Scaffold: Clean Architecture + EF Core + ThemeProvider + Axios | [cookie-frontend#25](https://github.com/COOKieProjectTeam/cookie-frontend/issues/25), [cookie-frontend#26](https://github.com/COOKieProjectTeam/cookie-frontend/issues/26) | [cookie-backend#23](https://github.com/COOKieProjectTeam/cookie-backend/issues/23) | Инфраструктурный каркас Sprint 1; нет прямого FR — обеспечивают FR-US-001 |
| DR-REC | Текст [SRS §6](./SRS.md); опубликованный снимок пакета — [SYNC](../SYNC.md) | — | — | Полноценная домен-модель, схема БД в нотации моделирования и прочие UML — добавляются в `architecture/` и сюда (issues) позже; старые артефакты из legacy-репо не используются |

## HumanOnly

- 

