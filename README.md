# API REST de Cadastro de Usuários

Este projeto consiste em uma API REST funcional para cadastro e gerenciamento de usuários. Desenvolvida em Python com o framework **FastAPI**, a aplicação utiliza o ORM **SQLAlchemy** para persistência de dados em um banco de dados **MySQL**.

O grande diferencial deste projeto é a adoção da **Arquitetura em Camadas (Layered Architecture)**, separando de forma clara as responsabilidades de rotas, regras de negócio e persistência de dados.

---

## 🏛️ Arquitetura do Projeto

A estrutura do projeto foi desenhada para garantir manutenibilidade, testabilidade e escalabilidade, dividindo-se nas seguintes camadas:

* **`controllers/` (Camada de Apresentação):** Responsável por expor os endpoints HTTP, receber as requisições e acionar a camada de serviço correspondente.
* **`services/` (Camada de Negócio):** Onde residem as validações e regras de negócio do sistema (ex: checagem de e-mails duplicados).
* **`repositories/` (Camada de Acesso a Dados):** Isola as consultas SQL/SQLAlchemy, gerenciando a comunicação direta com o banco.
* **`models/` (Camada de Domínio/ORM):** Contém os mapeamentos das tabelas do banco de dados utilizando SQLAlchemy.
* **`schemas/` (Camada de Validação/DTOs):** Define as regras de entrada e saída de dados usando Pydantic, garantindo tipagem forte e segurança.
* **`config/` (Configurações):** Centraliza a conexão com o banco de dados e gerenciamento de sessões.

### 📁 Estrutura de Pastas

```text
meu_projeto/
│
├── config/
│   └── database.py       # Configuração e sessão do MySQL
├── controllers/
│   └── usuario_controller.py # Rotas e endpoints HTTP
├── models/
│   └── usuario_model.py  # Entidade mapeada do banco de dados
├── repositories/
│   └── usuario_repo.py   # Manipulação de dados (Queries)
├── schemas/
│   └── usuario_schema.py # DTOs e validações com Pydantic
├── services/
│   └── usuario_service.py# Camada com as Regras de Negócio
├── main.py               # Arquivo principal e inicialização da API
└── README.md             # Documentação do projeto
```
## Regras de Negócio Implementadas

1 - Unicidade de E-mail no Cadastro: Não é permitido registrar dois usuários com o mesmo endereço de e-mail.

2 - Validação de E-mail Modificado: Na atualização de credenciais ou dados gerais, o sistema impede a alteração do e-mail para um endereço que já pertença a outro usuário.

3 - Tratamento de Exceções Nativo: Caso um usuário buscado por ID não exista, o sistema intercepta a requisição e retorna o status 404 Not Found padronizado.

4 - Isolamento de Dados Sensíveis: O campo senha nunca é exposto nas rotas de leitura ou resposta da API.

## Tecnologias Utilizadas

- Python 3.10+
- FastAPI: Framework web moderno e de alto desempenho.
- SQLAlchemy: Mapeamento Objeto-Relacional (ORM) para Python.
- PyMySQL: Driver de conexão para o banco MySQL.
- Pydantic: Validação de dados e parsing.
- Uvicorn: Servidor ASGI para rodar a aplicação.


## Como Executar o Projeto Localmente

### Pró-requisitos
Antes de começar, certifique-se de ter instalado em sua máquina:

- Python (versão 3.10 ou superior)
- Servidor MySQL ativo

### 1 - Clonar o Repositório
- git clone https://github.com/Thiemeleci/API-Sistema-de-usuarios.git

### 2 - Configurar o Ambiente Virtual (Opcional, mas recomendado)
- python -m venv venv (Para criar o ambiente virtual)
- .\venv\Scripts\activate (Ativar no windows)
- source venv/bin/activate (Ativar no Linux/MacOS)

### 3 - Instalar as Dependências
- pip install fastapi uvicorn sqlalchemy cryptography pymysql pydantic[email]

### 4 - Configurar o Banco de Dados
- Crie um banco de dados no seu MySQL chamado sistema_usuarios
- Abra o arquivo config/database.py e configure a string de conexão com o seu usuário e senha do MySQL (Ex: SQLALCHEMY_DATABASE_URL = "mysql+pymysql://seu_usuario:sua_senha@localhost:3306/sistema_usuarios")

### 5 - Executar a Aplicação
- python main.py
- A API estará disponível no endereço: http://127.0.0.1:8000

## Endpoints Criados:

- POST - /usuarios - Cadastro de um novo usuário
- GET - /usuarios - Lista todos os usuários cadastrados
- GET - /usuarios/{id} - Busca um usuário pelo Id
- PUT - /usuarios/{id} - Atualização completa dos dados do usuário
- PATCH - /usuarios/{id}/credenciais - Atualização parcial (apenas e-mail e/ou senha)
- DELETE - /usuarios/{id} - Exclusão de um usuário do sistema

## Como Testar no Postman

- Criar Usuário (POST)
- URL: http://127.0.0.1:8000/usuarios/
- Body (raw -> JSON):
- {
  "nome": "exemplo",
  "email": "exemplo@gmail.com",
  "senha": "exemplo123"
}