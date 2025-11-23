from fastapi import APIRouter
from app.services.viacep import buscar_cep

router = APIRouter(prefix="/api", tags=["CEP"])

@router.get("/cep/{cep}")
def get_cep(cep: str):
    dados = buscar_cep(cep)
    return dados if dados else {"erro": "CEP inválido"}
