#!/usr/bin/env python3
"""
Idempotent patch: COOKie Use Case блок в Excalidraw JSON.
Элементы id начинаются с genucd_ — при перезапуске удаляются и создаются заново.
"""

from __future__ import annotations

import json
from pathlib import Path

EXCALIPATH = Path(__file__).resolve().parent / "COOKie-v2.0.excalidraw"
P = "genucd_"

_idx = [0]


def I() -> str:
    _idx[0] += 1
    return f"zz{_idx[0]:04d}"


def txt(
    idx: str,
    eid: str,
    x: float,
    y: float,
    w: float,
    h: float,
    text: str,
    fz: float = 12.0,
    align: str = "left",
    valign: str = "top",
) -> dict:
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
        "frameId": None,
        "roundness": None,
        "seed": hash(eid) % (10**9),
        "version": 1,
        "versionNonce": (hash(eid) * 17) % (10**9),
        "isDeleted": False,
        "boundElements": [],
        "updated": 1777240000000,
        "link": None,
        "locked": False,
        "text": text,
        "fontSize": fz,
        "fontFamily": 1,
        "textAlign": align,
        "verticalAlign": valign,
        "containerId": None,
        "originalText": text,
        "autoResize": False,
        "lineHeight": 1.2,
        "index": idx,
    }


def rect(idx: str, eid: str, x: float, y: float, w: float, h: float, bg: str, stroke: str, sw: float = 2.0) -> dict:
    return {
        "id": eid,
        "type": "rectangle",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": stroke,
        "backgroundColor": bg,
        "fillStyle": "solid",
        "strokeWidth": sw,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 3},
        "seed": hash(eid + "r") % (10**9),
        "version": 1,
        "versionNonce": hash(eid + "rn") % (10**9),
        "isDeleted": False,
        "boundElements": [],
        "updated": 1777240000000,
        "link": None,
        "locked": False,
        "index": idx,
    }


def ellipse(idx: str, eid: str, x: float, y: float, w: float, h: float, bg: str, stroke: str) -> dict:
    """UML use case oval."""
    return {
        "id": eid,
        "type": "ellipse",
        "x": x,
        "y": y,
        "width": w,
        "height": h,
        "angle": 0,
        "strokeColor": stroke,
        "backgroundColor": bg,
        "fillStyle": "solid",
        "strokeWidth": 1.5,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": None,
        "seed": hash(eid + "e") % (10**9),
        "version": 1,
        "versionNonce": hash(eid + "en") % (10**9),
        "isDeleted": False,
        "boundElements": [],
        "updated": 1777240000000,
        "link": None,
        "locked": False,
        "index": idx,
    }


def arrow_line(idx: str, eid: str, sx: float, sy: float, dx: float, dy: float) -> dict:
    return {
        "id": eid,
        "type": "arrow",
        "x": sx,
        "y": sy,
        "width": dx,
        "height": dy,
        "angle": 0,
        "strokeColor": "#495057",
        "backgroundColor": "transparent",
        "fillStyle": "hachure",
        "strokeWidth": 1,
        "strokeStyle": "solid",
        "roughness": 1,
        "opacity": 100,
        "groupIds": [],
        "frameId": None,
        "roundness": {"type": 2},
        "seed": hash(eid) % (10**9),
        "version": 1,
        "versionNonce": hash(eid + "n") % (10**9),
        "isDeleted": False,
        "boundElements": [],
        "updated": 1777240000000,
        "link": None,
        "locked": False,
        "points": [[0, 0], [dx, dy]],
        "lastCommittedPoint": None,
        "startBinding": None,
        "endBinding": None,
        "startArrowhead": None,
        "endArrowhead": "arrow",
        "index": idx,
        "moveMidPointsWithElement": False,
    }


UC_ROWS: list[tuple[str, str]] = [
    ("UC-BrowseRecipes", "поиск, фильтры · FR-RS-002"),
    ("UC-ViewRecipe", "карточка рецепта · FR-RS-003"),
    ("UC-Authenticate", "регистрация и вход · FR-US-001"),
    ("UC-ManageUserProfile", "профиль и цели · FR-US-002"),
    ("UC-ManageFavorites", "избранное · FR-US-003"),
    ("UC-RateRecipe", "оценка 1–5 · FR-RS-004"),
    ("UC-GenerateMealPlan", "план питания · FR-MP-001"),
    ("UC-BuildShoppingList", "агрегация покупок · FR-MP-002"),
    ("UC-PartnerHandOff", "hand-off партнёру · FR-MP/FR-OR"),
    ("UC-BrowseOrderReadyMeals", "готовые блюда · FR-OR-001"),
    ("UC-ChatNutritionAI", "чат ИИ · FR-AI-*"),
    ("UC-IngestRecipes", "парсинг корпуса · FR-PS-*"),
    ("UC-ModerateRecipes", "статусы UGC · FR-RS-001"),
    ("UC-PartnerAnalytics", "B2B аналитика · FR-OR-001"),
    ("UC-AdministerPlatform", "операции Admin · SRS §2.2"),
    ("UC-ManageProSubscription", "оплата Pro · INT-API-002"),
    ("UC-ManagePersonalData", "GDPR: согласие/экспорт/удаление"),
    ("UC-RestoreAccountAccess", "email + reset · FR-US-001"),
    ("UC-OperateProductReporting", "дашборды и отчёты · FR-AN"),
    ("UC-ManageIngredientMasterData", "справочник · FR-RS-005"),
]


def uc_pair(idx_prefix: str, base_id: str, x: float, y: float, w: float, h: float, title: str, sub: str) -> list[dict]:
    ee = ellipse(f"{idx_prefix}a", base_id + "_e", x, y, w, h, "#fffbeb", "#854d0e")
    body = title if not (sub or "").strip() else f"{title}\n{sub}"
    fz = 9.5 if "\n" in body else 11.0
    tt = txt(
        f"{idx_prefix}b",
        base_id + "_t",
        x + 8,
        y + 8,
        w - 16,
        h - 16,
        body,
        fz=fz,
        align="center",
        valign="middle",
    )
    tt["autoResize"] = False
    return [ee, tt]


def detail_card(
    col: int,
    dy: float,
    bx: float,
    title: str,
    actor: str,
    usecases: list[str],
    secondary: str,
    refs: str,
) -> list[dict]:
    """Актёр слева | связь → | граница системы с вертикальным стеком UC-овалов."""
    CARD_W = 386.0
    GAP = 22.0
    x0 = bx + col * (CARD_W + GAP)

    oy = dy
    h_sys = 252.0
    w_actor = 96.0
    x_sys = x0 + w_actor + 36.0
    w_sys = 252.0
    actor_top = oy + 40.0
    actor_h = h_sys

    pills = len(usecases)
    pill_h, pill_gap = 48.0, 10.0
    stack = pills * pill_h + max(0, pills - 1) * pill_gap
    pills_y0 = actor_top + 36.0 + (h_sys - 36.0 - stack) / 2

    els: list[dict] = []
    els.append(txt(I(), P + f"cd{col}_title", x0, oy - 26, CARD_W + 10, 24, title, fz=12.5))

    els.append(rect(I(), P + f"cd{col}_act_bg", x0, actor_top, w_actor - 8, actor_h - 44, "#f1f5f9", "#94a3b8", 1))
    els.append(
        txt(
            I(),
            P + f"cd{col}_act",
            x0 + 2,
            actor_top + 12,
            w_actor - 12,
            actor_h - 68,
            actor,
            fz=11,
            align="center",
            valign="middle",
        )
    )

    mid_y = actor_top + actor_h / 2 - 8.0
    ax_end = x0 + w_actor - 4
    els.append(
        arrow_line(I(), P + f"cd{col}_a1", ax_end, mid_y - 22, max(28.0, x_sys - ax_end + 22), -2),
    )

    els.append(rect(I(), P + f"cd{col}_sys", x_sys, actor_top + 36, w_sys, h_sys, "#fefce8", "#ca8a04", 2))
    els.append(
        txt(I(), P + f"cd{col}_sysh", x_sys + 6, actor_top + 44, w_sys - 12, 16, "<<system>> COOKie", fz=10.5, align="center"),
    )

    for i, pn in enumerate(usecases):
        py = pills_y0 + i * (pill_h + pill_gap)
        els.extend(uc_pair(I(), P + f"cd{col}_p{i}", x_sys + 14, py, w_sys - 28, pill_h, pn, ""))

    sx = secondary.strip()
    if sx:
        sec_y = actor_top + 36 + h_sys + 8
        els.append(
            txt(
                I(),
                P + f"cd{col}_sec",
                x_sys,
                sec_y,
                w_sys,
                26,
                f"«secondary actor» {sx}",
                fz=10,
                align="center",
            ),
        )
        foot_y = sec_y + 30
    else:
        foot_y = actor_top + 36 + h_sys + 10

    els.append(txt(I(), P + f"cd{col}_ref", x0, foot_y, CARD_W - 8, 36, refs, fz=9.5))
    return els


def build() -> list[dict]:
    _idx[0] = 0
    out: list[dict] = []
    bx, by = -1520.0, 3310.0

    out.append(
        txt(
            I(),
            P + "title",
            bx,
            by,
            1380,
            28,
            "Use Case diagrams (COOKie) — визуальный конспект текстовых UC и ссылок на FR",
            fz=20,
        )
    )
    out.append(
        txt(
            I(),
            P + "sub",
            bx,
            by + 30,
            1320,
            36,
            "Overview: 20 UC в одной системной границе (овал + краткая суть). Ниже D1–D5 — те же блоки расшифровки, что §1 доп. диаграммы в заметке.",
            fz=12,
        ),
    )

    # --- Обзор: размер сетки от контента ---
    COLS = 5
    ROWS = 4
    CELL_W = 232.0
    CELL_H = 102.0
    G_CELL = 10.0
    PAD_TOP = 48.0  # заголовок system
    PAD_BOT = 20.0
    SIDE_L = 130.0
    SIDE_R = 112.0
    INNER_W = COLS * CELL_W + (COLS - 1) * G_CELL
    INNER_H = PAD_TOP + ROWS * CELL_H + (ROWS - 1) * G_CELL + PAD_BOT

    sys_x = bx + SIDE_L + 54
    sys_y = by + 86
    sys_w = INNER_W + 56
    sys_h = INNER_H + 36

    out.append(txt(I(), P + "ov_lbl", bx, sys_y - 22, 320, 20, "Overview — карта всех UC", fz=13.5))

    out.append(
        txt(
            I(),
            P + "actors_l",
            bx + 14,
            sys_y + PAD_TOP + 80,
            SIDE_L - 24,
            220,
            "Акторы (роли SRS §2.2):\nAnonymous, Free,\nPro, Moderator,\nAdmin,\nPartner Mgr.",
            fz=11,
        )
    )
    out.append(
        txt(
            I(),
            P + "actors_r",
            sys_x + sys_w + 10,
            sys_y + PAD_TOP + 100,
            SIDE_R + 36,
            200,
            "Внешние интеграции:\nRetail · Delivery ·\nLLM · Pay ·\nWWW (источники)",
            fz=10,
        )
    )

    mid_in = sys_y + PAD_TOP + INNER_H / 2
    out.append(arrow_line(I(), P + "alv", sys_x - 52, mid_in, 40, -2))
    out.append(arrow_line(I(), P + "arv", sys_x + sys_w + 14, mid_in - 36, -40, -2))

    out.append(rect(I(), P + "system", sys_x, sys_y, sys_w, sys_h, "#ffffff", "#64748b", 2))
    out.append(txt(I(), P + "system_h", sys_x + 8, sys_y + 10, sys_w - 16, 26, "<<system>> COOKie", fz=14, align="center"))

    gx0 = sys_x + (sys_w - INNER_W) / 2
    gy0 = sys_y + PAD_TOP + 14

    for i, (title, sub) in enumerate(UC_ROWS[:20]):
        c, r = i % COLS, i // COLS
        if r >= ROWS:
            break
        cx = gx0 + c * (CELL_W + G_CELL)
        cy = gy0 + r * (CELL_H + G_CELL)
        out.extend(uc_pair(I(), P + f"ov{i}", cx, cy, CELL_W, CELL_H, title, sub))

    # --- Detail row D1–D5 -------------------------------------------------
    dy = sys_y + sys_h + 48
    out.extend(detail_card(0, dy, bx, "D1 — ManageProSubscription", "Free /\nPro User", ["Subscribe Pro", "Manage subscription"], "Payment (ЮKassa)", "SRS: FR-US*, INT-API-002"))

    out.extend(detail_card(1, dy, bx, "D2 — ManagePersonalData", "User\n(Free / Pro)", ["Consent", "Export my data", "Delete account"], "Email (SMTP)", "SRS: DR-GDPR"))

    out.extend(detail_card(2, dy, bx, "D3 — RestoreAccountAccess", "User", ["Verify email", "Reset password"], "Email (SMTP)", "«include» UC-Authenticate"))

    out.extend(detail_card(3, dy, bx, "D4 — OperateProductReporting", "Admin", ["Open dashboards", "Schedule report", "Export CSV"], "Analytics store", "FR-AN-002, FR-AN-003"))

    out.extend(
        detail_card(
            4,
            dy,
            bx,
            "D5 — ManageIngredientMasterData",
            "Admin",
            ["CRUD ingredient", "Merge synonyms"],
            "Recipe DB linkage",
            "FR-RS-005; затем пересчёт КБЖУ FR-DE-002 (batch)",
        )
    )

    return out


def main() -> None:
    data = json.loads(EXCALIPATH.read_text(encoding="utf-8"))
    data["elements"] = [e for e in data["elements"] if not str(e.get("id", "")).startswith(P)]
    data["elements"].extend(build())
    out_path = EXCALIPATH.as_posix()
    EXCALIPATH.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    n = sum(1 for e in data["elements"] if str(e.get("id")).startswith(P))
    print(f"Wrote {n} generated elements ({out_path})")


if __name__ == "__main__":
    main()
