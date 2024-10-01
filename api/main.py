from fastapi import FastAPI
from api.routes import pdf

app = FastAPI()

app.include_router(pdf)











# uvicorn api.main:app --reload