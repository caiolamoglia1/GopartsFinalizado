# 🌐 API.md - Guia Completo de APIs do Zero

## 📚 Índice
1. [O que é uma API?](#o-que-é-uma-api)
2. [Conceitos Fundamentais](#conceitos-fundamentais)
3. [Tipos de APIs](#tipos-de-apis)
4. [HTTP e REST](#http-e-rest)
5. [Métodos HTTP](#métodos-http)
6. [Status Codes](#status-codes)
7. [JSON - Formato de Dados](#json---formato-de-dados)
8. [Como Consumir APIs](#como-consumir-apis)
9. [Como Criar APIs](#como-criar-apis)
10. [Autenticação](#autenticação)
11. [Tratamento de Erros](#tratamento-de-erros)
12. [Boas Práticas](#boas-práticas)
13. [Exemplos Práticos](#exemplos-práticos)

---

## 🤔 O que é uma API?

**API** = **Application Programming Interface** (Interface de Programação de Aplicações)

### 🔍 Analogia Simples
Imagine um **restaurante**:
- 👨‍🍳 **Cozinha** = Sistema/Banco de dados
- 🍽️ **Cardápio** = Documentação da API
- 🧑‍💼 **Garçom** = API
- 👤 **Cliente** = Sua aplicação

Você (cliente) não vai direto na cozinha pegar a comida. Você fala com o garçom (API), que:
1. Recebe seu pedido
2. Vai na cozinha buscar
3. Traz a comida para você

### 💡 Definição Técnica
Uma API é um **conjunto de regras e protocolos** que permite que diferentes aplicações se comuniquem entre si.

---

## 🧩 Conceitos Fundamentais

### 🔗 **Cliente e Servidor**
```
Cliente (Sua App) -----> API -----> Servidor (Dados)
                  ↑              ↓
               Requisição    Resposta
```

### 📡 **Endpoint**
É o "endereço" específico de uma função da API:
```
https://api.exemplo.com/produtos
https://api.exemplo.com/usuarios/123
https://api.exemplo.com/pedidos
```

### 📦 **Request (Requisição)**
O que você envia para a API:
- **URL**: Onde enviar
- **Método**: O que fazer (GET, POST, etc.)
- **Headers**: Informações extras
- **Body**: Dados (quando necessário)

### 📬 **Response (Resposta)**
O que a API retorna:
- **Status Code**: Se deu certo ou não
- **Headers**: Informações sobre a resposta
- **Body**: Os dados solicitados

---

## 🏷️ Tipos de APIs

### 🌐 **Web APIs (REST)**
- Mais comum hoje
- Usa protocolo HTTP
- Formato JSON
- Exemplos: Instagram API, GitHub API

### 🧼 **SOAP APIs**
- Mais antigo
- Usa XML
- Mais rígido e formal

### 🔌 **GraphQL**
- Mais moderno
- Você escolhe exatamente quais dados quer
- Uma só requisição pode buscar dados de vários lugares

### 🔄 **WebSocket APIs**
- Comunicação em tempo real
- Bidirecional
- Exemplo: Chat em tempo real

---

## 🌍 HTTP e REST

### 🔤 **HTTP** (HyperText Transfer Protocol)
É o "idioma" que navegadores e servidores usam para conversar.

### 🏗️ **REST** (Representational State Transfer)
É um **estilo arquitetural** para criar APIs web. APIs REST são:

#### ✅ Características REST:
- **Stateless**: Cada requisição é independente
- **Cacheable**: Respostas podem ser armazenadas
- **Uniform Interface**: Padrão consistente
- **Client-Server**: Separação clara de responsabilidades

#### 🎯 **Princípios REST:**
1. **Recursos** são identificados por URLs
2. **Métodos HTTP** indicam a ação
3. **Representações** (geralmente JSON)
4. **HATEOAS** (Hypermedia as the Engine of Application State)

---

## 🔧 Métodos HTTP

### 📖 **GET** - Buscar dados
```http
GET /produtos
GET /produtos/123
```
- Não altera nada
- Pode ser repetido sem problemas
- Dados vão na URL

### ➕ **POST** - Criar novo recurso
```http
POST /produtos
Content-Type: application/json

{
  "nome": "Amortecedor",
  "preco": 150.00
}
```

### 🔄 **PUT** - Atualizar recurso completo
```http
PUT /produtos/123
Content-Type: application/json

{
  "id": 123,
  "nome": "Amortecedor Novo",
  "preco": 180.00,
  "estoque": 50
}
```

### 🖊️ **PATCH** - Atualizar parcialmente
```http
PATCH /produtos/123
Content-Type: application/json

{
  "preco": 160.00
}
```

### ❌ **DELETE** - Remover recurso
```http
DELETE /produtos/123
```

### 🔍 **OPTIONS** - Descobrir métodos disponíveis
```http
OPTIONS /produtos
```

---

## 🚦 Status Codes

### ✅ **2xx - Sucesso**
- **200 OK**: Tudo certo
- **201 Created**: Recurso criado
- **204 No Content**: Sucesso, mas sem dados para retornar

### ❌ **4xx - Erro do Cliente**
- **400 Bad Request**: Requisição inválida
- **401 Unauthorized**: Não autenticado
- **403 Forbidden**: Sem permissão
- **404 Not Found**: Recurso não encontrado
- **422 Unprocessable Entity**: Dados inválidos

### 💥 **5xx - Erro do Servidor**
- **500 Internal Server Error**: Erro no servidor
- **502 Bad Gateway**: Problema no gateway
- **503 Service Unavailable**: Serviço indisponível
- **504 Gateway Timeout**: Timeout no gateway

---

## 📄 JSON - Formato de Dados

**JSON** (JavaScript Object Notation) é o formato mais usado para trocar dados.

### 🔢 **Tipos de Dados:**
```json
{
  "texto": "string",
  "numero": 123,
  "decimal": 45.67,
  "booleano": true,
  "nulo": null,
  "array": [1, 2, 3],
  "objeto": {
    "chave": "valor"
  }
}
```

### 🛒 **Exemplo Real - Produto:**
```json
{
  "id": 123,
  "nome": "Amortecedor Traseiro",
  "codigo": "K12345LA",
  "preco": 150.00,
  "estoque": 25,
  "categoria": {
    "id": 5,
    "nome": "Suspensão"
  },
  "tags": ["automotivo", "suspensao", "seguranca"],
  "ativo": true,
  "criado_em": "2025-09-03T19:30:00Z"
}
```

---

## 🔌 Como Consumir APIs

### 🐍 **Python com requests:**
```python
import requests

# GET - Buscar produtos
response = requests.get('https://api.exemplo.com/produtos')
produtos = response.json()

# POST - Criar produto
novo_produto = {
    "nome": "Filtro de Óleo",
    "preco": 25.00
}
response = requests.post(
    'https://api.exemplo.com/produtos',
    json=novo_produto
)

# Verificar se deu certo
if response.status_code == 201:
    print("Produto criado!")
else:
    print(f"Erro: {response.status_code}")
```

### 🌐 **JavaScript com fetch:**
```javascript
// GET - Buscar produtos
fetch('https://api.exemplo.com/produtos')
  .then(response => response.json())
  .then(produtos => console.log(produtos));

// POST - Criar produto
fetch('https://api.exemplo.com/produtos', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    nome: 'Filtro de Óleo',
    preco: 25.00
  })
})
.then(response => response.json())
.then(resultado => console.log(resultado));
```

### 💻 **cURL (Terminal):**
```bash
# GET
curl https://api.exemplo.com/produtos

# POST
curl -X POST https://api.exemplo.com/produtos \
  -H "Content-Type: application/json" \
  -d '{"nome": "Filtro de Óleo", "preco": 25.00}'
```

---

## 🏗️ Como Criar APIs

### 🐍 **API Simples com Flask (Python):**
```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Dados simulados
produtos = [
    {"id": 1, "nome": "Amortecedor", "preco": 150.00},
    {"id": 2, "nome": "Filtro", "preco": 25.00}
]

# GET - Listar produtos
@app.route('/produtos', methods=['GET'])
def listar_produtos():
    return jsonify(produtos)

# GET - Buscar produto específico
@app.route('/produtos/<int:produto_id>', methods=['GET'])
def buscar_produto(produto_id):
    produto = next((p for p in produtos if p['id'] == produto_id), None)
    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404

# POST - Criar produto
@app.route('/produtos', methods=['POST'])
def criar_produto():
    dados = request.get_json()
    
    # Validação simples
    if not dados or 'nome' not in dados or 'preco' not in dados:
        return jsonify({"erro": "Nome e preço são obrigatórios"}), 400
    
    novo_produto = {
        "id": len(produtos) + 1,
        "nome": dados['nome'],
        "preco": dados['preco']
    }
    produtos.append(novo_produto)
    
    return jsonify(novo_produto), 201

# PUT - Atualizar produto
@app.route('/produtos/<int:produto_id>', methods=['PUT'])
def atualizar_produto(produto_id):
    produto = next((p for p in produtos if p['id'] == produto_id), None)
    if not produto:
        return jsonify({"erro": "Produto não encontrado"}), 404
    
    dados = request.get_json()
    produto.update(dados)
    
    return jsonify(produto)

# DELETE - Remover produto
@app.route('/produtos/<int:produto_id>', methods=['DELETE'])
def remover_produto(produto_id):
    global produtos
    produtos = [p for p in produtos if p['id'] != produto_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
```

### 🚀 **Executar a API:**
```bash
python api.py
# API rodando em http://localhost:5000
```

---

## 🔐 Autenticação

### 🔑 **API Key**
```python
headers = {
    'Authorization': 'Bearer sua_api_key_aqui',
    'Content-Type': 'application/json'
}
response = requests.get('https://api.exemplo.com/dados', headers=headers)
```

### 🎫 **JWT (JSON Web Token)**
```python
import jwt

# Criar token
token = jwt.encode(
    {"user_id": 123, "exp": datetime.utcnow() + timedelta(hours=1)},
    "chave_secreta",
    algorithm="HS256"
)

# Usar token
headers = {"Authorization": f"Bearer {token}"}
```

### 🔒 **OAuth 2.0**
Processo mais complexo com múltiplas etapas:
1. Redirecionar usuário para autorização
2. Receber código de autorização
3. Trocar código por token de acesso
4. Usar token para acessar API

---

## ⚠️ Tratamento de Erros

### 🛡️ **Código Defensivo:**
```python
import requests
from requests.exceptions import RequestException, Timeout, ConnectionError

def buscar_produto(produto_id):
    try:
        response = requests.get(
            f'https://api.exemplo.com/produtos/{produto_id}',
            timeout=10  # 10 segundos de timeout
        )
        
        # Verificar status code
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("Produto não encontrado")
            return None
        elif response.status_code >= 500:
            print("Erro no servidor, tente novamente")
            return None
        else:
            print(f"Erro inesperado: {response.status_code}")
            return None
            
    except Timeout:
        print("Timeout: API demorou para responder")
        return None
    except ConnectionError:
        print("Erro de conexão: Verifique sua internet")
        return None
    except RequestException as e:
        print(f"Erro na requisição: {e}")
        return None
```

### 🔄 **Retry com Backoff:**
```python
import time
import random

def requisicao_com_retry(url, max_tentativas=3):
    for tentativa in range(max_tentativas):
        try:
            response = requests.get(url, timeout=10)
            if response.status_code == 200:
                return response.json()
            elif response.status_code >= 500:
                # Erro do servidor - tentar novamente
                if tentativa < max_tentativas - 1:
                    delay = (2 ** tentativa) + random.uniform(0, 1)
                    print(f"Tentativa {tentativa + 1} falhou, tentando novamente em {delay:.1f}s")
                    time.sleep(delay)
                    continue
            else:
                # Erro do cliente - não tentar novamente
                break
                
        except (Timeout, ConnectionError):
            if tentativa < max_tentativas - 1:
                delay = (2 ** tentativa) + random.uniform(0, 1)
                print(f"Erro de conexão, tentando novamente em {delay:.1f}s")
                time.sleep(delay)
                continue
    
    return None
```

---

## ✨ Boas Práticas

### 🎯 **Para Consumir APIs:**
1. **Sempre tratar erros** - A rede pode falhar
2. **Usar timeouts** - Não esperar para sempre
3. **Implementar retry** - Para erros temporários
4. **Respeitar rate limits** - Não sobrecarregar a API
5. **Usar HTTPS** - Segurança sempre
6. **Validar dados** - Nunca confie cegamente
7. **Loggar operações** - Para debugging

### 🏗️ **Para Criar APIs:**
1. **Usar status codes corretos** - 200, 404, 500, etc.
2. **Validar entrada** - Verificar dados recebidos
3. **Documentar endpoints** - Como usar sua API
4. **Versionamento** - `/v1/produtos`, `/v2/produtos`
5. **Rate limiting** - Prevenir abuso
6. **Paginação** - Para listas grandes
7. **CORS** - Para acesso de navegadores
8. **Logs detalhados** - Para monitoramento

### 📚 **Estrutura de URLs RESTful:**
```
GET    /produtos           # Listar todos
GET    /produtos/123       # Buscar específico
POST   /produtos           # Criar novo
PUT    /produtos/123       # Atualizar completo
PATCH  /produtos/123       # Atualizar parcial
DELETE /produtos/123       # Remover

# Recursos aninhados
GET    /produtos/123/avaliacoes    # Avaliações do produto
POST   /produtos/123/avaliacoes    # Nova avaliação
```

---

## 🎯 Exemplos Práticos

### 🛒 **Sistema de E-commerce:**
```python
# 1. Listar produtos
produtos = requests.get('https://api.loja.com/produtos').json()

# 2. Buscar produto específico
produto = requests.get('https://api.loja.com/produtos/123').json()

# 3. Adicionar ao carrinho
carrinho = requests.post('https://api.loja.com/carrinho', json={
    "produto_id": 123,
    "quantidade": 2
}).json()

# 4. Finalizar pedido
pedido = requests.post('https://api.loja.com/pedidos', json={
    "carrinho_id": carrinho['id'],
    "endereco": "Rua ABC, 123"
}).json()
```

### 🌤️ **Consultar Clima:**
```python
def consultar_clima(cidade):
    api_key = "sua_chave_aqui"
    url = f"https://api.openweathermap.org/data/2.5/weather"
    
    params = {
        "q": cidade,
        "appid": api_key,
        "units": "metric",
        "lang": "pt"
    }
    
    response = requests.get(url, params=params)
    
    if response.status_code == 200:
        dados = response.json()
        return {
            "cidade": dados["name"],
            "temperatura": dados["main"]["temp"],
            "descricao": dados["weather"][0]["description"]
        }
    else:
        return None

# Uso
clima = consultar_clima("São Paulo")
if clima:
    print(f"Em {clima['cidade']}: {clima['temperatura']}°C, {clima['descricao']}")
```

### 📱 **Enviar Notificação:**
```python
def enviar_notificacao(titulo, mensagem):
    webhook_url = "https://hooks.slack.com/services/..."
    
    payload = {
        "text": f"*{titulo}*\n{mensagem}"
    }
    
    response = requests.post(webhook_url, json=payload)
    return response.status_code == 200
```

---

## 🎓 Próximos Passos

### 📖 **Para Iniciantes:**
1. ✅ Entender conceitos básicos (você já está aqui!)
2. 🔬 Praticar com APIs públicas (JSONPlaceholder, GitHub API)
3. 🐍 Aprender uma linguagem (Python + requests)
4. 🏗️ Criar sua primeira API simples
5. 📚 Estudar autenticação e segurança

### 🚀 **Para Avançar:**
1. 🔄 GraphQL
2. 🌐 Microserviços
3. 🔒 OAuth 2.0 / JWT
4. 📊 Rate limiting e caching
5. 🧪 Testes de API
6. 📋 Documentação (Swagger/OpenAPI)
7. ☁️ Deploy na nuvem

### 🛠️ **Ferramentas Úteis:**
- **Postman** - Testar APIs
- **Insomnia** - Alternativa ao Postman
- **curl** - Linha de comando
- **HTTPie** - curl mais amigável
- **Swagger** - Documentação de APIs
- **JSON Viewer** - Visualizar JSON

---

## 🎉 Conclusão

**Sim, você consegue aprender APIs do zero!** 

APIs são fundamentais no desenvolvimento moderno. Com este guia você tem:
- ✅ Conceitos fundamentais
- ✅ Exemplos práticos
- ✅ Códigos prontos para usar
- ✅ Boas práticas
- ✅ Próximos passos

**Comece simples, pratique muito e evolua gradualmente!**

### 🚀 **Primeiro Projeto Sugerido:**
Crie uma API simples para gerenciar uma lista de tarefas:
- GET /tarefas (listar)
- POST /tarefas (criar)
- PUT /tarefas/id (atualizar)
- DELETE /tarefas/id (remover)

**Boa sorte na sua jornada com APIs!** 🌟
