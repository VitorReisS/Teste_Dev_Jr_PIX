# API de Agendamentos de Pagamento

Esta API foi desenvolvida utilizando **Python** e **Django** para gerenciar agendamentos de pagamentos. A API permite a criação, listagem, consulta, exclusão e atualizar agendamentos de pagamentos. O projeto utiliza o banco de dados SQLite (padrão do Django) e retorna os dados no formato JSON.

## Funcionalidades
- **Criar Agendamento de Pagamento**: Permite o agendamento de pagamentos futuros com suporte para recorrência.
- **Listar Todos os Agendamentos**: Exibe todos os agendamentos registrados no sistema.
- **Consultar Agendamento Específico**: Retorna os detalhes de um agendamento específico.
- **Excluir Agendamento**: Remove um agendamento específico do banco de dados.
- **Editar Agendamento**: Atualiza um agendamento específico do banco de dados.

## Requisitos

- **Python** 3.8+
- **Django** 5.1.1
- **Django Rest Framework** 3.14+
- **SQLite** (banco de dados padrão do Django)

## Instalação

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. Crie e ative um ambiente virtual (recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate  # Para Windows
   ```

3. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

4. Rode as migrações para criar as tabelas no banco de dados SQLite:

   ```bash
   python manage.py migrate
   ```

5. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

Agora, a API estará disponível em `http://127.0.0.1:8000/`.

## Endpoints

### 1. Criar Agendamento de Pagamento

- **URL**: `/api/agendamentos/criar/`
- **Método**: `POST`

- **Exemplo de cURL**
  ```bash
    curl --location 'http://127.0.0.1:8000/api/agendamentos/criar/' \
    --header 'Content-Type: application/json' \
    --data '  {
    "data_pagamento": "2024-09-13",
    "permite_recorrencia": true,
    "quantidade_recorrencia": 5,
    "intervalo_recorrencia": 30,
    "status_recorrencia": "ativo",
    "agencia": 1234,
    "conta": 5678,
    "valor_pagamento": 100.50
    }'
  ```

- **Exemplo de Requisição**:

  ```json
  {
  "data_pagamento": "2024-09-14",
  "permite_recorrencia": true,
  "quantidade_recorrencia": 5,
  "intervalo_recorrencia": 30,
  "status_recorrencia": "ativo",
  "agencia": 1234,
  "conta": 5678,
  "valor_pagamento": 100.50
  }
  ```

- **Exemplo de Resposta**:

  ```json
  {
    "id": 1,
    "valor_pagamento": "10050.00",
    "data_pagamento": "2024-09-14",
    "permite_recorrencia": true,
    "quantidade_recorrencia": 5,
    "intervalo_recorrencia": 30,
    "status_recorrencia": "ativo",
    "agencia": 1234,
    "conta": 5678
  }
  ```

### 2. Listar Todos os Agendamentos

- **URL**: `/api/agendamentos/`
- **Método**: `GET`

- **Exemplo de cURL**
  ```bash
    curl --location "http://127.0.0.1:8000/api/agendamentos/"
  ```

- **Exemplo de Resposta**:

  ```json
  [
    {
        "id": 1,
        "valor_pagamento": "10050.00",
        "data_pagamento": "2024-09-13",
        "permite_recorrencia": true,
        "quantidade_recorrencia": 5,
        "intervalo_recorrencia": 30,
        "status_recorrencia": "ativo",
        "agencia": 1234,
        "conta": 5678
    },
    {
        "id": 2,
        "valor_pagamento": "10000.00",
        "data_pagamento": "2024-09-13",
        "permite_recorrencia": false,
        "quantidade_recorrencia": 5,
        "intervalo_recorrencia": 15,
        "status_recorrencia": "ativo",
        "agencia": 12345,
        "conta": 678910
    }
  ]
  ```

### 3. Consultar Agendamento Específico

- **URL**: `/api/agendamentos/<id>/`
- **Método**: `GET`

- **Exemplo de cURL**
  ```bash
    curl --location "http://127.0.0.1:8000/api/agendamentos/1/"
  ```

- **Exemplo de Resposta** (para `/api/agendamentos/1/`):

  ```json
  {
    "id": 1,
    "valor_pagamento": "10050.00",
    "data_pagamento": "2024-09-13",
    "permite_recorrencia": true,
    "quantidade_recorrencia": 5,
    "intervalo_recorrencia": 30,
    "status_recorrencia": "ativo",
    "agencia": 1234,
    "conta": 5678
  }
  ```

### 4. Excluir Agendamento

- **URL**: `/api/agendamentos/<id>/deletar`
- **Método**: `DELETE`

  ```bash
    curl --location --request DELETE 'http://127.0.0.1:8000/api/agendamentos/1/deletar'
  ```

- **Exemplo de Requisição** (para `/api/agendamentos/1/deletar/`):

  ```bash
  DELETE /api/agendamentos/1/deletar/
  ```

- **Resposta**:
  - Código de resposta: `204 No Content` (sem corpo)

### 5. Editar Agendamento

- **URL**: `/api/agendamentos/<id>/atualizar/`
- **Método**: `PATCH`

- **Exemplo de cURL**
  ```bash
    curl --location --request PATCH 'http://127.0.0.1:8000/api/agendamentos/2/atualizar' \
    --header 'Content-Type: application/json' \
    --data ' {
          "id": 2,
          "valor_pagamento": "10000.00",
          "data_pagamento": "2024-09-13",
          "permite_recorrencia": true,
          "quantidade_recorrencia": 5,
          "intervalo_recorrencia": 15,
          "status_recorrencia": "ativo",
          "agencia": 12345,
          "conta": 678910
      }'
  ```

- **Exemplo de Requisição**:

  ```json
  {
  "data_pagamento": "2024-09-13",
  "permite_recorrencia": true,
  "quantidade_recorrencia": 5,
  "intervalo_recorrencia": 30,
  "status_recorrencia": "ativo",
  "agencia": 1234,
  "conta": 5678,
  "valor_pagamento": 100.50
  }
  ```

- **Exemplo de Resposta**:

  ```json
  {
    "id": 1,
    "valor_pagamento": "10050.00",
    "data_pagamento": "2024-09-13",
    "permite_recorrencia": true,
    "quantidade_recorrencia": 5,
    "intervalo_recorrencia": 30,
    "status_recorrencia": "ativo",
    "agencia": 1234,
    "conta": 5678
  }
  ```

## Estrutura do Projeto

- **pagamentos**: Diretório principal do projeto Django.
- **agendamentos/**: Aplicativo que gerencia os agendamentos de pagamento.
- **agendamentos/models.py**: Definição do modelo de dados.
- **agendamentos/views.py**: Lógica das views da API.
- **agendamentos/serializers.py**: Serializadores para converter dados em JSON.
- **agendamentos/urls.py**: Definição das rotas da API.

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.