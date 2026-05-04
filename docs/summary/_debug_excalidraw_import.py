#!/usr/bin/env python3
"""
Локальные проверки JSON сцены (контур как isValidExcalidrawData в upstream Excalidraw).
Не гарантирует успех импорта в браузере; вывод в stdout и код выхода 0/1/2.

Запуск: python summary/_debug_excalidraw_import.py [пути…]
"""

from __future__ import annotations

import json
import sys
from pathlib import Path


def is_valid_excalidraw_data_top(data: object) -> bool:
    if not isinstance(data, dict):
        return False
    elems = data.get("elements")
    app = data.get("appState")
    return data.get("type") == "excalidraw" and (
        not elems or (isinstance(elems, list) and (app is None or isinstance(app, dict)))
    )


ALLOWED_TYPES = frozenset(
    (
        "rectangle",
        "diamond",
        "ellipse",
        "arrow",
        "line",
        "freedraw",
        "text",
        "image",
        "frame",
        "magicframe",
        "iframe",
        "embeddable",
        "laser",
        "selection",
    )
)


def validate(path: Path) -> int:
    fname = path.name
    raw = path.read_bytes()
    text = raw.decode("utf-8")
    issues = 0
    try:
        data = json.loads(text)
    except json.JSONDecodeError as e:
        print(f"[{fname}] JSON error: {e}")
        return 1

    valid_top = is_valid_excalidraw_data_top(data)
    print(f"[{fname}] top-level-like-valid: {valid_top}")

    elements = data.get("elements") or []
    print(f"[{fname}] elements: {len(elements)}")

    id_set: dict[str, int] = {}
    types: dict[str, int] = {}
    for el in elements:
        if isinstance(el, dict):
            eid = el.get("id") or ""
            id_set[eid] = id_set.get(eid, 0) + 1
            t = el.get("type") or "?"
            types[t] = types.get(t, 0) + 1

    dups = {k: v for k, v in id_set.items() if k and v > 1}
    unknown = [(t, types[t]) for t in sorted(types) if t not in ALLOWED_TYPES]

    print(f"[{fname}] duplicate ids: {len(dups)}", list(dups.items())[:3] if dups else [])
    print(f"[{fname}] unknown element types:", unknown[:10])

    id_positions: dict[str, int] = {}
    frames: dict[str, int] = {}
    for idx, el in enumerate(elements):
        if not isinstance(el, dict):
            continue
        i = el.get("id")
        if isinstance(i, str):
            id_positions[i] = idx
            if el.get("type") == "frame":
                frames[i] = idx

    child_after = 0
    bad_ref = 0
    for idx, el in enumerate(elements):
        if not isinstance(el, dict):
            continue
        fid = el.get("frameId")
        if not fid:
            continue
        if fid not in id_positions:
            bad_ref += 1
            continue
        fpos = frames.get(fid)
        if fpos is None:
            bad_ref += 1
            continue
        if idx > fpos:
            child_after += 1

    print(
        f"[{fname}] frames: {len(frames)}, child-after-frame: {child_after}, bad frameId: {bad_ref}",
    )

    if not valid_top:
        issues += 1
    if dups:
        issues += 1
    if unknown:
        issues += 1
    if child_after or bad_ref:
        issues += 1

    return 0 if issues == 0 else 2


def main() -> None:
    targets = [Path(__file__).resolve().parent / "COOKie-v2.0.excalidraw"]
    if len(sys.argv) > 1:
        targets = [Path(a) for a in sys.argv[1:]]
    rc_all = 0
    for p in targets:
        rc = validate(p)
        rc_all = max(rc_all, rc)
        print(p.name, "exit", rc)
    sys.exit(rc_all)


if __name__ == "__main__":
    main()
