# Projeto de API para Integração de Sistemas (N703)
## API da Plataforma de Adoção "A Friend for Life"

Este repositório contém o código-fonte e a documentação de uma API REST desenvolvida sobre a plataforma "A Friend for Life". O objetivo deste projeto é expor os dados de pets disponíveis para adoção, permitindo a integração com sistemas externos, conforme os requisitos da disciplina.

![Status](https://img-shields.io/badge/Status-API%20Funcional-brightgreen)![Python](https://img-shields.io/badge/Python-3.x-blue)![Django](https://img-shields.io/badge/Django-4.x-darkgreen)![DRF](https://img-shields.io/badge/DRF-3.x-red)


### 1. Objetivo do Trabalho

O objetivo é desenvolver uma API REST funcional que integre pelo menos dois sistemas distintos. O **Sistema 1** é a aplicação Django, que atua como provedor dos dados. O **Sistema 2** é um cliente de API (neste caso, o Postman), que consome os dados para validação e teste.

### 2. Descrição Funcional da Solução

A API expõe os dados de animais cadastrados na plataforma, permitindo que aplicações externas listem todos os pets disponíveis para adoção e consultem os detalhes de um pet específico. A comunicação é feita via protocolo HTTP, e os dados são trafegados no formato JSON, seguindo os princípios REST.

---

### 3. Guia de Instalação e Execução

Siga estes passos para configurar e rodar a aplicação e sua API localmente.

#### a. Pré-requisitos
-   Python 3.x
-   Git

#### b. Configuração do Ambiente
```bash
# 1. Clone este repositório
git clone https://github.com/Yuridevpro/api_friend_for_life
cd https://github.com/Yuridevpro/api_friend_for_life

# 2. Crie e ative o ambiente virtual
# Crie No macOS/Linux:
python3 -m venv venv
# Ative No macOS/Linux:
source venv/bin/activate

# Crie No Windows:
python -m venv venv
# Ative No Windows:
venv\Scripts\activate

# 3. Instale as dependências do projeto
pip install -r requirements.txt
```

#### d. Banco de Dados e Dados de Teste
```bash
# 5. Navegue até a pasta do código-fonte Django
cd src

# 6 crie as migracoes 
python manage.py makemigrations

# 7. execute a migacao e Crie o banco de dados SQLite e suas tabelas
python manage.py migrate

# 8. Popule o banco de dados com usuários e pets de teste
python manage.py seed_data
```

#### e. Executando a Aplicação
```bash
# 9. Inicie o servidor de desenvolvimento Django
python manage.py runserver
```
A aplicação e sua API estarão disponíveis em **http://127.0.0.1:8000**.

---

### 4. Testando a API

#### a. Testes Unitários Automatizados
Com o ambiente configurado, você pode rodar a suíte de testes unitários.

```bash
# Navegue até a pasta do código-fonte
cd src

# Execute o comando de teste. O Django encontrará os testes automaticamente.
python manage.py test
```
**Resultado esperado:** Todos os testes devem passar com o status `OK`.

#### b. Verificação Rápida via Navegador
A API desenvolvida com Django REST Framework oferece uma interface navegável para desenvolvimento e verificação rápida. Com o servidor rodando, você pode usar seu navegador para inspecionar os endpoints:

1.  **Listar todos os pets:**
    *   Acesse: [http://127.0.0.1:8000/api/pets/](http://127.0.0.1:8000/api/pets/)
    *   **Resultado esperado:** Uma página do DRF exibindo uma lista de todos os pets de teste em formato JSON.

2.  **Ver detalhes de um pet específico:**
    *   Acesse: [http://127.0.0.1:8000/api/pets/1/](http://127.0.0.1:8000/api/pets/1/)
    *   **Resultado esperado:** Uma página do DRF exibindo os dados em JSON do pet com `id=1`, que foi criado pelo comando `seed_data`.

#### c. Teste Completo via Postman/Insomnia
Para uma validação mais formal e para simular um cliente de API externo, utilize a coleção fornecida:

1.  Com o servidor ainda rodando, abra o Postman ou Insomnia.
2.  Importe a coleção de testes localizada em: `/postman/api-friend-for-life.postman_collection.json`.
3.  Execute as requisições `Listar todos os pets` e `Obter detalhes de um pet`.
4.  **Resultado esperado:** Ambas as requisições devem retornar um status `200 OK` com os respectivos dados em JSON.```



---

### 5. Documentação das Rotas da API (Swagger/OpenAPI)

A documentação completa e interativa da API, gerada automaticamente, está disponível nos seguintes endpoints enquanto o servidor estiver rodando:

-   **Swagger UI (Recomendado):** [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
-   **ReDoc:** [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)

#### Endpoints Implementados
| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/pets/` | Retorna uma lista paginada de todos os pets disponíveis para adoção. |
| `GET` | `/api/pets/{id}/` | Retorna os detalhes de um pet específico pelo seu ID. |

---

### 6. Estrutura Principal do Repositório

```
/
├── 📄 README.md                # Documentação principal e guia de execução
├── 📂 docs/                     # Documentação adicional (Arquitetura)
│   └── architecture.md
├── 📂 src/                      # Código-fonte principal da aplicação Django
├── 📂 tests/                    # Testes unitários da API
│   └── instrucao.txt
└── 📂 postman/                  # Coleção do Postman para testes manuais
    └── collection.json
```

---

### 7. Equipe
- **Nome do Integrante 1:** [Matrícula]
- **Nome do Integrante 2:** [Matrícula]
- **Nome do Integrante 3:** [Matrícula]
- **Nome do Integrante 4:** [Matrícula]