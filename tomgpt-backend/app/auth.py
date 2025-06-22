# app/auth.py

from google.oauth2 import id_token
from google.auth.transport import requests
from fastapi import HTTPException
import os

def verify_google_token(token: str) -> str:
    try:
        if token.startswith("Bearer "):
            token = token.split(" ", 1)[1]

        idinfo = id_token.verify_oauth2_token(
            token,
            requests.Request(),
            os.getenv("GOOGLE_CLIENT_ID")  # Optional: add your client ID to verify audience
        )

        user_id = idinfo.get("sub")
        if not user_id:
            raise ValueError("Missing user ID in token")

        return user_id


    except Exception as e:
        print("❌ Token verification failed:", str(e))
        raise HTTPException(status_code=401, detail=f"Invalid token: {str(e)}")
