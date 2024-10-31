# Flask API Biblioteca

API de biblioteca desenvolvida em Flask para gerenciar empréstimos de livros, usuários e livros.

---

## Sobre o projeto

Este projeto utiliza Flask para criação de APIs RESTful com um sistema de empréstimos, gerenciando usuários e livros. A API possui documentação automática com Swagger para fácil exploração e teste das rotas.

---

## Instalação e Configuração

**1. Clone o repositório:**
```bash
git clone https://github.com/ligiaboliveira/flask-api-biblioteca.git
```

**Navegue até o diretório do projeto:**
```bash
cd flask-api-biblioteca
```

**Crie um ambiente virtual (opcional, mas recomendado):**
```bash
python3 -m venv .venv
```

**Ative o ambiente virtual:**
```bash
# No Linux ou MacOS
source .venv/bin/activate
```

**Instale as dependências do projeto:**
```bash
pip install -r requirements.txt
```

**Adicione as migrations (se estiver usando Flask-Migrate):**
```bash
flask db init
flask db migrate -m "Initial migration."
flask db upgrade
```

**Inicie o servidor de desenvolvimento:**
```bash
flask run
```

**Acesse a aplicação em seu navegador web:**
> [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

---

## Documentação da API

A API possui uma documentação interativa gerada pelo **Swagger**, que pode ser acessada em:

> [http://localhost:5000/apidocs/](http://localhost:5000/apidocs/)

A documentação permite explorar e testar todas as rotas da API diretamente pelo navegador, proporcionando uma visão completa dos endpoints disponíveis, seus métodos, parâmetros e respostas.

## Contribuições

Sinta-se à vontade para abrir issues ou pull requests para melhorias!

## Licença

Este projeto está licenciado sob a MIT License. Veja o arquivo LICENSE para mais detalhes.

---