# app/db.py

import os
import json
from pathlib import Path

BASE_DIR = Path("user_data")
BASE_DIR.mkdir(exist_ok=True)

def _get_user_chat_path(user_id: str, chat_id: str) -> Path:
    user_dir = BASE_DIR / user_id
    user_dir.mkdir(exist_ok=True)
    return user_dir / f"{chat_id}.json"

def save_chat(user_id: str, chat_id: str, history: list[dict]):
    path = _get_user_chat_path(user_id, chat_id)
    with open(path, "w") as f:
        json.dump(history, f, indent=2)

def load_chat(user_id: str, chat_id: str) -> list[dict] | None:
    path = _get_user_chat_path(user_id, chat_id)
    if not path.exists():
        return None
    with open(path) as f:
        return json.load(f)
