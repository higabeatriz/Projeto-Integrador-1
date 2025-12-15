# 💊 API Projeto Django - Gestão de Intervenções Farmacêuticas

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue.svg?logo=python)](https://www.python.org/downloads/)
[![Django](https://img.shields.io/badge/Django-5.0%2B-green.svg?logo=Django)](https://www.djangoproject.com/)
[![SQLite](https://img.shields.io/badge/SQLite-003B57.svg?logo=sqlite&logoColor=white)](https://www.sqlite.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Sumário

- [Visão Geral](#visão-geral)
- [Funcionalidades e Benefícios](#funcionalidades-e-benefícios)
- [Pacotes Utilizados](#pacotes-utilizados)
- [Estrutura do Projeto](#estrutura-do-projeto)
- [Diagrama de Banco de Dados](#diagrama-de-banco-de-dados)
- [Documentação da API](#documentação-da-api)
- [Configuração do Ambiente](#configuração-do-ambiente)
- [Autenticação (Autenticação de Token)](#Autenticação-Autenticação-de-Token)
- [Guia de Acesso Rápido](#Guia-de-Acesso-Rápido)


## Visão Geral

Esta API foi desenvolvida para apoiar o fluxo de trabalho hospitalar através da **Intervenção Farmacêutica**. O sistema permite que os profissionais da farmácia clínica registrem problemas relacionados à farmacoterapia e documentem condutas propostas para a equipe multidisciplinar. O objetivo central é aumentar a segurança do paciente e promover o uso racional de medicamentos.

A **Intervenção Farmacêutica** é o ato de identificar, prevenir e resolver Problemas Relacionados aos Medicamentos (PRMs), propondo uma conduta para otimizar o tratamento do paciente.

📝 A Importância da Ficha de Intervenção Digital

O sistema transforma o registro manual da intervenção em uma ficha digital estruturada, auditável e de fácil consulta. Essa digitalização é fundamental porque:

**Melhora a Segurança:** Reduz erros relacionados aos medicamentos (PRMs) e formaliza sugestões de conduta, assegurando que a sugestão chegue à equipe multidisciplinar de forma clara e registrada.

**Garante a Rastreabilidade:** Cada registro é uma "impressão digital" do processo, vinculando o evento ao Farmacêutico (responsável), ao Paciente e ao Desfecho da Intervenção (se foi aceita ou não pela equipe médica).

**Gera Indicadores de Qualidade:** A coleta estruturada de dados permite calcular a Taxa de Aceitação de Intervenções, um KPI crucial para medir a contribuição do serviço de Farmácia Clínica e justificar sua importância estratégica no hospital.

## Funcionalidades e Benefícios

| Módulo | Funcionalidade | Benefícios |
| :--- | :--- | :--- |
|📝 **Intervenção** | Registro completo da ocorrência, conduta, e desfecho (`Aceita`, `Não Aceita`). | **Rastreabilidade e Auditoria** de decisões. |
|🧑‍⚕️ **Perfil Paciente** | Cadastro de prontuário, leito e alergias. | **Contextualização** da intervenção e segurança. |
|💊 **Catálogo** | Gestão de medicamentos. | **Padronização** dos dados farmacêuticos. |
|🔐 **Autenticação** | Acesso protegido via Token Authentication. | **Segurança** e garantia de que o responsável é registrado. |

## Pacotes Utilizados

O projeto utiliza um ambiente virtual padrão (`venv`) e `requirements.txt`.

| Tecnologia | Versão | Descrição |
|---|---|---|
| Python | 3.12+ | Linguagem principal de desenvolvimento. |
| Django | >=5.0 | Framework base do projeto. |
| Django REST Framework | latest | Toolkit para construção de APIs RESTful. |
| **drf-spectacular** | latest | Geração de documentação interativa OpenAPI (Swagger). |
| python-dotenv | latest | Gerenciamento de variáveis de ambiente. |
| gunicorn | latest | Servidor WSGI recomendado para produção. |

## Estrutura do Projeto

```
PROJETO_FARMA/
├── manage.py              # Script padrão do Django para executar comandos.
├── requirements.txt       # Lista de dependências Python necessárias para rodar o projeto.
├── db.sqlite3             # Arquivo do banco de dados SQLite padrão do projeto.
├── .env.example           # Modelo para variáveis de ambiente (chaves secretas, configurações).
├── .gitignore             # Arquivo que define quais arquivos o Git deve ignorar (ex: db.sqlite3, venv/).
├── README.md              # Documentação principal do projeto.
│
├── core/                  # App Principal (Lógica de Negócio da Farmácia Clínica)
│   ├── migrations/        # Histórico de alterações do esquema do banco de dados.
│   ├── admin.py           # Configuração para gerenciar modelos no Painel Administrativo.
│   ├── apps.py            # Configurações específicas do app 'core'.
│   ├── models.py          # Definição das Entidades do banco de dados (Intervencao, Paciente, Medicamento).
│   ├── permissions.py     # Controle de Acesso (Define quem pode acessar rotas protegidas - Token).
│   ├── serializers.py     # Serialização/Desserialização de dados (Traduz Python para JSON).
│   ├── tests.py           # Arquivo para escrever e rodar testes automatizados da lógica da API.
│   └── views.py           # Lógica da API (ViewSets que definem as respostas às requisições CRUD).
│
├── config/                # Configurações Globais
│   ├── settings.py        # Configurações principais do projeto (apps instalados, banco de dados, chaves).
│   ├── urls.py            # Roteamento principal (Define as rotas do admin, api/ e documentação).
│   ├── wsgi.py            # Ponto de entrada WSGI para servidores de produção (Síncronos).
│   └── asgi.py            # Ponto de entrada ASGI para servidores que suportam tráfego Assíncrono (WebSockets).
│
└── venv/                  # Ambiente Virtual Isolado (Contém as bibliotecas instaladas).
```

## Diagrama de Banco de Dados

<img width="1078" height="846" alt="Image" src="https://github.com/user-attachments/assets/957da151-8fbe-45ee-b2a8-96fed895d801" />

> **Descrição:** Diagrama ER (Entidade-Relacionamento).

## Documentação da API

A documentação interativa está disponível em `/api/docs/` (Swagger UI) ou `/api/redoc/` (ReDoc) no ambiente de desenvolvimento.

### Endpoints Principais

| Método | Endpoint              | Descrição                          | Autenticação |
|--------|-----------------------|------------------------------------|--------------|
| GET    | `/api/intervencoes/`  |Recupera o histórico de intervenções| Requerida    |
| POST   | `/api/intervencoes/`  |Registra nova conduta farmacêutica  | Requerida    |
| GET    | `/api/pacientes/`     |Lista perfis clínicos               | Requerida    |
| GET    | `/api/medicamentos/`  |Lista medicamentos cadastrados      | Opcional     |

> **Detalhes:** Consulte a interface Swagger para schemas de request/response, parâmetros e exemplos.

## 🔐 Autenticação (Token Authentication) 

Para acessar os endpoints protegidos, é necessário obter e enviar o token de autenticação do usuário.

Geração do Token: O token é gerado automaticamente para o Superusuário ou qualquer usuário criado.

Uso em Requisições: O token deve ser incluído no cabeçalho (Header) de cada requisição, no formato:

 ```bash
Authorization: Token <SEU_TOKEN_AQUI>
   ```

Dica: Na interface Swagger UI, você pode clicar no botão Authorize e inserir o seu token para testar os endpoints protegidos.

## Configuração do Ambiente

Siga os passos abaixo para configurar o ambiente local.

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/higabeatriz/Projeto-Integrador-1.git
   cd projeto_farma
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4.  **Aplique as migrações: **
       ```bash
       python manage.py makemigrations
       python manage.py migrate
       python manage.py createsuperuser
       ```

5. **Inicie o servidor:**
   ```bash
   python manage.py runserver
   ```
   
## ✨ Guia de Acesso Rápido

Assumimos que o servidor já está rodando (python manage.py runserver).

1. Painel de Gestão (Django Admin)
   
Acesso para cadastro e edição dos dados (Medicamentos, Pacientes, Intervenções) e para obter o Token de Autenticação.

URL de Acesso: http://127.0.0.1:8000/admin/

Login: Use as credenciais do Superusuário criadas.

2. Documentação Interativa
   
Explore as funcionalidades da API de forma visual, sem escrever código, e teste os endpoints protegidos com o seu Token.

URL de Acesso: http://127.0.0.1:8000/api/docs/

3. Visualização dos Dados Brutos (API)
   
Acesse a lista de Intervenções Farmacêuticas diretamente. Esta rota exige autenticação, então você deve estar logado ou ter autorizado o Token.

URL de Acesso: http://127.0.0.1:8000/api/intervencoes/

Ação: Se estiver visualizando no navegador, use o link do Swagger UI primeiro, insira o Token lá e depois tente acessar este link para ver os dados formatados.























