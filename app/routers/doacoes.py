from fastapi import APIRouter, Form, Request
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.database import salvar_doacao, listar_doacoes, buscar_doacao_por_id, atualizar_doacao, excluir_doacao

router = APIRouter(tags=["Doações"])
templates = Jinja2Templates(directory="app/templates")

# Rota para renderizar a página inicial
@router.get("/")
def listar(request: Request):
    doacoes = listar_doacoes()
    return templates.TemplateResponse("index.html", {"request": request, "doacoes": doacoes})

# Rota para renderizar o formulário de cadastro
@router.get("/cadastro")
def form_cadastro(request: Request):
    return templates.TemplateResponse("cadastrar.html", {"request": request})

# Recebe dados do formulário e cria doação
@router.post("/doacoes")
def criar_doacao(
    item: str = Form(...),
    quantidade: str = Form(...), # Mudado de int para str para aceitar "1 kg", "1 litro"
    tipo: str = Form(...),
    cep: str = Form(...),
    logradouro: str = Form(...),
    numero: int = Form(...),
    complemento: str = Form(None), # Opcional
    bairro: str = Form(...),
    cidade: str = Form(...),
    estado: str = Form(...),
    status: str = Form(...)
):
    # Salva no banco com os campos separados
    salvar_doacao(item, quantidade, tipo, cep, logradouro, numero, complemento, bairro, cidade, estado, status)

    # Redireciona para confirmação
    url = f"/confirmacao?item={item}&quantidade={quantidade}&tipo={tipo}"
    return RedirectResponse(url=url, status_code=303)

@router.get("/confirmacao")
def confirmacao(request: Request, item: str, quantidade: str, tipo: str):
    return templates.TemplateResponse("confirmacao.html", {
        "request": request, 
        "item": item, 
        "quantidade": quantidade, 
        "tipo": tipo
    })

# Rotas de Edição e Exclusão
@router.get("/editar/{id_doacao}")
def form_editar(request: Request, id_doacao: int):
    d = buscar_doacao_por_id(id_doacao)
    return templates.TemplateResponse("editar.html", {"request": request, "d": d})

@router.post("/editar/{id_doacao}")
def salvar_edicao(
    id_doacao: int,
    item: str = Form(...),
    quantidade: str = Form(...), # Mudado de int para str
    tipo: str = Form(...),
    cep: str = Form(...),
    logradouro: str = Form(...),
    numero: int = Form(...),
    complemento: str = Form(None),
    bairro: str = Form(...),
    cidade: str = Form(...),
    estado: str = Form(...),
    status: str = Form(...)
):
    atualizar_doacao(id_doacao, item, quantidade, tipo, cep, logradouro, numero, complemento, bairro, cidade, estado, status)
    return RedirectResponse(url="/", status_code=303)

@router.get("/excluir/{id_doacao}")
def deletar(id_doacao: int):
    excluir_doacao(id_doacao)
    return RedirectResponse(url="/", status_code=303)