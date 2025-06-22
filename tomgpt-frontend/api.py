# api.py

import requests
import os

API_BASE = os.getenv("API_BASE_URL", "http://localhost:8000")

def headers(token):
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

def start_chat(token, message):
    res = requests.post(f"{API_BASE}/chat", headers=headers(token), json={"message": message})
    res.raise_for_status()
    return res.json()

def continue_chat(token, chat_id, message):
    res = requests.post(f"{API_BASE}/chat/{chat_id}", headers=headers(token), json={"message": message})
    res.raise_for_status()
    return res.json()

def get_chat(token, chat_id):
    res = requests.get(f"{API_BASE}/chat/{chat_id}", headers=headers(token))
    res.raise_for_status()
    return res.json()
