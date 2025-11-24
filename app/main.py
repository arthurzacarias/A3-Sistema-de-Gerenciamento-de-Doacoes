from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routers import doacoes, cep

app = FastAPI()

# Arquivos estáticos (CSS, JS, Imagens)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Inclui as rotas que fazem o sistema funcionar
# Como o doacoes.router não tem prefixo, ele assume a home "/"
app.include_router(doacoes.router)
app.include_router(cep.router)