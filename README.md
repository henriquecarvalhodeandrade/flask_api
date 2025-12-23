# Flask API - Sistema de Gerenciamento Educacional

Este repositório contém uma API REST robusta desenvolvida com **Flask**, focada no gerenciamento de cursos, formações, professores e usuários. A aplicação utiliza práticas modernas de desenvolvimento, incluindo autenticação JWT, controle de acesso baseado em funções (RBAC) e persistência em banco de dados relacional.

## Funcionalidades

- **Gerenciamento de Cursos:** CRUD completo para cursos, incluindo integração com formações.
- **Gestão de Formações:** Organização de cursos e vinculação de múltiplos professores.
- **Controle de Professores:** Cadastro e listagem de instrutores.
- **Sistema de Usuários e Segurança:**
  - Registro de usuários com senhas criptografadas (`passlib`).
  - Autenticação via **JWT (JSON Web Tokens)** com suporte a Refresh Tokens.
  - Controle de acesso administrativo via decorator `@admin_required`.
  - Proteção de endpoints via `@api_key_required` usando chaves API únicas.
- **Paginação:** Resultados de listagem otimizados com suporte a parâmetros de página e quantidade por item.
- **HATEOAS:** Links dinâmicos nos recursos para facilitar a navegação na API.

## Tecnologias Utilizadas

- **Core:** Flask, Flask-RESTful.
- **Banco de Dados:** SQLAlchemy (ORM), Flask-Migrate (Alembic) para migrações e PyMySQL.
- **Serialização:** Marshmallow e Flask-Marshmallow para validação e transformação de dados.
- **Segurança:** Flask-JWT-Extended e Passlib.
- **Servidor:** Gunicorn (configurado no Procfile para deploy).

## Configuração e Instalação

1. **Clonar o repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd flask_api
2. **Configurar o ambiente virtual:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate

    Instalar dependências:
    Bash

    pip install -r Requirements.txt

    Configurar o Banco de Dados: Certifique-se de ter um servidor MySQL rodando e ajuste as credenciais no arquivo config.py:
    Python

    USERNAME = "root"
    PASSWORD = "seu_password"
    SERVER = "localhost"
    DB = "api_flask"
3. **Executar Migrações:**
    ```bash
    flask db upgrade
4. **Rodar a aplicação:**
    ```bash
    python api/run.py
## Principais Endpoints

    POST /login: Autenticação de usuário e geração de tokens.

    GET /cursos: Listagem paginada de cursos (requer api_key).

    GET/POST /formacoes: Gerenciamento de formações (requer JWT).

    GET/POST /professores: Gerenciamento de professores (requer JWT).

    POST /usuario: Criação de novos usuários e geração de api_key.

### Principais pontos incluídos:
- **Segurança:** Destaquei o uso de `api_key` e `JWT`, que são diferenciais do seu código.
- **Estrutura:** Mencionei o uso de `Services`, `Models`, `Views` (Resource) e `Schemas`, que organizam bem o seu projeto.
- **Persistência:** Referenciei o fluxo de migrações com Alembic que está presente no seu diretório `migrations`.


###### Referência:  [Udemy -Desenvolvimento Web com Flask](https://www.udemy.com/course/desenvolvimento-web-com-flask/?couponCode=CM251223G1)
