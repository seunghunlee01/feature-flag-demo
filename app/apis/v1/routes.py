from fastapi import APIRouter

from app.apis.v1.appconfig.apis import router as appconfig_router

router = APIRouter(prefix="/api/v1")
router.include_router(appconfig_router)
