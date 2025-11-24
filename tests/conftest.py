import pytest
import os
from fastapi.testclient import TestClient
from app.main import app
import app.database as database

# Define um nome de banco de dados específico para testes
TEST_DB_NAME = "test_doacoes.db"

@pytest.fixture(scope="function", autouse=True)
def setup_test_db():
    """
    Esta fixture roda automaticamente antes de cada teste.
    1. Troca o nome do banco para um arquivo de teste.
    2. Cria a tabela do zero.
    3. Roda o teste.
    4. Apaga o banco de teste no final.
    """
    # 1. Patch: Troca o nome do banco na aplicação para o banco de teste
    original_db_name = database.DB_NAME
    database.DB_NAME = TEST_DB_NAME

    # 2. Garante que o banco antigo não exista e cria as tabelas novas
    if os.path.exists(TEST_DB_NAME):
        os.remove(TEST_DB_NAME)
    database.criar_tabela()

    yield # Aqui o teste acontece

    # 3. Limpeza: Fecha conexões pendentes (se houver) e apaga o arquivo
    database.DB_NAME = original_db_name
    if os.path.exists(TEST_DB_NAME):
        try:
            os.remove(TEST_DB_NAME)
        except PermissionError:
            pass # Às vezes o windows segura o arquivo por alguns milissegundos

@pytest.fixture
def client():
    return TestClient(app)