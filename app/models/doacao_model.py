from pydantic import BaseModel
from typing import Optional

class Doacao(BaseModel):
    nome: str            
    item: str            
    quantidade: int      
    cep: str             
    logradouro: str
    numero: int
    complemento: Optional[str] = None
    bairro: str
    cidade: str
    estado: str
    status: str