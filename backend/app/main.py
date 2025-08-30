from fastapi import FastAPI
from app.api import routes

app = FastAPI(title="CipherSecurity API")

app.include_router(routes.router)