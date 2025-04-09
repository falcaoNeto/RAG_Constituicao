Claro, Falcão! Aqui está o README reorganizado, corrigido e com uma linguagem mais fluida e profissional:

---

# 📱 Chatbot Constitucional - RAG + WhatsApp

Este projeto é um **chatbot jurídico via WhatsApp**, capaz de responder perguntas relacionadas à **Constituição Federal de 1988**. Ele utiliza uma **LLM (Large Language Model)** integrada com a técnica de **RAG (Retrieval-Augmented Generation)** para buscar trechos relevantes da Constituição antes de gerar as respostas.

O backend foi desenvolvido com **Flask**, e faz uso das bibliotecas **LangChain** e **Docling** para orquestração da LLM, extração e indexação do documento constitucional. A comunicação com o WhatsApp é realizada via **WAHA**, uma API containerizada que permite interação via QR code com a conta do WhatsApp.

---

## ✅ Funcionalidades

- 🔍 **Busca Inteligente:** Utiliza RAG para localizar e retornar trechos relevantes da Constituição.
- 🤖 **Chatbot Jurídico:** Responde perguntas sobre o texto constitucional de forma clara e objetiva.
- 💬 **Integração com WhatsApp:** Comunicação via API WAHA, rodando em container Docker.
- 🛠️ **API RESTful:** Backend em Flask para gerenciar requisições e orquestrar a aplicação.

---

## 🛠️ Tecnologias Utilizadas

- **Linguagem:** Python
- **Frameworks e Bibliotecas:**
  - [Flask](https://flask.palletsprojects.com/)
  - [LangChain](https://github.com/hwchase17/langchain)
  - [Docling](https://github.com/usuario/docling) *(substitua pelo link oficial, se houver)*
- **Containers e Orquestração:**
  - Docker
  - Docker Compose
  - [WAHA](https://waha.devlike.pro/) – Comunicação com WhatsApp
- **API Externa:**
  - [OpenAI API](https://beta.openai.com/)

---

## 📦 Pré-requisitos

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)
- Conta na [OpenAI](https://beta.openai.com/) com chave de API
- Acesso ao [WAHA](https://waha.devlike.pro/)

---

## 🚀 Instalação e Configuração

### 1. Clonar o Repositório

```bash
git clone https://github.com/falcaoNeto/RAG_Constituicao
cd RAG_Constituicao
```

### 2. Adicionar a chave da OpenAI

Crie um arquivo `.env` com a sua chave da OpenAI:

```bash
cp .env.example .env
```

Depois edite o `.env` e insira sua chave no campo correspondente.

---

### 3. Subir os containers com Docker Compose

```bash
docker-compose build
docker-compose up -d
```

---

### 4. Configurar o WAHA

1. Acesse o painel do WAHA em: [http://localhost:3000/dashboard/](http://localhost:3000/dashboard/)
2. Vá até as configurações da sessão.
3. Configure o **Webhook URL** como:

```
http://api:5000/chatbot/webhook/
```

4. Inicie a sessão do WAHA.
5. Escaneie o **QR Code** para vincular o número do WhatsApp.

---

✅ Pronto! Agora você pode começar a utilizar o chatbot jurídico via WhatsApp para tirar dúvidas sobre a Constituição Federal de 1988.
