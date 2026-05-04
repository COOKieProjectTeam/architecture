#!/usr/bin/env python3
"""
Идемпотентный патч COOKie-v2.0.excalidraw: документационные Frames (gensum_*), обёртка genucd_* в gensum_frm_use_cases.
После запуска `summary/_gen_uc_diagrams.py` снова выполните этот скрипт, чтобы восстановить рамку и привязки.
Запуск: python summary/_expand_doc_frames.py из каталога проекта COOKie.
У элементов genucd_* правится только frameId при сборке заново.
"""

from __future__ import annotations

import json
import subprocess
import sys
import time
from pathlib import Path

EXCALIPATH = Path(__file__).resolve().parent / "COOKie-v2.0.excalidraw"
NOW = int(time.time() * 1000)
P_GS = "gensum_"

_idx = [8800]


def next_idx() -> str:
    _idx[0] += 1
    return f"zY{_idx[0]:04d}"


def frame_el(
    eid: str,
    idx: str,
    x: float,
    y: float,
    w: float,
    h: float,
    name: str,
    bg: str = "#fafafa",
) -> dict:
    return {
        "id": eid,
        "type": "frame",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": "#6b7280",
        "backgroundColor": bg,
        "fillStyle": "solid",
        "strokeWidth": 2,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": None,
        "seed": hash(eid) % (10**9),
        "version": 1,
        "versionNonce": (hash(eid) * 19) % (10**9),
        "isDeleted": False,
        "boundElements": [],
        "updated": NOW,
        "link": None,
        "locked": False,
        "name": name,
        "index": idx,
    }


def text_el(
    eid: str,
    idx: str,
    x: float,
    y: float,
    w: float,
    h: float,
    text: str,
    fz: float = 12.0,
    frame_id: str | None = None,
    bold_title: bool = False,
) -> dict:
    # bold_title unused — Excalidraw plain text; keep param for future
    _ = bold_title
    return {
        "id": eid,
        "type": "text",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": "#1e1e1e",
        "backgroundColor": "transparent",
        "fillStyle": "hachure",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": frame_id,
        "roundness": None,
        "seed": hash(eid + "t") % (10**9),
        "version": 1,
        "versionNonce": hash(eid + "tn") % (10**9),
        "isDeleted": False,
        "boundElements": [],
        "updated": NOW,
        "link": None,
        "locked": False,
        "text": text,
        "fontSize": fz,
        "fontFamily": 1,
        "textAlign": "left",
        "verticalAlign": "top",
        "containerId": None,
        "originalText": text,
        "autoResize": False,
        "lineHeight": 1.3,
        "index": idx,
    }


CONTENT = {
    # Ключевые строки без путей к файлам внутри текстов доски (план)
    "toc": """COOKie — навигация по документальным блокам (конспект с ID)


1) Продукт и стейкхолдеры — см. ниже
2) BRD · BC / MET — следующий блок
3) SRS (функционал, родительские FR) — крупный блок
4) NFR — сводка по категориям
5) Архитектура (стек + узлы) — ниже; цветная легенда слева на холсте (x≈240)
6) Use case — карточки и овалы генерируются скриптом genucd_ (обёртка Frame)
7) Процесс · MoSCoW · REQ+UML последний текстовый Frame

Подсказка: в Obsidian включите Frames / выделите рамку для фокуса экспорта.""",
    "product": """Что это: веб-сервис планирования питания = менеджер рецептов + связка с готовой едой и доставкой.


Миссия: проще персонализированное недельное планирование и закупки без ручной рутины.


Ценность B2C: план периода, профиль и аллергии, список покупок, КБЖУ и микронутриенты, сценарии «в один клик» через интеграции (Pro).


Ценность B2B: канал для готовых блюд и доставки, аналитика спроса с учётом политики данных партнёров.


Стейкхолдеры (роль → фокус):
• Anonymous — воронка и лимиты по политике роли
• Free User — база продукта, лимит избранного (см. FR-US-003)
• Pro User — цепочка КБЖУ → корзина/список → интеграции ритейлеров и доставки; ИИ вторичен
• Content Moderator — UGC и статусы рецептов
• Admin — полный доступ к платформе
• Partner Manager — каталог готовой еды и аналитика заказов


Глоссарий (топ): MVP; КБЖУ; B2C/B2B; UGC; LLM; Slug; JSONB; SLO/SLI; JSONB для нутриентов в PostgreSQL.""",
    "brd": """Объём: MVP ~4 месяца, регион СНГ, итерации MVP + Future roadmap.


BC-001: ~1000 пользователей к концу первых 4 месяцев; MVP в срок.
BC-002: один платный тариф Pro; конверсия Free→Pro 8–10% (целевой горизонт измерения согласован с продуктом).
BC-003: минимум 2 крупных ритейлера и 2 сервиса доставки к согласованному сроку (детали партнёров в SRS §7).


MET-PROD-001: North Star — WAU.
MET-PROD-002: воронка регистрации ~30%; Free→Pro 8–10%.
MET-PROD-003: engagement — просмотры рецептов/нед ≥10; ≥40% с ≥1 избранным; Retention D7 ~30%, D30 ~20%.


MET-TECH-001: SLI Availability 99.9%; P95 latency <500 ms; error rate <0.1%.
MET-TECH-002: CPU <70%, RAM <80%, Disk <75%.
MET-TECH-003: PostgreSQL P95 <100 ms; pool <80%; Redis hit rate >90%.""",
    "srs": """§2.2 Роли — см. блок «Продукт» (эта доска дублирует смысл, не заменяет канон текста).


§3 FR-RS (Recipe Service)
• FR-RS-001 CRITICAL — жизненный цикл рецептов, UGC, модерация, slug, версии
• FR-RS-002 CRITICAL — поиск, фильтры, сортировка, пагинация, RU-текст
• FR-RS-003 HIGH — карточка рецепта и табы
• FR-RS-004 MEDIUM — рейтинг 1–5
• FR-RS-005 HIGH — мастер-данные ингредиентов, дубли, пересчёт КБЖУ


§3 FR-PS (Parser)
• FR-PS-001 CRITICAL — парсинг сайтов в корпус
• FR-PS-002 LOW — видео-парсинг (Future, не MVP)


§3 FR-DE (Enrichment)
• FR-DE-001 CRITICAL — нормализация единиц
• FR-DE-002 CRITICAL — автоматический расчёт КБЖУ
• FR-DE-003 MEDIUM — авто-классификация


§3 FR-AN (Analytics)
• FR-AN-001 HIGH — события пользователей
• FR-AN-002 HIGH — продуктовые метрики и дашборды
• FR-AN-003 MEDIUM — отчёты и экспорт


§3 FR-US (User)
• FR-US-001 CRITICAL — регистрация, JWT, OAuth, восстановление доступа
• FR-US-002 HIGH — профиль и цели
• FR-US-003 MEDIUM — избранное с лимитами тарифа


§4 Future (цепочка Pro / интеграции)
• FR-AI-001 / FR-AI-002 — чат и рекомендации (Phase 2+)
• FR-MP-001 / FR-MP-002 — план питания и список покупок (Phase 2)
• FR-OR-001 — готовая еда и hand-off партнёру (Phase 2–3)


Интеграции, PSP, webhooks — детали в SRS §7 (на доске без перечня внешних URL).""",
    "nfr": """Сводка по категориям (полные пороги — канон NFR):

NFR-PF-001…005 — производительность: API P50/P95/P99; поиск P95 ≤300 ms; карточка P95 ≤2 s TTFB ≤500 ms; RPS MVP 100 → Year1 500 → Year2 2000; imgproxy/WebP для изображений.

NFR-SC-001…004 — масштабирование: горизонтальные сервисы, HPA правила в K8s, реплики PG/Redis/sharding ClickHouse, целевые объёмы рецептов/пользователей по годам.

NFR-AV-001…004 — доступность: MVP uptime 99.5%, затем 99.9%; отказоустойчивость, graceful degradation, health endpoints.

NFR-SEC-001…005 + SEC-* — JWT, RBAC, TLS, rate limit, аудит; пентест и зависимости.

NFR-OBS-001…005 — Prometheus, логирование ELK-style, трассировка, алерты, Sentry.

NFR-L10N / NFR-COMP — языки, часовые пояса, валюты; браузеры и responsive.""",
    "arch": """Контур (канон техстека совпадает с markdown): Next.js 14 App Router + TypeScript + React 18; TanStack Query + Zustand; styled-components; RHF+Zod; Axios; MSW в dev на /api/v1/* от swagger.


Backend: ASP.NET Core 8 модульный монолит; EF Core 8; FluentValidation; Identity + JWT + OAuth (Yandex ID, T‑ID); Serilog; StackExchange.Redis; AWS SDK S3 к объектному хранилищу.


Данные: PostgreSQL 15 (JSONB нутриенты, GIN RU-поиск), Redis 7 кэш и rate-limit, объектное хранилище для медиа; health live/ready.


Клиентская структура: app/, features/, entities/, shared/api|ui|lib; web-vitals → POST /api/v1/metrics.


Программная и системная проекция UML в vault пока каркас — на доске фиксируем только стек и узлы выше.


Доменная модель (информационный уровень): слот под концептуальную UML; сущности из реализации стека: User, Recipe, Ingredient, Favorite, Rating, Session, ErrorLog, MetricEvent, value objects Nutrition/DietaryTags/Allergens.""",
    "process": """Методология: спринты 2 недели; freeze объёма на старте спринта; приоритеты — MoSCoW поверх меток CRITICAL/HIGH/MEDIUM/LOW; операционный бэклог ведётся в GitHub Issues/Projects (организация команды), не дублируется здесь.


MoSCoW (MVP): CRITICAL→Must; HIGH→Should; MEDIUM→Could; LOW/Future→Won’t сейчас.


MVP Must: FR-RS-001/002, FR-PS-001, FR-DE-001/002, FR-US-001; Should/HIGH: FR-AN-001/002, FR-RS-003/005, FR-US-002; прочие — см. prioritization.


REQ+UML: этапы §1–§5 закрыты на дате согласования пакета; §3–§4 — анализ и документирование (свойства требований, зрелость пирамиды BRD/SRS/FRS/NFR); §6–§7 — трассировка к задачам и спринтам ведётся в GitHub, не на этой доске.


Открытые вопросы §3 (сжато): OQ-001 конкурентный анализ TBD; OQ-002 согласовать лимиты FR-AI для Free vs Pro; OQ-003 минимальный набор админских сценариев MVP.


Жизненный цикл (процесс): спецификация и архитектура до первого dev-спринта; реализация — задачи в GitHub; существенные отклонения от утверждённой спеки — через Change Request когда процесс включён; UI-каркас в FRS — по мере необходимости.""",
}


def build_section(frame_id: str, title_text_id: str, title: str, body_key: str, x: float, y: float, w: float, h_frame: float) -> tuple[list[dict], dict]:
    """Returns (children, frame) frame must come after children."""
    padding = 16.0
    title_h = 28.0
    fh = frame_el(
        frame_id,
        next_idx(),
        x,
        y,
        w,
        h_frame,
        title.replace("\n", " ")[:120],
        "#fafafa",
    )
    tt = text_el(
        title_text_id,
        next_idx(),
        x + padding,
        y + padding - 4,
        w - padding * 2,
        title_h,
        title,
        fz=17,
        frame_id=frame_id,
    )
    body_id = P_GS + body_key + "_body"
    body = text_el(
        body_id,
        next_idx(),
        x + padding,
        y + padding + title_h,
        w - padding * 2,
        h_frame - padding * 2 - title_h - 8,
        CONTENT[body_key],
        fz=12,
        frame_id=frame_id,
    )
    return [tt, body], fh


LEGACY_DOC_FRAME_IDS = frozenset(
    {"frame_toc", "frame_prod", "frame_brd", "frame_srs", "frame_nfr", "frame_arch", "frame_proc"}
)


def patch_frame_roundness_null(data: dict) -> None:
    """Как FRAME_STYLE во Excalidraw: у frame roundness = null."""
    for e in data.get("elements") or []:
        if isinstance(e, dict) and e.get("type") == "frame":
            e["roundness"] = None


def main() -> None:
    data = json.loads(EXCALIPATH.read_text(encoding="utf-8"))
    cleaned: list[dict] = []
    for e in data["elements"]:
        eid = str(e.get("id", ""))
        if eid.startswith(P_GS) or eid in LEGACY_DOC_FRAME_IDS:
            continue
        if eid.startswith("genucd_"):
            e["frameId"] = None
        cleaned.append(e)
    elements = cleaned
    FID_UC = P_GS + "frm_use_cases"

    non_uc: list[dict] = []
    uc: list[dict] = []
    for e in elements:
        if e.get("id", "").startswith("genucd_"):
            e["frameId"] = FID_UC
            uc.append(e)
        else:
            non_uc.append(e)

    if not uc:
        raise SystemExit("No genucd_ elements found — abort.")

    min_x = min(el["x"] for el in uc)
    min_y = min(el["y"] for el in uc)
    max_x = max(el["x"] + el.get("width", 0) for el in uc)
    max_y = max(el["y"] + el.get("height", 0) for el in uc)
    pad = 28.0
    frame_uc = frame_el(
        FID_UC,
        next_idx(),
        min_x - pad,
        min_y - pad,
        max_x - min_x + pad * 2,
        max_y - min_y + pad * 2,
        "Use case (genucd_ зона генератора)",
        "#fffbeb",
    )

    DOC_X = 920.0
    DOC_W = 780.0
    y_cursor = -800.0
    gap = 36.0

    sections_layout = [
        (P_GS + "frm_toc", P_GS + "toc_title", "Оглавление конспекта", "toc", 160),
        (P_GS + "frm_product", P_GS + "prod_title", "Продукт и стейкхолдеры", "product", 420),
        (P_GS + "frm_brd", P_GS + "brd_title", "BRD · бизнес-цели и метрики", "brd", 380),
        (P_GS + "frm_srs", P_GS + "srs_title", "SRS · функциональные требования (родительские FR)", "srs", 960),
        (P_GS + "frm_nfr", P_GS + "nfr_title", "NFR · сводная матрица (кратко)", "nfr", 480),
        (P_GS + "frm_arch", P_GS + "arch_title", "Архитектура · стек и узлы", "arch", 520),
        (P_GS + "frm_proc", P_GS + "proc_title", "Процесс · MoSCoW · REQ+UML", "process", 500),
    ]

    new_blocks: list[dict] = []
    for fid, tid, title, ckey, h in sections_layout:
        children, frm = build_section(fid, tid, title, ckey, DOC_X, y_cursor, DOC_W, float(h))
        new_blocks.extend(children)
        new_blocks.append(frm)
        y_cursor += h + gap

    # Cross-reference note near existing legend (non-frame text) — small label at DOC_X referencing left legend
    ref_id = P_GS + "pointer_legend"
    new_blocks.insert(
        0,
        text_el(
            ref_id,
            next_idx(),
            DOC_X,
            -840.0,
            DOC_W,
            32,
            "Документальный столбец (gensum_*): добавлен скриптом _expand_doc_frames.py\nЛегенда слоёв и цветные блоки архитектуры — слева (x≈240).",
            fz=11,
            frame_id=None,
        ),
    )

    data["elements"] = non_uc + uc + [frame_uc] + new_blocks

    patch_frame_roundness_null(data)

    EXCALIPATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Patched", EXCALIPATH, "genucd count", len(uc), "new elements", len(new_blocks) + 1)

    wd = Path(__file__).resolve().parent
    try:
        subprocess.run(
            [sys.executable, str(wd / "_export_excalidraw_web_flat.py")],
            cwd=str(wd.parent),
            check=False,
            timeout=120,
        )
    except (OSError, subprocess.TimeoutExpired):
        pass


if __name__ == "__main__":
    main()
