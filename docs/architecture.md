# Arquitetura da API - A Friend for Life

Este documento descreve a arquitetura da camada de API construída sobre a aplicação web "A Friend for Life", detalhando seus componentes, o fluxo de comunicação e os protocolos utilizados, conforme os requisitos da disciplina de Técnicas de Integração de Sistemas.

### 1. Visão Geral da Arquitetura da API

A API foi desenvolvida utilizando o **Django REST Framework (DRF)**, uma extensão robusta e flexível do framework Django. Ela foi projetada para operar sobre a arquitetura monolítica existente da aplicação, adicionando uma camada de serviço que expõe os modelos de dados através de endpoints RESTful.

Esta abordagem permite que a lógica de negócios e as regras já implementadas na aplicação principal sejam reutilizadas, garantindo consistência, enquanto se oferece uma interface padronizada para a integração com sistemas externos. A comunicação segue o protocolo **REST/HTTP**, utilizando os métodos HTTP padrão (`GET`) e o formato de dados **JSON** para a serialização.

### 2. Diagrama da Arquitetura de Integração

O diagrama a seguir ilustra como um sistema externo (Cliente da API) se integra com a aplicação Django através da camada de API.

```mermaid
graph TD
    A["Cliente da API<br>(Postman, Script, App)"] -- HTTP/JSON --> B("Servidor de Desenvolvimento Django");
    
    subgraph "Aplicação Django (Sistema 1)"
        B -- Roteamento --> C["API Views<br>(views.py)"];
        C -- Busca Dados --> D["Models Django<br>(models.py)"];
        D -- ORM --> E[("Banco de Dados<br>SQLite")];
        C -- Serialização --> F["Serializers<br>(serializers.py)"];
    end

    style B fill:#bbf,stroke:#333,stroke-width:2px

**Fluxo da Requisição da API (Ambiente Local):**
1.  Um **Cliente da API** (A), como o Postman, envia uma requisição HTTP (ex: `GET /api/pets/`) para o **Servidor de Desenvolvimento Django** (B), que está rodando localmente.
2.  O servidor, através do seu roteador de URLs, direciona a requisição para a **API View** (C) correspondente (ex: `PetListAPIView`).
3.  A API View utiliza os **Models Django** (D) e o ORM para buscar os dados necessários no banco de dados **SQLite** (E).
4.  Os objetos do Django retornados da consulta são passados para os **Serializers** (F), que os convertem para o formato JSON.
5.  A API View retorna a resposta em JSON para o Cliente da API (A).

### 3. Protocolos de Comunicação

*   **Protocolo Principal:** HTTP/1.1 (conforme executado pelo servidor de desenvolvimento do Django).
*   **Formato de Dados:** JSON.
*   **Protocolo de Interação:** REST (Representational State Transfer), utilizando verbos HTTP (`GET`) para interagir com os recursos (`/api/pets/`).

### 4. Tratamento de Erros

O Django REST Framework fornece um tratamento de erros padronizado e informativo, essencial para a integração de sistemas:

*   **`404 Not Found`:** É retornado quando uma requisição é feita para um recurso específico que não existe (ex: `GET /api/pets/999/` onde o pet com ID 999 não está no banco de dados).
*   **`400 Bad Request`:** Seria retornado caso a API tivesse endpoints `POST` ou `PUT` e os dados enviados pelo cliente fossem inválidos ou estivessem incompletos.
*   **`500 Internal Server Error`:** É retornado em caso de falhas inesperadas no servidor durante o processamento da requisição, impedindo que a operação seja concluída.
```
