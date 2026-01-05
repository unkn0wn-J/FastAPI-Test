from app.configs.tortoise_config import initialize_tortoise
from fastapi import FastAPI

app = FastAPI()

initialize_tortoise(app)
