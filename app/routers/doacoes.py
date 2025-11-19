from fastapi import APIRouter, Form
from app.database import salvar_doacao, listar_doacoes
from app.services.viacep import buscar_cep

router = APIRouter(prefix="/doacoes", tags=["Doações"])

@router.post("/")
def criar_doacao(
    item: str = Form(...),
    quantidade: int = Form(...),
    tipo: str = Form(...),
    cep: str = Form(...),
    status: str = Form(...)
):
    # Consulta endereço via API
    endereco = buscar_cep(cep)

    # Salva no banco SQLite
    salvar_doacao(item, quantidade, tipo, endereco, status)

    return {"mensagem": "Doação registrada com sucesso!"}


@router.get("/")
def listar():
    return listar_doacoes()
