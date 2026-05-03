---
date: 2026-05-03
topic: "COOKie — NFR"
section: projects
ai_assisted: true
---

# Нефункциональные требования

_Нефункциональные требования. Трассировка: [[../SYNC|SYNC]]. История импорта — [[../meta/sources-and-sessions|источники и сессии]]._

## Сводная таблица (экспресс)

| ID | Категория | Требование | Метрика / критерий |
|----|-----------|------------|-------------------|
| NFR-PF-001…005 | Производительность | Latency, поиск, карточка, RPS, изображения | См. подразделы ниже |
| NFR-SC-001…004 | Масштабируемость | Горизонтальное масштабирование, HPA, БД, объёмы | См. подразделы |
| NFR-AV-001…004 | Доступность | SLO, отказоустойчивость, degradation, health | См. подразделы |
| NFR-SEC-001…005 | Безопасность | JWT, RBAC, шифрование, rate limit, защиты, аудит | См. подразделы |
| NFR-OBS-001…005 | Наблюдаемость | Prometheus, ELK, tracing, алерты, Sentry | См. подразделы |
| NFR-L10N-001…004 | L10n / i18n | Языки, контент, TZ, валюты | См. подразделы |
| NFR-COMP-001…003 | Совместимость | Браузеры, моб. ОС, responsive | См. подразделы |
| SEC-001…003 | Безопасность (доп.) | Пентест, зависимости, secrets | См. §8 ниже |

## 5. Нефункциональные требования

### 5.1. Производительность (NFR-PF)

**NFR-PF-001**: API latency
- P50 (медиана): ≤ 200ms
- P95: ≤ 500ms
- P99: ≤ 1000ms

**NFR-PF-002**: Поиск рецептов
- Время ответа для поиска с фильтрами: P95 ≤ 300ms

**NFR-PF-003**: Загрузка карточки рецепта
- Полная загрузка (с изображениями): P95 ≤ 2000ms
- Time to First Byte (TTFB): ≤ 500ms

**NFR-PF-004**: Пропускная способность
- MVP: 100 запросов в секунду (RPS)
- Year 1: 500 RPS
- Year 2: 2000 RPS

**NFR-PF-005**: Оптимизация изображений (MVP)
- Исходник хранится в **едином качестве**; производные превью (thumbnail / medium / large и т.д.) генерируются по запросу через **[imgproxy](https://github.com/imgproxy/imgproxy)** (или совместимый кластер поверх объектного хранилища), без дублирования набора статических файлов для каждого размера
- Формат выдачи: WebP для веб, JPEG для fallback где нужно
- Ориентиры разрешений можно задавать в конфиге imgproxy и политике CDN (не обязательно фиксировать три отдельных файла в хранилище)
- Lazy loading для изображений вне viewport

### 5.2. Масштабируемость (NFR-SC)

**NFR-SC-001**: Горизонтальная масштабируемость
- Все микросервисы должны поддерживать horizontal scaling
- Stateless сервисы (кроме сессий в Redis)

**NFR-SC-002**: Автоматическое масштабирование
- Kubernetes HPA (Horizontal Pod Autoscaler):
  - Recipe Service: CPU > 70% → scale up
  - Parser Service: Queue depth > 100 → scale up
  - API Gateway: Request rate > 1000 RPS → scale up

**NFR-SC-003**: Масштабирование баз данных
- PostgreSQL: Read replicas для Recipe DB и User DB
- ClickHouse: Sharding для Analytics DB (2+ шарда)
- Redis: Redis Cluster с репликацией (3 ноды)

**NFR-SC-004**: Целевые объемы данных
- Year 1: 10,000 рецептов, 5,000 пользователей
- Year 2: 50,000 рецептов, 25,000 пользователей
- Year 3: 100,000 рецептов, 80,000 пользователей

### 5.3. Доступность (NFR-AV)

**NFR-AV-001**: Uptime SLO
- MVP: 99.5% (43 минуты downtime в месяц)
- Year 1+: 99.9% (43 минуты downtime в месяц)

**NFR-AV-002**: Отказоустойчивость
- Репликация критичных БД (PostgreSQL primary + replica)
- Резервные копии БД: ежедневные (retention 30 дней)
- Disaster recovery: RTO < 4 часа, RPO < 1 час

**NFR-AV-003**: Graceful degradation
- При недоступности Analytics Service: события буферизуются
- При недоступности Cache: fallback на БД
- При недоступности Parser Service: очередь накапливается

**NFR-AV-004**: Health checks
- Все сервисы должны экспонировать /health endpoint
- Kubernetes liveness и readiness probes
- Мониторинг health checks через Prometheus

### 5.4. Безопасность (NFR-SEC)

**NFR-SEC-001**: Аутентификация и авторизация
- JWT токены для аутентификации
- RBAC (Role-Based Access Control) для авторизации
- OAuth 2.0 для внешних провайдеров

**NFR-SEC-002**: Шифрование
- HTTPS для всех API endpoints (TLS 1.3)
- Шифрование паролей: bcrypt (cost factor 12)
- Шифрование чувствительных данных в БД: AES-256

**NFR-SEC-003**: Rate limiting
- API Gateway: 1000 запросов/час на IP для анонимных
- API Gateway: 5000 запросов/час на пользователя для авторизованных
- ИИ-диетолог: ограниченный лимит для **Free**; расширенный доступ для **Pro** (конкретные числа см. SRS FR-AI-001 вместе с продуктовой политикой)

**NFR-SEC-004**: Защита от атак
- CORS: whitelist доменов
- CSRF protection для форм
- XSS protection: санитизация пользовательского ввода
- SQL injection: использование parameterized queries (ORM)

**NFR-SEC-005**: Аудит
- Логирование всех изменений данных (audit log)
- Логирование аутентификации и авторизации
- Retention: 1 год для audit logs

### 5.5. Наблюдаемость (NFR-OBS)

**NFR-OBS-001**: Мониторинг метрик
- Prometheus для сбора метрик со всех сервисов
- Grafana для визуализации
- Метрики: latency, throughput, error rate, resource usage

**NFR-OBS-002**: Логирование
- Структурированные логи (JSON format)
- ELK Stack (Elasticsearch, Logstash, Kibana)
- Log levels: ERROR, WARN, INFO, DEBUG
- Retention: 30 дней для DEBUG, 90 дней для INFO/WARN, 1 год для ERROR

**NFR-OBS-003**: Трассировка (Tracing)
- Distributed tracing: Jaeger или Zipkin
- Trace ID передается через все микросервисы
- Корреляция логов и трейсов

**NFR-OBS-004**: Алертинг
- Критические алерты (PagerDuty / Telegram):
  - API error rate > 1%
  - Latency P99 > 3s
  - Database connection pool exhausted
- Предупреждающие алерты (Email / Slack):
  - Latency P95 > 1s
  - Disk usage > 80%
  - Queue depth > 500

**NFR-OBS-005**: Отслеживание ошибок
- Sentry для frontend и backend
- Source maps для JS (production)
- Automatic error grouping и deduplication

### 5.6. Локализация и интернационализация (NFR-L10N)

**NFR-L10N-001**: Языки (MVP)
- Русский язык (основной)
- Английский язык (для интерфейса, опционально)

**NFR-L10N-002**: Локализация контента
- Рецепты: приоритет на русскоязычные источники
- Ингредиенты: синонимы для разных регионов СНГ (Россия, Беларусь, Казахстан)
- Единицы измерения: метрическая система (граммы, литры)

**NFR-L10N-003**: Временные зоны
- Хранение всех timestamp в UTC
- Отображение в локальном времени пользователя

**NFR-L10N-004**: Валюты
- Основная валюта: RUB (российский рубль)
- Поддержка альтернативных валют (для будущих регионов): BYN, KZT, USD

### 5.7. Совместимость (NFR-COMP)

**NFR-COMP-001**: Поддержка браузеров (Web)
- Chrome: последние 2 версии
- Firefox: последние 2 версии
- Safari: последние 2 версии
- Edge: последние 2 версии
- Мобильные браузеры: iOS Safari 14+, Chrome Mobile 90+

**NFR-COMP-002**: Поддержка мобильных платформ (Native App)
- iOS: 14.0+
- Android: 8.0+ (API level 26+)

**NFR-COMP-003**: Адаптивность (Responsive Design)
- Breakpoints: 320px (mobile), 768px (tablet), 1024px (desktop), 1440px (wide)
- **MVP:** см. документ [[../requirements/FRS|FRS]], UI-UX-002 — приоритет **desktop-first** в веб; разметка тем не менее **responsive**. После выхода мобильного приоритета — усилить тестирование на mobile breakpoints

---

## 8. Требования к безопасности (дополнение к §5.4)

См. также канонические формулировки **NFR-SEC-*** выше.

**SEC-001**: Пентестинг
- Ежегодный внешний пентест после выхода на рынок
- Внутренний security audit каждые 6 месяцев

**SEC-002**: Уязвимости зависимостей
- Автоматическое сканирование npm/pip зависимостей (Snyk / Dependabot)
- Патчинг критичных уязвимостей в течение 7 дней

**SEC-003**: Secrets management
- Никаких secrets в коде или git репозитории
- Использование Kubernetes Secrets / AWS Secrets Manager
- Аудит доступа к секретам

## HumanOnly

- 

