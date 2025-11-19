import sqlite3

# Nome do arquivo do banco
DB_NAME = "doacoes.db" 

def conectar():
    # Cria e retorna uma conexão com o banco SQLite
    return sqlite3.connect(DB_NAME)

def criar_tabela():
    # Cria tabela de doações caso ainda não exista
    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS doacoes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    item TEXT,
    quantidade INTEGER,
    tipo TEXT,
    endereco TEXT,
    status TEXT
    )
    """)

    conn.commit()
    conn.close()

# Cria tabela automaticamente ao iniciar o sistema
criar_tabela()

def salvar_doacao(item, quantidade, tipo, endereco, status):
    #Insere uma nova doação no banco
    conn = conectar()
    cur = conn.cursor()

    cur.execute(
    "INSERT INTO doacoes(item, quantidade, tipo, endereco, status) VALUES (?, ?, ?, ?, ?)",
    (item, quantidade, tipo, endereco, status)
    )

    conn.commit()
    conn.close()

def listar_doacoes():
    # Retorna todas as doações cadastradas
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT id, item, quantidade, tipo, endereco, status FROM doacoes")
    data = cur.fetchall()

    conn.close()
    return data