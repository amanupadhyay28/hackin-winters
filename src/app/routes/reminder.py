from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter()


@router.get("/reminder")
async def reminder(request: Request):
    return "Reminder"


@router.get("/reminder/create")
async def reminder(request: Request):
    ...


@router.get("/reminder/user")
async def reminder(request: Request, phone: int):
    ...
