from __future__ import annotations

from fastapi import FastAPI, Request

from tortoise.contrib.fastapi import register_tortoise
import constants
from fastapi.templating import Jinja2Templates

app = FastAPI()
template = Jinja2Templates(directory="src/templates")


@app.get("/")
async def root(request: Request):
    return template.TemplateResponse("index.html", {"request": request})


register_tortoise(
    app,
    config=constants.TORTOISE_CONF,
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
