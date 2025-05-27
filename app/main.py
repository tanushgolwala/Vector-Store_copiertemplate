from fastapi import FastAPI
from app.api import router
from app.db import init_db

app = FastAPI()
init_db()
app.include_router(router)
