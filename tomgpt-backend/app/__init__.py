# app/__init__.py

# Make this directory a Python package
# Also preload env vars for the whole app

from dotenv import load_dotenv
load_dotenv()

# Optional: re-export things if needed elsewhere
from .auth import verify_google_token
from .chat import chat_with_openai
from .db import save_chat, load_chat
from .utils import create_uuid, format_chat_message
