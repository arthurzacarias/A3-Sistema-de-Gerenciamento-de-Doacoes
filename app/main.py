# Importa FastAPI e ferramentas de resposta e templates
from urllib import request
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles


# Importa router de doações e função para listar doações
from app.routers import doacoes
from app.database import listar_doacoes


# Inicializa o aplicativo FastAPI
app = FastAPI()


# Define onde estão os templates HTML
templates = Jinja2Templates(directory="app/templates")


# Publica arquivos estáticos (CSS, imagens etc.)
app.mount("/static", StaticFiles(directory="app/static"), name="static")


# Registra rotas do módulo de doações
app.include_router(doacoes.router)


# Rota da página inicial
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    todas = listar_doacoes() # Busca doações no banco
    return templates.TemplateResponse("index.html", {"request": request, "doacoes": todas})

# Rota do formulário de cadastro
@app.get("/cadastro", response_class=HTMLResponse)
async def form_cadastro(request: Request):
    return templates.TemplateResponse("cadastrar.html", {"request": request})