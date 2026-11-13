# 🚀 LootSync

Sistema de gestão de catálogo e versões de assets digitais da SyncedCorp. A aplicação combina uma API em Python com um painel web para cadastrar e consultar itens como sprites, áudios, scripts e builds.

## Funcionalidades

- Cadastro, listagem e exclusão de assets pelo painel web.
- API para criar, consultar, atualizar e excluir produtos.
- Armazenamento local em banco SQLite, criado automaticamente.
- Documentação interativa da API gerada pelo FastAPI.

## Requisitos

- Python 3
- pip

## Como executar

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/Renanxvier/syncedcorp-lootsync.git
cd syncedcorp-lootsync
```

Crie e ative um ambiente virtual. No Windows (PowerShell):

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

No macOS ou Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependências e inicie a API:

```bash
python -m pip install -r requirements.txt
python -m uvicorn main:app --reload
```

No Windows, se `py` não estiver disponível, use `python` para criar o ambiente virtual.

## Como usar

Com o servidor em execução, acesse:

- **Painel de assets:** <http://127.0.0.1:8000/static/index.html>
- **Documentação interativa da API:** <http://127.0.0.1:8000/docs>
- **Status da API:** <http://127.0.0.1:8000/>

No painel, preencha os dados do asset e selecione **Salvar Asset**. Os itens cadastrados aparecem no catálogo; use **Excluir** para removê-los. A atualização de um produto está disponível pela API.

## Endpoints da API

| Método | Endpoint | Ação |
| --- | --- | --- |
| `GET` | `/` | Retorna as informações e o status do projeto. |
| `GET` | `/produtos/` | Lista os produtos cadastrados. |
| `POST` | `/produtos/` | Cadastra um produto. |
| `PUT` | `/produtos/{produto_id}` | Atualiza um produto pelo ID. |
| `DELETE` | `/produtos/{produto_id}` | Exclui um produto pelo ID. |

O cadastro e a atualização recebem um JSON com `nome`, `tipo`, `versao`, `tamanho` e `descricao`. Exemplo:

```json
{
  "nome": "Pack de Sprites Viking",
  "tipo": "Sprite",
  "versao": "v1.0.0",
  "tamanho": "15MB",
  "descricao": "Sprites para um jogo de aventura."
}
```

## Estrutura do projeto

```text
syncedcorp-lootsync/
├── database/
│   ├── database.py    # Conexão e configuração do SQLite
│   └── models.py      # Modelo de produto
├── static/
│   └── index.html     # Painel web
├── main.py            # Aplicação FastAPI e endpoints
└── requirements.txt   # Dependências Python
```

## Tecnologias

- Python, FastAPI e Pydantic
- SQLAlchemy e SQLite
- HTML, CSS e JavaScript

O arquivo `lootsync.db` é criado na pasta do projeto quando a aplicação inicia. Ele armazena os dados localmente e não é enviado ao GitHub.
