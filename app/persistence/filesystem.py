# src/baseline_service/persistence/filesystem.py

import os
import json
from typing import Any, Dict, List


def list_files(path: str) -> List[str]:
    """
    List all non‐hidden files in a directory.
    """
    try:
        return [f for f in os.listdir(path) if not f.startswith(".")]
    except FileNotFoundError:
        return []


def read_json(path: str) -> Dict[str, Any]:
    """
    Read a JSON file and return its contents as a dict.
    """
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: str, data: Dict[str, Any]) -> None:
    """
    Write a dict to a JSON file.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def read_text(path: str) -> str:
    """
    Read a text (e.g. Markdown) file and return its full contents.
    """
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(path: str, content: str) -> None:
    """
    Write a string to a text (e.g. Markdown) file.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
