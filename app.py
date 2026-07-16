from fastapi import FastAPI

from backend.service import get_answer

from backend.routes import router

app = FastAPI()

app.include_router(router)

