# 🧪 Guia de Testes - GoParts API Integration

## 🚀 Como Testar o Sistema

### 📋 **Pré-requisitos**
1. ✅ Dependências instaladas (pandas, requests, flask)
2. ✅ CSV limpo disponível em `data/output/produtos_limpos_utf8.csv`
3. ✅ Ambiente virtual ativo

---

## 🎯 **Opção 1: Teste Rápido (HTTPBin) - RECOMENDADO**

Esta é a forma mais simples de testar, pois usa httpbin.org:

### No PowerShell:
```powershell
cd "c:\Goparts1\GopartsFinalizado\GoParts"
C:/Goparts1/.venv/Scripts/python.exe src/httpbin_integration.py
```

### Ou use o menu:
```cmd
test_menu.bat
# Escolha opção 1
```

### 📊 **O que esperar:**
- ✅ Carregamento de 20 produtos do CSV
- ✅ Conexão com httpbin.org
- ✅ Envio com falhas simuladas (~30%)
- ✅ Retries automáticos com backoff exponencial
- ✅ Relatório final com estatísticas

---

## 🏠 **Opção 2: Teste com API Local**

### Passo 1: Iniciar API de Teste
```powershell
# Terminal 1
cd "c:\Goparts1\GopartsFinalizado\GoParts"
C:/Goparts1/.venv/Scripts/python.exe src/test_api.py
```

### Passo 2: Executar Cliente
```powershell
# Terminal 2 (novo terminal)
cd "c:\Goparts1\GopartsFinalizado\GoParts"
C:/Goparts1/.venv/Scripts/python.exe src/api_integration.py
```

### 🌐 **Endpoints da API de Teste:**
- `GET http://localhost:5000/health` - Status
- `POST http://localhost:5000/produtos` - Cadastrar produto
- `GET http://localhost:5000/stats` - Estatísticas
- `POST http://localhost:5000/reset` - Reset

---

## 🔧 **Opção 3: Verificação do Sistema**

Para verificar se tudo está configurado:

```powershell
cd "c:\Goparts1\GopartsFinalizado\GoParts"
C:/Goparts1/.venv/Scripts/python.exe test_integration.py
```

### ✅ **Verificações realizadas:**
- Imports (pandas, requests)
- Arquivo CSV existe e carrega
- Conexão com httpbin.org
- Estrutura do projeto
- Scripts existem

---

## 📱 **Opção 4: Menu Interativo**

Execute o menu de testes:

```cmd
cd "c:\Goparts1\GopartsFinalizado\GoParts"
test_menu.bat
```

**Opções do menu:**
1. 🌐 Teste com HTTPBin.org
2. 🏠 Teste com API Local  
3. 🔧 Iniciar API de Teste
4. 📋 Teste de Verificação
5. 📊 Ver Logs

---

## 📊 **Exemplo de Saída Esperada**

```
🌐 GoParts HTTPBin Integration v1.0
==================================================
📁 Arquivo CSV: C:\...\produtos_limpos_utf8.csv
🌐 API: httpbin.org (simulando falhas)
📝 Log file: C:\...\logs\httpbin_integration_20250903_192622.log
🔄 Retry config: max_attempts=5, backoff=2.0x
💥 Taxa de falha simulada: 30%

📊 Carregando produtos do CSV...
✅ 20 produtos carregados
🔍 Testando conexão com httpbin.org...
✅ Conexão com httpbin.org estabelecida
🚀 Iniciando envio de 20 produtos...

📤 Enviando produto: Amortecedor Traseiro (tentativa 1)
🔴 Simulando erro HTTP 502
⚠️ Tentando novamente em 1.0s...
📤 Enviando produto: Amortecedor Traseiro (tentativa 2)
✅ Produto enviado com sucesso: K12345LA

...

============================================================
📊 RELATÓRIO FINAL - HTTPBin Integration
============================================================
⏱️  Duração total: 51.5s
📦 Total de produtos: 20
✅ Enviados com sucesso: 20
❌ Falhas: 0
📈 Taxa de sucesso: 100.0%
💥 Taxa de falha esperada: ~30%
============================================================
```

---

## 🔍 **Logs e Debugging**

### 📁 **Localização dos Logs:**
```
logs/
├── httpbin_integration_YYYYMMDD_HHMMSS.log
└── api_integration_YYYYMMDD_HHMMSS.log
```

### 📋 **Ver logs:**
```cmd
# Windows
type logs\httpbin_integration_*.log

# PowerShell  
Get-Content logs\httpbin_integration_*.log
```

---

## ⚠️ **Troubleshooting**

### ❌ **"Module not found"**
```powershell
# Reinstalar dependências
C:/Goparts1/.venv/Scripts/python.exe -m pip install requests pandas flask
```

### ❌ **"CSV não encontrado"**
```powershell
# Executar limpeza primeiro
C:/Goparts1/.venv/Scripts/python.exe run.py
```

### ❌ **"API não está rodando"**
```powershell
# Verificar se a API está ativa
curl http://localhost:5000/health
```

### ❌ **"Conexão com httpbin falhou"**
- Verificar conexão com internet
- Tentar novamente em alguns minutos

---

## 🎯 **Testes Avançados**

### 🔧 **Testar API manualmente:**
```powershell
# Testar endpoint de saúde
curl http://localhost:5000/health

# Enviar produto manualmente
curl -X POST http://localhost:5000/products -H "Content-Type: application/json" -d "{\"nome_produto\":\"Teste\",\"codigo\":\"TEST01\",\"preco\":100.0,\"estoque\":10}"
```

### 📊 **Verificar estatísticas:**
```powershell
curl http://localhost:5000/stats
```

---

## ✅ **Critérios de Sucesso**

Um teste bem-sucedido deve mostrar:
- ✅ Carregamento do CSV (20 produtos)
- ✅ Conexão estabelecida
- ✅ Envios com retries funcionando
- ✅ Taxa de sucesso alta (90%+)
- ✅ Logs detalhados gerados
- ✅ Backoff exponencial em ação
- ✅ Tratamento de erros 5xx

---

## 🏁 **Quick Start**

**Para um teste rápido de 2 minutos:**

1. Abra PowerShell como administrador
2. Execute:
   ```powershell
   cd "c:\Goparts1\GopartsFinalizado\GoParts"
   C:/Goparts1/.venv/Scripts/python.exe src/httpbin_integration.py
   ```
3. Aguarde o relatório final
4. Verifique os logs em `logs/`

**Pronto! 🎉**
