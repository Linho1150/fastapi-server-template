from typing import Union

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.sample.controller import sample_controller

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(sample_controller.router)
