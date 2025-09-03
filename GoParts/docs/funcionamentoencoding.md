# 📄 Funcionamento de Encoding - Projeto GoParts

## 🎯 Objetivo
Este documento explica como lidar com problemas de encoding ao processar arquivos CSV com acentos e caracteres especiais em português.

## 🔍 Problema Identificado

### ❌ Sintomas dos Problemas de Encoding:
- **Acentos quebrados**: `PivÃ´` em vez de `Pivô`
- **Caracteres estranhos**: `LÃ¢mpada` em vez de `Lâmpada`
- **Símbolos corrompidos**: `VÃ¡lvula` em vez de `Válvula`

### 🚨 Causa Raiz:
Uso de encoding incorreto para ler o arquivo CSV, resultando em interpretação incorreta dos caracteres acentuados.

## 🔧 Solução Implementada

### 1️⃣ **Detecção Automática de Encoding**

```python
# Testa diferentes encodings automaticamente
encodings_para_testar = ['utf-8', 'latin1', 'cp1252', 'iso-8859-1']

for encoding in encodings_para_testar:
    try:
        print(f"🔍 Tentando encoding: {encoding}")
        with open('arquivo.csv', 'r', encoding=encoding) as file:
            # Processa o arquivo
            break
    except UnicodeDecodeError:
        continue
```

### 2️⃣ **Resultado da Descoberta**

| Encoding Testado | Resultado | Status |
|------------------|-----------|---------|
| `utf-8` | ✅ Acentos perfeitos | **FUNCIONA** |
| `latin1` | ❌ `PivÃ´ de SuspensÃ£o` | Falha |
| `cp1252` | ⚠️ Não testado | - |
| `iso-8859-1` | ⚠️ Não testado | - |

## 📊 Comparação ANTES vs DEPOIS

### ❌ **ANTES (Latin1 incorreto):**
```
PivÃ´ de SuspensÃ£o
LÃ¢mpada de Farol
Filtro de Ã³leo
VÃ¡lvula TermostÃ¡tica
Sensor de OxigÃªnio
ReservatÃ³rio de ExpansÃ£o
```

### ✅ **DEPOIS (UTF-8 correto):**
```
Pivô de Suspensão
Lâmpada de Farol
Filtro de óleo
Válvula Termostática
Sensor de Oxigênio
Reservatório de Expansão
```

## 🎓 Lições Aprendidas

### 1. **Não confie apenas no nome do arquivo**
- Arquivo chamado `produtos_bagunçados_latin1.csv`
- **Na verdade estava em UTF-8**, não Latin1!

### 2. **Sempre teste múltiplos encodings**
```python
# Ordem recomendada de teste:
encodings = ['utf-8', 'latin1', 'cp1252', 'iso-8859-1']
```

### 3. **UTF-8 é o padrão moderno**
- Mais comum em sistemas atuais
- Suporta todos os caracteres Unicode
- Recomendado para novos arquivos

## 🔄 Processo Completo de Limpeza

### Etapa 1: **Detecção de Encoding**
```python
# Testa automaticamente até encontrar o correto
for encoding in ['utf-8', 'latin1', 'cp1252']:
    try:
        df = pd.read_csv(arquivo, encoding=encoding)
        break
    except UnicodeDecodeError:
        continue
```

### Etapa 2: **Correção de Estrutura**
```python
# Corrige vírgulas extras que desalinham colunas
if len(campos) > 4:
    nome_produto = campos[0]
    codigo = campos[1] 
    preco = campos[2]
    estoque = campos[3] if campos[3].strip() else campos[4]
```

### Etapa 3: **Salvamento em UTF-8**
```python
# Sempre salva em UTF-8 para garantir compatibilidade
df.to_csv('arquivo_limpo.csv', encoding='utf-8-sig', index=False)
```

