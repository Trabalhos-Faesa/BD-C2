# Projeto

Trabalho C2 da disciplina de Banco de Dados na FAESA.

## Tema

O tema escolhido foi "Controle de Venda de produtos", a ideia é um back-end simples que provê uma forma de implementar um fluxo de pedidos de produtos por clientes através de um carrinho de compras que contém itens, além de relatórios. Veja também `DIAGRAMA-RELACIONAL.png` e acesse a página `/docs` da aplicação em execução.

## Dependências para execução local

- [Docker](https://docs.docker.com/desktop/setup/install/linux/) (e Docker Compose)
- [Postgres](https://www.postgresql.org/) em execução, devidamente configurado (veja `postgres.example.env`)
  - `docker compose up -d --force-recreate postgres`
- Pacotes Python, usando [uv](https://docs.astral.sh/uv/) e [venv](https://docs.python.org/pt-br/3/library/venv.html)
  - Criar o ambiente virtual: `uv venv` (opcional, o _uv_ através de `uv sync` já cria um ambiente virtual em `.venv` automaticamente caso não exista)
  - Instalar todas as dependências (`--all-extras --all-groups`) do ambiente reprodutível (`--frozen`): `uv sync --all-extras --all-groups --frozen`

  - Para quem prefere usar apenas _pip_ e não usar _uv_
    - Criar o ambiente virtual `.venv`: `python -m venv .venv`
    - Ativar o ambiente virtual: `. ./.venv/bin/activate`
    - Atualizar o _pip_ e instalar pacotes importantes: `python -m pip install -U pip setuptools wheel`
    - Instalar todas as dependências: `pip install -r requirements.txt`

- Arquivos `.env` e `postgres.env` devidamente definidos (faça uma cópia de `.example.env` e `postgres.example.env`)

## Iniciar a aplicação

### Iniciar o servidor (pela CLI)

- Ativar o ambiente virtual: `. ./.venv/bin/activate`
- `fastapi dev src/main.py`

- Sem precisar ativar o ambiente virtual: `./.venv/bin/fastapi dev src/main.py`

### Iniciar o servidor (pelo VSCode)

- Crie uma cópia de `.vscode/settings.example.json` como `.vscode/settings.json` (recomendável)
- Crie uma cópia de `.vscode/launch.example.json` como `.vscode/launch.json` (obrigatório)
- Instale as extensões do VSCode recomendadas para esse repositório/workspace (definidas por `.vscode/extensions.json`) (recomendável, sendo algumas obrigatórias)

- Por fim, pode-se usar o debugger do VSCode (atalho de teclado `F5`) para executar (e depurar) a aplicação.

### Iniciar o servidor (pelo Docker Compose)

- `docker compose up -d --force-recreate --build app`
