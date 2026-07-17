from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from backend.service import get_answer

from backend.routes import router

app = FastAPI()

origins = [
    "http://localhost:5550",
    "http://127.0.0.1:5500"
]

app.add_middleware(CORSMiddleware,
                allow_origins=origins,
                allow_credentials=True,
                allow_headers=["*"],
                allow_methods=["*"]
                )

app.include_router(router)

