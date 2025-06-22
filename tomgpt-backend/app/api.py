# app/api.py
from fastapi import APIRouter, Request, HTTPException
from pydantic import BaseModel

from app.auth import verify_google_token
from app.chat import chat_with_openai
from app.db import save_chat, load_chat
from app.utils import create_uuid, format_chat_message

router = APIRouter()

class NewChatInput(BaseModel):
    message: str

class MessageInput(BaseModel):
    message: str

@router.post("/chat")
async def start_new_chat(req: Request, input: NewChatInput):
    token = req.headers.get("Authorization")
    user_id = verify_google_token(token)

    chat_id = create_uuid()
    history = [format_chat_message("user", input.message)]
    reply = await chat_with_openai(history)
    history.append(format_chat_message("assistant", reply))

    save_chat(user_id, chat_id, history)
    return {"chat_id": chat_id, "reply": reply}

@router.post("/chat/{chat_id}")
async def continue_chat(chat_id: str, req: Request, input: MessageInput):
    token = req.headers.get("Authorization")
    user_id = verify_google_token(token)

    history = load_chat(user_id, chat_id)
    if not history:
        raise HTTPException(status_code=404, detail="Chat not found")

    history.append(format_chat_message("user", input.message))
    reply = await chat_with_openai(history)
    history.append(format_chat_message("assistant", reply))

    save_chat(user_id, chat_id, history)
    return {"reply": reply}

@router.get("/chat/{chat_id}")
async def get_chat(chat_id: str, req: Request):
    token = req.headers.get("Authorization")
    user_id = verify_google_token(token)

    history = load_chat(user_id, chat_id)
    if not history:
        raise HTTPException(status_code=404, detail="Chat not found")

    return {"messages": history}
