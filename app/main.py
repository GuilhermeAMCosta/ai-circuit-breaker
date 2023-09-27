import uvicorn
from fastapi import FastAPI

from app import __version__
from app.api.routes import health
from app.settings import deploy_settings

app = FastAPI(
    title=deploy_settings.APP,
    version=__version__,
    description="Circuit Breaker - Controller for Payments",
    docs_url="/docs",
)

app.include_router(health.router, prefix=deploy_settings.BASE_PATH)

uvicorn.run(
    app=app,
    host=deploy_settings.HOST,
    port=deploy_settings.PORT,
    timeout_keep_alive=50,
)
