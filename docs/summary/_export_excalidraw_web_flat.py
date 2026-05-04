#!/usr/bin/env python3
"""
Копия сцены без элементов type:frame и без frameId
(вариант «площе» основной доски для веб-импорта; см. README).

Читает COOKie-v2.0.excalidraw, пишет COOKie-v2.0.web.excalidraw рядом.

Запуск: python summary/_export_excalidraw_web_flat.py из каталога проекта COOKie.
"""

from __future__ import annotations

import copy
import json
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "COOKie-v2.0.excalidraw"
TARGET = Path(__file__).resolve().parent / "COOKie-v2.0.web.excalidraw"


def main() -> None:
    src = SOURCE if len(sys.argv) < 2 else Path(sys.argv[1])
    dst = TARGET if len(sys.argv) < 3 else Path(sys.argv[2])
    data = json.loads(src.read_text(encoding="utf-8"))
    n_in = len(data.get("elements") or [])
    frames_removed = 0
    flat: list[dict] = []
    for raw in data.get("elements") or []:
        if not isinstance(raw, dict):
            continue
        if raw.get("type") == "frame":
            frames_removed += 1
            continue
        el = copy.deepcopy(raw)
        el["frameId"] = None
        flat.append(el)
    data = copy.deepcopy(data)
    data["elements"] = flat
    dst.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Wrote", dst, "elements", len(flat), "(removed", frames_removed, "frames)")


if __name__ == "__main__":
    main()
