# utils.py

import datetime

def format_message(role: str, content: str) -> dict:
    return {
        "role": role,
        "text": content,
        "timestamp": datetime.datetime.utcnow().isoformat() + "Z"
    }
