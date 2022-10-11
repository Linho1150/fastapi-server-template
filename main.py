from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from datetime import datetime
from app.sample.controller import sample_controller

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(sample_controller.router)


@app.get("/health-check", tags=["Health-check"], summary="Response DateTime for Health-Check")
async def health_check():
    return {"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
