from fastapi import FastAPI, Depends, HTTPException
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from database.database import SessionLocal, engine, Base
from database.models import Produto
from pydantic import BaseModel

# Cria as tabelas no banco de dados SQLite automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="LootSync API",
    description="Sistema de Gestão de Catálogo e Versões para Assets e Produtos Digitais",
    version="1.0.0"
)

# Monta a pasta static para servir o painel web (HTML, CSS e JS)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Dependência para pegar a sessão do banco de dados em cada requisição


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Estrutura dos dados para criar ou atualizar um produto (Pydantic)


class ProdutoCreate(BaseModel):
    nome: str
    tipo: str
    versao: str
    tamanho: str
    descricao: str


@app.get("/")
def read_root():
    return {
        "projeto": "LootSync",
        "status": "Online",
        "mensagem": "Bem-vindo à API de gestão de produtos digitais da SyncedCorp!"
    }

# Rota para CADASTRAR um novo produto/asset (POST)


@app.post("/produtos/")
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
    novo_produto = Produto(
        nome=produto.nome,
        tipo=produto.tipo,
        versao=produto.versao,
        tamanho=produto.tamanho,
        descricao=produto.descricao
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return {"mensagem": "Produto cadastrado com sucesso!", "produto": novo_produto}

# Rota para LISTAR todos os produtos cadastrados (GET)


@app.get("/produtos/")
def listar_produtos(db: Session = Depends(get_db)):
    produtos = db.query(Produto).all()
    return produtos

# Rota para ATUALIZAR um produto existente pelo ID (PUT)


@app.put("/produtos/{produto_id}")
def atualizar_produto(produto_id: int, produto_dados: ProdutoCreate, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        raise HTTPException(status_code=404, chno="Produto não encontrado")

    produto.nome = produto_dados.nome
    produto.tipo = produto_dados.tipo
    produto.versao = produto_dados.versao
    produto.tamanho = produto_dados.tamanho
    produto.descricao = produto_dados.descricao

    db.commit()
    db.refresh(produto)
    return {"mensagem": "Produto atualizado com sucesso!", "produto": produto}

# Rota para DELETAR um produto pelo ID (DELETE)


@app.delete("/produtos/{produto_id}")
def deletar_produto(produto_id: int, db: Session = Depends(get_db)):
    produto = db.query(Produto).filter(Produto.id == produto_id).first()

    if not produto:
        raise HTTPException(status_code=404, detail="Produto não encontrado")

    db.delete(produto)
    db.commit()
    return {"mensagem": "Produto deletado com sucesso!"}
