from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from app.setup.service import appconfig_service

templates = Jinja2Templates(directory="templates")

router = APIRouter(prefix="/appconfig")


@router.get("/", status_code=200, response_class=HTMLResponse)
async def get_appconfig(request: Request):
    application = await appconfig_service.get_application()
    environment = await appconfig_service.get_environment()
    profile = await appconfig_service.get_profile()
    config = await appconfig_service.get_appconfig()

    return templates.TemplateResponse("table.html",
                                      {"request": request, "application": application['service'],
                                       "environment": environment['service'], "profile": profile['service'],
                                       "data": config})
