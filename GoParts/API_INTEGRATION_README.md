# 🔗 GoParts API Integration - Parte 3

## 📋 Visão Geral

Esta parte implementa a integração com API REST, incluindo:
- ✅ Envio de produtos do CSV limpo para API
- ✅ Sistema de retries com backoff exponencial
- ✅ Tratamento de falhas intermitentes (5xx, timeouts)
- ✅ Logging detalhado de todas as operações
- ✅ Duas opções de teste: API local e HTTPBin.org

## 🛠️ Arquivos Criados

### 📄 Scripts Principais
- `src/api_integration.py` - Cliente para API local com retries
- `src/httpbin_integration.py` - Cliente para HTTPBin.org 
- `src/test_api.py` - API Flask de teste (30% falha)
- `api_launcher.py` - Launcher unificado

### 📁 Logs
- `logs/` - Diretório para logs de integração
- Logs com timestamp: `httpbin_integration_YYYYMMDD_HHMMSS.log`

## 🚀 Como Executar

### Opção 1: HTTPBin.org (Mais Simples)
```bash
cd "c:\GoParts\GopartsFinalizado\GoParts"
C:/GoParts/.venv/Scripts/python.exe src/httpbin_integration.py
```

### Opção 2: API Local
```bash
# Terminal 1 - Inicia API de teste
cd "c:\GoParts\GopartsFinalizado\GoParts"
C:/GoParts/.venv/Scripts/python.exe src/test_api.py

# Terminal 2 - Executa integração
cd "c:\GoParts\GopartsFinalizado\GoParts"
C:/GoParts/.venv/Scripts/python.exe src/api_integration.py
```

### Opção 3: Launcher Unificado
```bash
cd "c:\GoParts\GopartsFinalizado\GoParts"
C:/GoParts/.venv/Scripts/python.exe api_launcher.py
```

## ⚙️ Configurações de Retry

### Backoff Exponencial
- **Tentativas máximas:** 5
- **Delay inicial:** 1 segundo
- **Fator de multiplicação:** 2x
- **Delay máximo:** 16 segundos
- **Sequência:** 1s → 2s → 4s → 8s → 16s

### Códigos para Retry
- `500` - Internal Server Error
- `502` - Bad Gateway  
- `503` - Service Unavailable
- `504` - Gateway Timeout
- `408` - Request Timeout
- Timeouts de conexão
- Erros de conexão

## 📊 Exemplo de Execução

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

## 🧪 API de Teste (Flask)

### Endpoints Disponíveis
- `GET /health` - Status da API
- `POST /produtos` - Cadastrar produto
- `GET /stats` - Estatísticas de uso
- `POST /reset` - Reset estatísticas

### Comportamento
- **Taxa de falha:** ~30% das requisições
- **Códigos de erro:** 500, 502, 503, 504
- **Delay de processamento:** 0.1-0.5s
- **Porta:** 5000

### Exemplo de Produto
```json
{
    "nome_produto": "Amortecedor Traseiro",
    "codigo": "K12345LA", 
    "preco": 100.0,
    "estoque": 50
}
```

## 📈 Estatísticas de Sucesso

### Resultados do Teste
- **Total processado:** 20 produtos
- **Taxa de sucesso:** 100%
- **Tempo total:** ~51.5 segundos
- **Retries utilizados:** Múltiplos (conforme necessário)

### Padrão de Retry Observado
1. Primeiro produto: 5 tentativas (4 falhas + 1 sucesso)
2. Maioria: 1-2 tentativas
3. Sistema conseguiu entregar todos os produtos

## 🔍 Logs Detalhados

Todos os logs são salvos em `logs/` com:
- ✅ Timestamp de cada operação
- ✅ Detalhes do produto sendo enviado
- ✅ Tentativas e delays
- ✅ Códigos de erro recebidos
- ✅ Estatísticas finais

## 🛡️ Tratamento de Erros

### Tipos de Erro Tratados
1. **HTTP 5xx** - Retry automático
2. **Timeouts** - Retry automático  
3. **Connection Errors** - Retry automático
4. **HTTP 4xx** - Falha imediata (erro do cliente)
5. **Outros erros** - Falha imediata

### Estratégia de Resilência
- Backoff exponencial previne sobrecarga da API
- Limite de tentativas evita loops infinitos
- Logs detalhados facilitam debugging
- Estatísticas finais para análise de performance

## 📝 Dependências

```txt
requests>=2.32.0
pandas>=2.0.0
chardet>=5.0.0
flask>=3.1.0 (apenas para API de teste)
```
