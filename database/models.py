from sqlalchemy import Column, Integer, String
from .database import Base


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)
    tipo = Column(String)  # Ex: Sprite, Áudio, Script, Build
    versao = Column(String)  # Ex: v1.0.0
    tamanho = Column(String)  # Ex: 15MB
    descricao = Column(String)
