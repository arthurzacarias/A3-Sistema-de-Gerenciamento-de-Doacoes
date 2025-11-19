from pydantic import BaseModel

class Doacao(BaseModel):
    nome: str            # Nome de quem está doando
    item: str            # Item doado (ex: roupas, alimentos)
    quantidade: int      # Quantidade do item
    cep: str             # CEP informado no cadastro
    endereco: dict | None = None   # Endereço retornado pela API ViaCEP
