# Projeto de API para Integração de Sistemas (N703)
## API da Plataforma de Adoção "A Friend for Life"

Este repositório contém o código-fonte e a documentação de uma API REST desenvolvida sobre a plataforma "A Friend for Life". O objetivo deste projeto é expor os dados de pets disponíveis para adoção, permitindo a integração com sistemas externos, conforme os requisitos da disciplina.

![Status](https://img.shields.io/badge/Status-API%20Funcional-brightgreen) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![Django](https://img.shields.io/badge/Django-4.x-darkgreen) ![DRF](https://img.shields.io/badge/DRF-3.x-red)

### 1. Objetivo do Trabalho

O objetivo é desenvolver uma API REST funcional que integre pelo menos dois sistemas distintos. O **Sistema 1** é a aplicação Django, que atua como provedor dos dados. O **Sistema 2** é um cliente de API (neste caso, o Postman), que consome os dados para validação e teste.

### 2. Descrição Funcional da Solução

A API expõe os dados de animais cadastrados na plataforma, permitindo que aplicações externas:
1.  Listem todos os pets disponíveis para adoção (`GET`).
2.  Consultem os detalhes de um pet específico (`GET`).

A comunicação é feita via protocolo HTTP, e os dados são trafegados no formato JSON, seguindo os princípios REST.

---

### 3. Guia de Instalação e Execução

Siga estes passos para configurar e rodar a aplicação e sua API localmente.

#### a. Pré-requisitos
-   Python 3.x
-   Git

#### b. Configuração do Ambiente
```bash
# 1. Clone este repositório
git clone https://github.com/Yuridevpro/api_friend_for_life.git

# 2. Crie e ative o ambiente virtual
# No macOS/Linux:
python3 -m venv venv
source venv/bin/activate
# No Windows:
python -m venv venv
venv\Scripts\activate

# 3. Instale as dependências do projeto
entre na pasta do projeto
cd api_friend_for_life
Entre na pasta do código-fonte
cd src

pip install -r requirements.txt
```



#### c. Banco de Dados e Execução
**IMPORTANTE:** Todos os comandos a seguir devem ser executados de dentro da pasta `src/`.

```bash

# 4. Crie as migracoes
python manage.py makemigrations

# 5. Crie o banco de dados SQLite e suas tabelas
python manage.py migrate

# 6. Popule o banco de dados com usuários e pets de teste
python manage.py seed_data

# 9. Inicie o servidor de desenvolvimento para testar
python manage.py runserver
```
A aplicação e sua API estarão disponíveis em **http://127.0.0.1:8000**.

---

### 4. Testando a API

#### a. Testes Unitários Automatizados
Com o ambiente configurado, você pode rodar a suíte de testes unitários.

```bash
# Certifique-se de que você está dentro da pasta src/
python manage.py test
```
**Resultado esperado:** Todos os testes (`4 testes`) devem passar com o status `OK`.

#### b. Verificação Rápida via Navegador
A API desenvolvida com Django REST Framework oferece uma interface navegável para desenvolvimento. **Com o servidor rodando**(python manage.py runserver
), use seu navegador para inspecionar os endpoints:

1.  **Listar todos os pets:**
    *   Acesse: [http://127.0.0.1:8000/api/pets/](http://127.0.0.1:8000/api/pets/)
    *   **Resultado esperado:** Uma página do DRF exibindo uma lista dos pets de teste em formato JSON.

2.  **Ver detalhes de um pet específico:**
    *   Acesse: [http://127.0.0.1:8000/api/pets/1/](http://127.0.0.1:8000/api/pets/1/)
    *   **Resultado esperado:** Uma página do DRF exibindo os dados em JSON do pet com `id=1`.

#### c. Teste Completo via Postman/Insomnia
Para simular um cliente de API externo, utilize a coleção fornecida:

1.  Com o servidor ainda rodando, abra o Postman ou Insomnia.
2.  Importe a coleção de testes localizada em: `/postman/collection.json`.
3.  Execute as requisições `Listar todos os pets`, `Obter detalhes de um pet` e `Registrar interesse em um pet`.
4.  **Resultado esperado:** As requisições devem retornar um status `200 OK` para GET e `201 Created`  para POST.


#### d. Demonstração Prática da Integração (Site Externo)
Para validar a integração de ponta a ponta e ver a API em ação, foi criada uma página de demonstração que simula um sistema externo consumindo os dados.

1.  **Certifique-se de que o servidor Django está rodando.** (`python manage.py runserver`)
2.  **Acesse a seguinte URL no seu navegador:**
    *   [http://127.0.0.1:8000/pagina_inicio/cliente-externo/](http://127.0.0.1:8000/pagina_inicio/cliente-externo/)
3.  **Resultado esperado:** Você verá uma página estilizada como o "Site da ONG Parceira", exibindo os cards dos pets que foram carregados dinamicamente através de uma chamada JavaScript à sua API. Ao clicar no botão "Tenho Interesse!", um modal com os contatos do protetor será exibido.

---

### 5. Documentação das Rotas da API (Swagger/OpenAPI)

A documentação completa e interativa da API, gerada automaticamente, está disponível nos seguintes endpoints enquanto o servidor estiver rodando:

-   **Swagger UI (Recomendado):** [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)
-   **ReDoc:** [http://127.0.0.1:8000/api/schema/redoc/](http://127.0.0.1:8000/api/schema/redoc/)

#### Endpoints Implementados
| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/pets/` | Retorna uma lista de todos os pets ativos e disponíveis para adoção, incluindo um **objeto aninhado com as informações públicas de seu respectivo protetor** (nome, contato). |
| `GET` | `/api/pets/{id}/` | Retorna os detalhes completos de um pet específico, consultado pelo seu ID, incluindo o **objeto aninhado com os dados do protetor**. |

---

### 6. Estrutura do Repositório e Arquivos Relevantes

A estrutura do projeto foi organizada para isolar o código-fonte (`src/`) dos artefatos de teste e documentação, conforme solicitado.

```
├── 📄 README.md                # Documentação principal e guia de execução
├── 📂 src/                      # Código-fonte principal da aplicação Django
│   ├── ⚙️ adote/
│   │   ├── settings.py        # Configurações do projeto
│   │   └── urls.py            # Roteador principal de URLs (inclui as rotas da API)
│   ├── 🐶 divulgar/
│   │   ├── models.py          # Define o modelo 'Pet'
│   │   ├── serializers.py     # "Traduz" o modelo 'Pet' para JSON
│   │   ├── tests.py           # Testes unitários para os endpoints da API
│   │   └── views.py           # Contém a lógica dos endpoints da API
│   └── ... (outros apps que fornecem modelos, como 'perfil')
├── 📂 docs/                     # Documentação adicional
│   └── architecture.md        # Detalhes da arquitetura da API
└── 📂 postman/                  # Coleção do Postman para testes manuais
    └── collection.json        # Arquivo de coleção exportado
```

#### Descrição dos Arquivos Participantes

*   **`src/adote/settings.py`**: Configuração principal do Django, ajustada para rodar 100% localmente.
*   **`src/adote/urls.py`**: Roteador principal que define as rotas da API e da documentação Swagger.
*   **`src/divulgar/models.py`**: Define o modelo `Pet`, a estrutura de dados principal exposta pela API.
*   **`src/divulgar/serializers.py`**: Contém o `PetSerializer`, responsável por converter os dados do modelo `Pet` para JSON.
*   **`src/divulgar/views.py`**: Contém as classes `PetListAPIView` e `PetDetailAPIView`, que são a lógica dos endpoints da API.
*   **`src/divulgar/tests.py`**: Contém os testes unitários automatizados para os endpoints.
*   **`docs/architecture.md`**: Detalha a arquitetura da camada da API.
*   **`postman/collection.json`**: Arquivo exportado do Postman com as requisições prontas para testar a API.

---

### 7. Equipe
- **Nome do Integrante 1:** [Matrícula]
- **Nome do Integrante 2:** [Matrícula]
- **Nome do Integrante 3:** [Matrícula]
- **Nome do Integrante 4:** [Matrícula]
```
