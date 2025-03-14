# Reservas de Restaurante - FastAPI
Este projeto é uma aplicação backend construída com **FastAPI**, **Jinja2** e **Uvicorn** para gerenciar um sistema de agendamento de quadras. O sistema permite o cadastro, listagem, edição e exclusão de quadras esportivas, além da exibição desses dados de forma dinâmica utilizando templates HTML renderizados com Jinja2.

A interface web apresenta uma tabela interativa para visualizar as quadras cadastradas, com botões para edição e exclusão, além de um formulário intuitivo para adicionar ou atualizar informações sobre as quadras.

**Author: Iasmin Azevedo** 

## Telas:

![Tela inicial](inicio.png)  
![Reservas](reservas.png)  

## Requisitos

Antes de rodar o projeto, você precisa ter o seguinte instalado na sua máquina:

- **Python 3.8+**
- **pip** (gerenciador de pacotes do Python)
- **uvicorn**

## Passos para instalação

### 1. Clone o repositório

Primeiro, clone o repositório para sua máquina local:

```bash
    git clone https://github.com/Iasmin-Azevedo/ReservaDeRestaurante.git
    cd ReservaDeRestaurante
```

### 2. Crie e ative um ambiente virtual

```bash
    python -m venv venv
    venv\Scripts\activate
```

### 3. Instale as dependências
Instale as dependências necessárias listadas no requirements.txt:

```bash
    pip install -r requirements.txt
```

### 6. Rode a aplicação
Agora que o ambiente está configurado e o banco de dados está pronto, você pode rodar o servidor Uvicorn para iniciar a API FastAPI:

```bash
    uvicorn main:app --reload
```
O servidor estará rodando em http://127.0.0.1:8000.

### 7. Teste a API
Abra o navegador e vá para http://127.0.0.1:8000/docs para acessar a documentação interativa da API gerada automaticamente pelo FastAPI. Lá você poderá testar as rotas da sua API, como cadastro de alunos, criação de provas, etc.

Estrutura do Projeto

```plaintext
project_name/
├── controllers/        # Controladores de API
│   ├── agendamento_controller.py
│   ├── quadra_controller.py
├── dao/                # Funções para interação com o banco de dados
│   ├── agendamento_dao.py
│   ├── quadra_dao.py
├── data/                # banco de dados json
│   ├── agendamentos.json
│   ├── quadras.json
├── models/             # Modelos para o banco de dados
│   ├── agendamento.py
│   ├── quadra.py
├── schemas/             # schema
│   ├── agendamento_schema.py
├── services/           # Lógica de negócios
│   ├── agendamento_service.py
│   ├── quadra_service.py
├── ArenaFast.postman_collection.json        # Arquivo da coleção FastAPI
├── main.py             # Arquivo principal para rodar o servidor FastAPI
├── requirements.txt             # Arquivo de requerimentos do sistema
├── README.md           # Documentação do projeto
```