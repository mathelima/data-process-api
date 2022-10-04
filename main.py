from logging.config import dictConfig
from fastapi import FastAPI
from plays import router
from logger import log_config
import logging

dictConfig(log_config)
app = FastAPI()

app.include_router(router.router)

logger = logging.getLogger("data-process-api")


@app.get("/")
async def root():
    return {"message": "Welcome to Data Process API!"}
