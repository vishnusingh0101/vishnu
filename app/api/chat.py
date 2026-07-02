from fastapi import APIRouter
from pydantic import BaseModel
from app.services.ollama_service import chat

router = APIRouter()

class ChatRequest(BaseModel):
    message: str

@router.post("/chat")
def ask_ai(req: ChatRequest):
    return {"response": chat(req.message)}
