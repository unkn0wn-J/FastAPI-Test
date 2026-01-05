# fastapi_4/app/__init__.py
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


register_tortoise(
    app,
    db_url="mysql://root:1234@localhost:3307/when2meet",
    modules={"models": ["app.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
