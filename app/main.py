from fastapi import FastAPI
from app.api.chat import router

app = FastAPI(
    title="VISHNU",
    description="Offline Personal AI Assistant",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def health():
    return {"assistant":"VISHNU","status":"running"}
