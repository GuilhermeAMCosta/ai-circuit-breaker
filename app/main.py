from app.settings import deploy_settings
from app import __version__
from app.api.routes import health

import uvicorn
from fastapi import FastAPI


app = FastAPI(
    title=deploy_settings.APP,
    version=__version__,
    description="Circuit Breaker X - Controller for XX",
    docs_url="/docs",
)


uvicorn.run(
    app=app,
    host=deploy_settings.HOST,
    port=deploy_settings.PORT,
    timeout_keep_alive=50,
)
