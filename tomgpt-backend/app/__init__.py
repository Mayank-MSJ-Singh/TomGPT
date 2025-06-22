# app/__init__.py

# Make this directory a Python package
# Also preload env vars for the whole app

from dotenv import load_dotenv
load_dotenv()

# Optional: re-export things if needed elsewhere
# app/__init__.py

from .auth import verify_google_token
from .chat import chat_with_openai
from .db import save_chat, load_chat
from .utils import create_uuid, current_timestamp, format_chat_message

__all__ = [
    # Auth
    "verify_google_token",

    # Chat
    "chat_with_openai",

    # DB
    "save_chat",
    "load_chat",

    # Utils
    "create_uuid",
    "current_timestamp",
    "format_chat_message",
]
