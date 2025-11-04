from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes

app = FastAPI(title="CipherSecurity API")

# Permite acesso do frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite qualquer origem (para testes)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclui as rotas diretamente (sem prefixo adicional)
app.include_router(routes.router, prefix="")  # <-- ESSENCIAL
