from datetime import datetime

from fastapi import APIRouter
from fastapi import Request
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

from models.main import Script

router = APIRouter()
templates = Jinja2Templates(directory="web/template")


@router.get("/health")
def health_check():
    """
    Checks the health of a project.

    It returns 200 if the project is healthy.
    """

    return {"status": 200}


@router.get('/status/{name}')
async def status_pick(name: str):
    obj, created = await Script.get_or_create(name=name)
    obj: Script
    obj.last_connection = datetime.now()
    await obj.save(update_fields=['last_connection'])
    return {'id': obj.id, 'name': obj.name}


@router.get('/statuses', response_class=HTMLResponse)
async def statuses(request: Request):
    scripts = await Script.all()
    context = {
        "now": datetime.now().strftime('%H:%M:%S - %d.%m.%Y')
    }

    return templates.TemplateResponse("index1.html", {'items': scripts, 'request': request, **context})
