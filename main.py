from fastapi import FastAPI
from plays import router

app = FastAPI()

app.include_router(router.router)


@app.get("/")
async def root():
    return {"message": "Welcome to Data Process API!"}
