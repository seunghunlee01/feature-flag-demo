from fastapi import FastAPI

from app.apis.v1.routes import router as v1_router
from app.setup.service import appconfig_service

app = FastAPI()
app.include_router(v1_router)

@app.get("/healthz")
async def get_health_status():
    return {"message": "healthy"}


@app.on_event("startup")
async def startup_event():
    await appconfig_service.start_scheduler()


@app.on_event("shutdown")
async def shutdown_event():
    await appconfig_service.stop_scheduler()
