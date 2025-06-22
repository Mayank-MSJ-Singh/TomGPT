from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from mangum import Mangum

from api import router   # ← This brings in all your API endpoints

app = FastAPI()

# 🔐 Enable CORS so frontend can call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # later restrict this to your frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔗 Attach the API routes
app.include_router(router)

# 🔁 For AWS Lambda
handler = Mangum(app)
