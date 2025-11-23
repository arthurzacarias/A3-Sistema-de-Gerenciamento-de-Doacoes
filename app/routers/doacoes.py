from fastapi import APIRouter, Form
from app.models.doacao_model import Doacao
from app.services.viacep import buscar_cep
from app.database import salvar_doacao, listar_doacoes
from fastapi.responses import RedirectResponse
import json

router = APIRouter(prefix="/doacoes", tags=["Doações"])

# Recebe dados do formulário e cria doação
@router.post("/")
def criar_doacao(
    item: str = Form(...),
    quantidade: int = Form(...),
    tipo: str = Form(...),
    cep: str = Form(...),
    status: str = Form(...)
):
    # Consulta endereço
    endereco = buscar_cep(cep)
    endereco_str = json.dumps(endereco)

    # Salva no banco
    salvar_doacao(item, quantidade, tipo, endereco_str, status)

    # Envia o usuário para a página de confirmação
    url = f"/confirmacao?item={item}&quantidade={quantidade}&tipo={tipo}"

    return RedirectResponse(url=url, status_code=303)

# Rota que lista todas as doações
@router.get("/")
def listar():
    return listar_doacoes()
