from fastapi import APIRouter

from backend.schemas import ChatRequest,ChatResponse

from backend.service import get_answer


router = APIRouter()

@router.get("/")

def get_status():
    
    return {
        "status" : "healthy"
    }

@router.post("/chat" , response_model = ChatResponse)

def get_info(request : ChatRequest):
    
    answer = get_answer(request.question)

    return ChatResponse(answer = answer)