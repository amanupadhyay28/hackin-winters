from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter()
template = Jinja2Templates(directory="src/templates")


@router.get("/reminder")
async def reminder(request: Request):
    return template.TemplateResponse("reminder.html", {"request": request})


@router.post("/reminder/create")
async def reminder(request: Request):
    ...


@router.get("/reminder/user")
async def reminder(request: Request, phone: int):
    ...
