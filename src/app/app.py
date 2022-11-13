from __future__ import annotations

from fastapi import FastAPI

from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()


@app.get("/")
async def root():
    return {"ping": "pong"}


# register_tortoise(
#     app,
#     db_url="sqlite://:memory:",
#     modules={"models": ["models"]},
# )
