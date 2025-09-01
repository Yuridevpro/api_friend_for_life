# Arquitetura da API - A Friend for Life

Este documento descreve a arquitetura da camada de API construída sobre a aplicação web "A Friend for Life", detalhando seus componentes, o fluxo de comunicação e os protocolos utilizados, conforme os requisitos da disciplina de Técnicas de Integração de Sistemas.

### **Arquivo `docs/architecture.md` (Versão Final com Arquitetura em Camadas)**

# Arquitetura da API - A Friend for Life

Este documento descreve a arquitetura da camada de API construída sobre a aplicação web "A Friend for Life", detalhando seus componentes e o fluxo de comunicação em um modelo de camadas.

### 1. Visão Geral

A API foi desenvolvida utilizando o **Django REST Framework (DRF)** sobre a aplicação Django existente. A arquitetura segue um padrão em camadas, separando as responsabilidades de apresentação, negócio e dados, e integrando-se com serviços externos para enriquecer a funcionalidade.

### 2. Arquitetura em Camadas

O diagrama a seguir apresenta a arquitetura em camadas do sistema, ilustrando a interação entre os componentes internos e os serviços externos consumidos.

```mermaid
graph TD
    subgraph "Cliente da API (Sistema Externo)"
        direction LR
        Client[Postman / Browser<br>(cliente_api_externo.html)]
    end

    subgraph "API 'A Friend for Life' (Sistema Principal)"
        direction LR
        
        subgraph "Camada de Apresentação"
            A[URLs<br>(urls.py)] --> B[API Views<br>(views.py)];
        end

        subgraph "Camada de Negócio"
            B --> C[Serviços de Integração];
            C -- "Busca/Valida Dados" --> D[Serializers<br>(serializers.py)];
        end

        subgraph "Camada de Dados"
            D -- "Interage com" --> E[Models<br>(models.py)];
            E -- ORM --> F[("Banco de Dados<br>SQLite")];
            C -- "Consome" --> G[Cliente HTTP<br>(requests)];
        end
    end

    subgraph "APIs Externas (Serviços Consumidos)"
        direction LR
        G --> H[API do IBGE];
        G --> I[API DiceBear Avatars];
    end

    Client -- "Requisição HTTP/JSON" --> A;

    style Client fill:#cde,stroke:#333,stroke-width:2px
```

### 3. Explicação da Arquitetura em Camadas

*   **Camada de Apresentação:**
    *   **URLs (`urls.py`):** Define os endpoints da API (ex: `/api/localidades/estados/`). É a porta de entrada para todas as requisições. Funciona como as "Routes" do exemplo.
    *   **API Views (`views.py`):** Recebe a requisição da URL e orquestra a resposta. Funciona como os "Controllers".

*   **Camada de Negócio:**
    *   **Serviços de Integração:** Representa a lógica dentro das nossas `API Views` que decide quais APIs externas chamar e como processar os dados. No nosso caso, é o código que chama o `requests.get(...)` para o IBGE.
    *   **Serializers (`serializers.py`):** Responsáveis por validar dados de entrada (se houvesse `POST`) e, principalmente, por transformar os objetos complexos dos modelos Django em formato JSON para a resposta.

*   **Camada de Dados:**
    *   **Models (`models.py`):** Define a estrutura dos nossos dados (`Pet`, `UserProfile`) e como eles se relacionam. Também contém lógica de negócio ligada aos dados, como o método `get_avatar()`.
    *   **Cliente HTTP (`requests`):** Componente responsável por realizar a comunicação de saída com as APIs externas.
    *   **Banco de Dados (SQLite):** A camada final de persistência onde os dados da aplicação são armazenados.

*   **APIs Externas:**
    *   **API do IBGE:** Fonte externa de dados geográficos (estados e cidades).
    *   **API DiceBear Avatars:** Fonte externa para a geração de imagens de avatares.



### 4. Tratamento de Erros

O Django REST Framework fornece um tratamento de erros padronizado e informativo, essencial para a integração de sistemas:

*   **`404 Not Found`:** É retornado quando uma requisição é feita para um recurso específico que não existe (ex: `GET /api/pets/999/` onde o pet com ID 999 não está no banco de dados).
*   **`400 Bad Request`:** Seria retornado caso a API tivesse endpoints `POST` ou `PUT` e os dados enviados pelo cliente fossem inválidos ou estivessem incompletos.
*   **`500 Internal Server Error`:** É retornado em caso de falhas inesperadas no servidor durante o processamento da requisição, impedindo que a operação seja concluída.

