# Projeto de API para Integração de Sistemas (N703)
## API da Plataforma de Adoção "A Friend for Life"

Este repositório contém o código-fonte e a documentação de uma API de serviços desenvolvida para a plataforma "A Friend for Life". O objetivo é demonstrar a criação de uma API própria que atua como um orquestrador, consumindo APIs externas para fornecer funcionalidades enriquecidas.

![Status](https://img.shields.io/badge/Status-API%20Funcional-brightgreen) ![Python](https://img.shields.io/badge/Python-3.x-blue) ![Django](https://img.shields.io/badge/Django-4.x-darkgreen) ![DRF](https://img.shields.io/badge/DRF-3.x-red)

 ### **Relação com os Objetivos de Desenvolvimento Sustentável (ODS)**

Este projeto contribui diretamente para o **ODS 11: Cidades e Comunidades Sustentáveis**, especificamente na meta de tornar as cidades mais inclusivas, seguras, resilientes e sustentáveis. Ao facilitar a adoção de animais de rua, a plataforma "A Friend for Life" ajuda a gerenciar a população de animais abandonados, o que é um desafio para a saúde pública e o bem-estar em ambientes urbanos. Uma comunidade que cuida de seus animais é uma comunidade mais humana, coesa e engajada, fortalecendo os laços sociais e promovendo um ambiente urbano mais seguro e acolhedor para todos os seus habitantes.

### 1. Objetivo do Trabalho

O objetivo é desenvolver uma API que, para funcionar, consome pelo menos duas APIs externas distintas, demonstrando conceitos de integração e orquestração de serviços.
-   **API Própria:** Atua como um Backend for Frontend (BFF), oferecendo endpoints de serviço.
-   **APIs Externas Consumidas:**
    1.  **IBGE:** Para fornecer dados de geolocalização (estados e cidades).
    2.  **DiceBear:** Para gerar avatares de perfil únicos.

### 2. Descrição Funcional da Solução

A API fornece dois conjuntos de serviços:
1.  **Serviço de Localidades:** Oferece endpoints que buscam e retornam a lista de estados e cidades do Brasil, consumindo a API do IBGE e adicionando uma camada de cache para otimização.
2.  **Serviço de Avatares:** Oferece um endpoint que gera uma URL de avatar única com base em um e-mail, consumindo a API da DiceBear.

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

# 9. Inicie o servidor de desenvolvimento para testar
python manage.py runserver
```
A aplicação e sua API estarão disponíveis em **http://127.0.0.1:8000**.

---

### 4. Guia de Criacao do usuario


#### **Opção 1: Cadastro Manual (Recomendado para Testar a Aplicação Web)**

Se você deseja testar a experiência completa da aplicação web (cadastro, login, etc.), siga o guia de uso detalhado.

1.  **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```
2.  **Siga o Guia de Uso:** Acesse o documento [`/docs/GUIA_DE_USO.md`](./docs/GUIA_DE_USO.md) para um passo a passo detalhado sobre como criar uma conta, ativar via terminal e usar todas as funcionalidades do site.

---

#### **Opção 2: Criação Automática de Usuário (Recomendado para Testar a API Rapidamente)**

Se o seu objetivo é apenas validar rapidamente os endpoints da API com o Postman ou no navegador, use este comando para criar um usuário de teste instantaneamente.

1.  **Execute o comando de seed (ainda dentro da pasta `src/`):**
    ```bash
    python manage.py seed_data
    ```
2.  **Inicie o servidor:**
    ```bash
    python manage.py runserver
    ```
*   Este comando cria o usuário de teste `teste@email.com`, que pode ser usado para testar o endpoint da API de avatares.

---



### 5. Testando a API

#### a. Testes Unitários Automatizados
```bash
# Na pasta src/, execute:
python manage.py test
```
**Resultado esperado:** Todos os testes devem passar com `OK`.

#### b. Teste Manual via Navegador
Com o servidor rodando, você pode verificar os endpoints no navegador:

1.  **Listar todos os estados:**
    *   Acesse: [http://127.0.0.1:8000/api/localidades/estados/](http://127.0.0.1:8000/api/localidades/estados/)

2.  **Gerar um avatar:**
    *   Acesse: [http://127.0.0.1:8000/api/avatar/exemplo@email.com/](http://127.0.0.1:8000/api/avatar/exemplo@email.com/)

#### c. Teste Completo via Postman/Insomnia
Para simular um cliente de API externo e validar os endpoints de forma mais robusta, utilize a coleção fornecida.

1.  Com o servidor ainda rodando, abra o Postman ou Insomnia.
2.  Importe a coleção de testes localizada em: `/postman/collection.json`.
3.  A coleção conterá requisições pré-configuradas para todos os endpoints, como `Listar Estados`, `Listar Cidades de um Estado` e `Gerar Avatar`.
4.  Execute as requisições para verificar o funcionamento. A resposta esperada é um status `200 OK` com os respectivos dados em JSON.


---

### 6. Documentação das Rotas da API (Swagger/OpenAPI)

A documentação interativa da API está disponível no seguinte endpoint:

-   **Swagger UI:** [http://127.0.0.1:8000/api/schema/swagger-ui/](http://127.0.0.1:8000/api/schema/swagger-ui/)

#### Endpoints Implementados
| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/api/localidades/estados/` | Retorna a lista de estados do Brasil (consome IBGE). |
| `GET` | `/api/localidades/estados/{id}/cidades/` | Retorna a lista de cidades de um estado (consome IBGE).|
| `GET` | `/api/avatar/{email}/` | Retorna a URL de um avatar gerado (consome DiceBear). |

---

### 7. Estrutura do Repositório e Arquivos Relevantes

A estrutura do projeto foi organizada para isolar o código-fonte (`src/`) dos artefatos de teste e documentação, conforme solicitado na proposta de trabalho.

```
/
├── 📄 README.md                # Guia principal com instruções de execução
├── 📜 requirements.txt         # Lista de dependências Python
├── 🔑 .env.example              # Modelo para o arquivo de variáveis de ambiente
├── 📂 src/                      # Código-fonte principal da aplicação Django
│   ├── ⚙️ adote/
│   │   ├── settings.py        # Configurações do projeto
│   │   └── urls.py            # Roteador principal de URLs (incluindo as rotas da API)
│   ├── 👤 perfil/
│   │   └── views.py           # Contém a view da API de Avatares
│   └── 📱 usuarios/
│   │   │   📂management/
│   │   │    └── commands/
│   │   │        └── seed_data.py # Script para popular o banco de dados
│   │   ├── tests.py  # Contém os testes unitários da API
│   │   └── views.py  # Contém as views da API de Localidades
├── 📂 docs/  # Documentação adicional
│   ├── 📄 architecture.md  # Detalhes da arquitetura da API
│   └── 📄 GUIA_DE_USO.md   # Guia para teste manual da aplicação web
├── 📂 tests/   # Pasta de testes (conforme solicitado)
│   └── 📄 instrucao.txt  # Nota explicando a localização dos testes
└── 📂 postman/ # Coleção do Postman para testes manuais
    └── 📄 collection.json  # Arquivo de coleção exportado
```

#### 8. Descrição dos Arquivos Participantes

*   **`src/adote/urls.py`**
    *   **Descrição:** Roteador de URLs principal do projeto. É aqui que são definidas as rotas para as APIs que criamos (`/api/localidades/` e `/api/avatar/`) e também as rotas para a documentação interativa (Swagger UI).

*   **`src/usuarios/mannagement/commands/seed_data.py`**
    *   **Descrição:** Comando de gerenciamento customizado do Django. Sua função é popular o banco de dados com um usuário de teste, facilitando a avaliação da API e da aplicação web.

*   **`src/perfil/models.py`**
    *   **Descrição:** Contém o modelo `UserProfile`, que foi aprimorado com o método `get_avatar()` para consumir a API da DiceBear e gerar uma URL de avatar.

*   **`src/perfil/views.py`**
    *   **Descrição:** Contém a view `AvatarAPIView`, que implementa o endpoint `/api/avatar/<email>/` e consome a API da DiceBear.

*   **`src/usuarios/views.py`**
    *   **Descrição:** Contém as views `EstadoListAPIView` e `CidadeListAPIView`, que implementam os endpoints `/api/localidades/...` e consomem a API do IBGE, adicionando uma camada de cache.

*   **`src/usuarios/tests.py`**
    *   **Descrição:** Contém os testes unitários automatizados para os endpoints da API (`/api/localidades/` e `/api/avatar/`), garantindo seu funcionamento correto e tratando casos de sucesso e erro.

*   **`docs/architecture.md`**
    *   **Descrição:** Documento técnico que detalha a arquitetura da camada da API, com um diagrama de fluxo e a explicação dos componentes e protocolos de comunicação.

*   **`postman/collection.json`**
    *   **Descrição:** Arquivo de coleção exportado do Postman. Contém requisições pré-configuradas para todos os endpoints da API, permitindo que o avaliador teste a integração de forma rápida e padronizada.

---

### 9. Equipe e Papéis

| Nome | Papel |
| :--- | :--- |
| José Alves Ferreira Neto | Product Owner / Gestão |
| Alan Magalhães Barros | Scrum Master |
| Alisson Rafael Silva de Almeida | Time (Desenvolvimento) |
| Yuri da Silva Ferreira | Time (Desenvolvimento) |
| Kairo César Ferreira Cunha | Time (Desenvolvimento / Testes) |
| Gabriel Nogueira Ibiapina | UX / Documentação |
```
