from fastapi import FastAPI
from app.api import routes

appcipher = FastAPI(title="CipherSecurity API")

appcipher.include_router(routes.router)