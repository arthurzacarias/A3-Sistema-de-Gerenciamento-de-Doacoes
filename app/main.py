from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

# Importa routers
from app.routers import doacoes, cep

# Funções do banco
from app.database import listar_doacoes, conectar

app = FastAPI()

# Templates
templates = Jinja2Templates(directory="app/templates")

# Arquivos estáticos
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Rotas externas
app.include_router(doacoes.router)
app.include_router(cep.router)


# -------------------------
# PÁGINA INICIAL
# -------------------------
@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    todas = listar_doacoes()

    # FORMATAR ENDEREÇO
    doacoes_formatadas = []
    for d in todas:
        endereco = d[4]

        # Se estiver em JSON → converter
        if endereco.startswith("{"):
            import json
            e = json.loads(endereco)
            endereco = f"{e['logradouro']}, {e['bairro']}, {e['cidade']} - {e['estado']}"

        doacoes_formatadas.append((
            d[0], d[1], d[2], d[3], endereco, d[5]
        ))

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "doacoes": doacoes_formatadas}
    )


# -------------------------
# TELA DE CADASTRO
# -------------------------
@app.get("/cadastro", response_class=HTMLResponse)
async def cadastro(request: Request):
    return templates.TemplateResponse("cadastrar.html", {"request": request})


# -------------------------
# TELA DE CONFIRMAÇÃO
# -------------------------
@app.get("/confirmacao", response_class=HTMLResponse)
async def confirmacao(request: Request, item: str, quantidade: int, tipo: str):
    return templates.TemplateResponse(
        "confirmacao.html",
        {
            "request": request,
            "item": item,
            "quantidade": quantidade,
            "tipo": tipo
        }
    )


# -------------------------
# PÁGINA DE EDIÇÃO
# -------------------------
@app.get("/editar/{id}", response_class=HTMLResponse)
async def editar_doacao(request: Request, id: int):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("SELECT * FROM doacoes WHERE id=?", (id,))
    d = cur.fetchone()
    conn.close()

    return templates.TemplateResponse(
        "editar.html",
        {"request": request, "d": d}
    )


# -------------------------
# PROCESSAR EDIÇÃO
# -------------------------
@app.post("/editar/{id}")
async def editar_salvar(request: Request, id: int):
    form = await request.form()

    item = form.get("item")
    quantidade = form.get("quantidade")
    tipo = form.get("tipo")
    endereco = form.get("endereco")
    status = form.get("status")

    conn = conectar()
    cur = conn.cursor()

    cur.execute("""
        UPDATE doacoes
        SET item=?, quantidade=?, tipo=?, endereco=?, status=?
        WHERE id=?
    """, (item, quantidade, tipo, endereco, status, id))

    conn.commit()
    conn.close()

    return RedirectResponse(url="/", status_code=302)


# -------------------------
# EXCLUIR DOAÇÃO
# -------------------------
@app.get("/excluir/{id}")
async def excluir(id: int):
    conn = conectar()
    cur = conn.cursor()

    cur.execute("DELETE FROM doacoes WHERE id=?", (id,))
    conn.commit()
    conn.close()

    return RedirectResponse(url="/", status_code=302)
