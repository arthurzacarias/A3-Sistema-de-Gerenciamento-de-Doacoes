from app.database import salvar_doacao, listar_doacoes, buscar_doacao_por_id, atualizar_doacao, excluir_doacao, criar_tabela

# O conftest.py já lida com a criação/destruição do banco, 
# então podemos chamar as funções direto.

def test_database_crud_direct():
    # 1. Salvar
    salvar_doacao("Unit Test", 1, "Unit", "00000", "Rua U", 1, "", "Bairro U", "Cidade U", "UF", "OK")
    
    # 2. Listar
    lista = listar_doacoes()
    assert len(lista) == 1
    id_doacao = lista[0][0] # O ID é o primeiro item da tupla
    
    # 3. Buscar por ID
    d = buscar_doacao_por_id(id_doacao)
    assert d is not None
    assert d[1] == "Unit Test" # Item
    
    # 4. Atualizar
    # Nota: atualizar_doacao espera todos os campos separados conforme seu database.py
    atualizar_doacao(
        id_doacao, "Updated Item", 2, "Unit", "00000", "Rua U", 1, "", "Bairro U", "Cidade U", "UF", "Updated"
    )
    
    d_atualizado = buscar_doacao_por_id(id_doacao)
    assert d_atualizado[1] == "Updated Item"
    assert d_atualizado[11] == "Updated" # Status (índice 11 na tabela)

    # 5. Excluir
    excluir_doacao(id_doacao)
    d_final = buscar_doacao_por_id(id_doacao)
    assert d_final is None