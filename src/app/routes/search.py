from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates


router = APIRouter(prefix="/search")
template = Jinja2Templates(directory="src/templates")


@router.get("/")
async def search_page(request: Request, name: str = None):
    if not name:
        return "without name"

    return "With name"
