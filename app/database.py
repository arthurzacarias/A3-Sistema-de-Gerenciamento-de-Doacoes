import sqlite3

DB_NAME = "doacoes.db"

def conectar():
    conn = sqlite3.connect(DB_NAME)
    return conn

def criar_tabela():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS doacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            item TEXT NOT NULL,
            quantidade TEXT NOT NULL, -- Mudado de INTEGER para TEXT
            tipo TEXT NOT NULL,
            cep TEXT NOT NULL,
            logradouro TEXT NOT NULL,
            numero INTEGER NOT NULL,
            complemento TEXT,
            bairro TEXT NOT NULL,
            cidade TEXT NOT NULL,
            estado TEXT NOT NULL,
            status TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Inicializa a tabela ao importar
criar_tabela()

def salvar_doacao(item, quantidade, tipo, cep, logradouro, numero, complemento, bairro, cidade, estado, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO doacoes (item, quantidade, tipo, cep, logradouro, numero, complemento, bairro, cidade, estado, status)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (item, quantidade, tipo, cep, logradouro, numero, complemento, bairro, cidade, estado, status))
    conn.commit()
    conn.close()

def listar_doacoes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doacoes")
    doacoes = cursor.fetchall()
    conn.close()
    return doacoes

def buscar_doacao_por_id(id_doacao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doacoes WHERE id = ?", (id_doacao,))
    d = cursor.fetchone()
    conn.close()
    return d

def atualizar_doacao(id_doacao, item, quantidade, tipo, cep, logradouro, numero, complemento, bairro, cidade, estado, status):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE doacoes 
        SET item=?, quantidade=?, tipo=?, cep=?, logradouro=?, numero=?, complemento=?, bairro=?, cidade=?, estado=?, status=?
        WHERE id=?
    """, (item, quantidade, tipo, cep, logradouro, numero, complemento, bairro, cidade, estado, status, id_doacao))
    conn.commit()
    conn.close()

def excluir_doacao(id_doacao):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM doacoes WHERE id = ?", (id_doacao,))
    conn.commit()
    conn.close()