# app/utils.py

import uuid
from datetime import datetime

def create_uuid() -> str:
    return str(uuid.uuid4())

def current_timestamp() -> str:
    return datetime.utcnow().isoformat() + "Z"

def format_chat_message(role: str, content: str) -> dict:
    return {
        "role": role,
        "content": content,
        "timestamp": current_timestamp()
    }
