# 🚀 **CASE TÉCNICO GOPARTS - GUIA DE EXECUÇÃO**

> **Desenvolvido para:** Processo Seletivo de Estágio  
> **Candidato:** [Seu Nome]  
> **Data:** Setembro 2025  
> **Tecnologias:** Python, Pandas, APIs REST, Retry Pattern  

---

## 📋 **SOBRE O PROJETO**

Este projeto implementa um **sistema completo de processamento de dados e integração com APIs** para a empresa GoParts, demonstrando competências em:

- ✅ **Limpeza e normalização de dados** (CSV com encoding automático)
- ✅ **Integração resiliente com APIs** (retry pattern com backoff exponencial)
- ✅ **Tratamento de erros** e logging profissional
- ✅ **Boas práticas de desenvolvimento** Python

---

## 🎯 **EXECUÇÃO RÁPIDA (2 MINUTOS)**

### **Opção 1: Demo Automático** ⭐ *(Recomendado para apresentação)*
```cmd
cd "c:\GoParts\GopartsFinalizado\GoParts"
python demo_apresentacao.py
```

### **Opção 2: Menu Interativo**
```cmd
cd "c:\GoParts\GopartsFinalizado\GoParts"
test_menu.bat
```

### **Opção 3: Comandos Manuais**
```cmd
cd "c:\GoParts\GopartsFinalizado\GoParts"
python src/data_cleaner.py
python src/httpbin_integration.py
```

---

## 🔧 **PRÉ-REQUISITOS**

### **Sistema:**
- ✅ Windows 10/11
- ✅ Python 3.8+ (projeto usa Python 3.13.7)
- ✅ Git (opcional - para clone do repositório)

### **Dependências Python:**
```txt
pandas==2.3.2
chardet==5.2.0
requests==2.32.5
flask==3.1.2
```

---

## ⚡ **INSTALAÇÃO E SETUP**

### **Passo 1: Preparar Ambiente**
```powershell
# 1. Clone o repositório (se não tiver)
git clone https://github.com/caiolamoglia1/GopartsFinalizado.git
cd GopartsFinalizado/GoParts

# 2. Criar ambiente virtual
python -m venv .venv

# 3. Ativar ambiente virtual
.venv\Scripts\activate

# 4. Instalar dependências
pip install pandas chardet requests flask
```

### **Passo 2: Verificar Estrutura**
```
GoParts/
├── 📁 data/
│   ├── raw/produtos.csv        # Dados originais
│   └── output/                 # Dados processados
├── 📁 src/
│   ├── data_cleaner.py        # Limpeza de dados
│   ├── api_integration.py     # Cliente API local
│   └── httpbin_integration.py # Cliente API externa
├── 📁 logs/                   # Logs de execução
└── demo_apresentacao.py       # Demo para apresentação
```

---

## 🎮 **COMO EXECUTAR**

### **🚀 Execução Completa (Demo)**

**Execute este comando único:**
```cmd
cd "c:\GoParts\GopartsFinalizado\GoParts"
python demo_apresentacao.py
```

**O que acontece:**
1. 🔄 **Processamento de Dados**: Limpa 20 produtos do CSV
2. 🌐 **Integração API**: Envia dados para httpbin.org com retry
3. 📊 **Relatórios**: Exibe estatísticas de sucesso

**Duração:** ~2-3 minutos

---

### **🔍 Execução Detalhada (Passo a Passo)**

#### **Parte 1: Limpeza de Dados**
```cmd
python src/data_cleaner.py
```
**Resultado esperado:**
```
✅ Encoding detectado: ISO-8859-1
✅ 20 produtos processados e limpos
✅ Arquivo salvo: data/output/produtos_limpos_utf8.csv
```

#### **Parte 2: Integração com API**
```cmd
python src/httpbin_integration.py
```
**Resultado esperado:**
```
📊 RELATÓRIO FINAL
============================================================
⏱️  Duração total: ~60s
📦 Total de produtos: 20
✅ Enviados com sucesso: 20
❌ Falhas: 0
📈 Taxa de sucesso: 100.0%
============================================================
```

---

### **🧪 Teste com API Local (Opcional)**

**Terminal 1 - Iniciar API:**
```cmd
python src/test_api.py
```

**Terminal 2 - Testar API:**
```cmd
python teste_api_rapido.py
python src/api_integration.py
```

---

## 📊 **RESULTADOS ESPERADOS**

### **✅ Indicadores de Sucesso:**

#### **Processamento de Dados:**
- ✅ **20 produtos** processados
- ✅ **Encoding** detectado automaticamente (ISO-8859-1 → UTF-8)
- ✅ **Preços** normalizados (R$ 1.234,56 → 1234.56)
- ✅ **Arquivo CSV** limpo gerado

#### **Integração de API:**
- ✅ **Taxa de sucesso: 100%** (com retry automático)
- ✅ **Backoff exponencial**: 1s → 2s → 4s → 8s → 16s
- ✅ **Logs detalhados** com timestamps
- ✅ **Tratamento de erros** HTTP 5xx

---

## 🔧 **SOLUÇÃO DE PROBLEMAS**

### **❌ Erro: "Python não encontrado"**
```cmd
# Verifique se Python está instalado
python --version

# Se não funcionar, tente:
py --version
# ou
python3 --version
```

### **❌ Erro: "Módulo não encontrado"**
```cmd
# Instale dependências
pip install pandas chardet requests flask

# Ou use o requirements.txt
pip install -r requirements.txt
```

### **❌ Erro: "Arquivo não encontrado"**
```cmd
# Certifique-se de estar no diretório correto
cd "c:\GoParts\GopartsFinalizado\GoParts"
dir src\  # Deve mostrar os arquivos .py
```

### **❌ Erro: "Encoding do arquivo"**
```cmd
# O sistema detecta automaticamente
# Verifique se data/raw/produtos.csv existe
dir data\raw\
```

---

## 📁 **ESTRUTURA DE ARQUIVOS GERADOS**

Após execução bem-sucedida:

```
data/output/
└── produtos_limpos_utf8.csv    # Dados processados

logs/
├── httpbin_integration_YYYYMMDD_HHMMSS.log
└── data_cleaning_YYYYMMDD_HHMMSS.log
```

---

## 🎯 **CARACTERÍSTICAS TÉCNICAS IMPLEMENTADAS**

### **🔄 Processamento de Dados:**
- **Detecção automática de encoding** com `chardet`
- **Normalização de preços** brasileiros (R$ → float)
- **Validação de dados** e tratamento de valores nulos
- **Logs estruturados** com níveis INFO/ERROR

### **🌐 Integração de APIs:**
- **Retry pattern** com backoff exponencial
- **Timeout configurável** (5s por requisição)
- **Circuit breaker** após 5 tentativas
- **Logging profissional** com contexto de erro
- **Testes com httpbin.org** (simulação de falhas reais)

### **🛡️ Tratamento de Erros:**
- **HTTP Status Codes**: 500, 502, 503, 504
- **Timeouts de rede**
- **Falhas de conexão**
- **Dados corrompidos ou inválidos**

---

## 📝 **RELATÓRIOS E MÉTRICAS**

### **Métricas Coletadas:**
- ✅ **Taxa de sucesso** de integração
- ✅ **Tempo total** de processamento
- ✅ **Número de retries** por requisição
- ✅ **Tipos de erro** encontrados
- ✅ **Latência média** das APIs

### **Logs Disponíveis:**
- 📁 `logs/data_cleaning_*.log` - Processamento de dados
- 📁 `logs/httpbin_integration_*.log` - Integração API
- 📁 `logs/api_integration_*.log` - Testes API local

---

## 🎬 **DEMO PARA APRESENTAÇÃO**

### **Script de Apresentação (30 segundos):**

```
"Desenvolvido um sistema completo de processamento de dados para GoParts.

O sistema automaticamente detecta encoding, limpa dados CSV e integra 
com APIs usando retry resiliente.

Vamos executar a demonstração..."
```

### **Comando único:**
```cmd
python demo_apresentacao.py
```

### **Resultado visual:**
```
🎯 DEMONSTRAÇÃO - PROJETO GOPARTS
==================================================
📱 Case Técnico: Sistema de Processamento de Dados e APIs
==================================================

🔄 PARTE 1: Processamento de Dados
   - Limpeza automática de CSV
   - Detecção de encoding
   - Normalização de preços
   - Validação de dados
   ⏯️  Pressione ENTER para executar...

✅ PARTE 1 CONCLUÍDA!

🌐 PARTE 2: Integração com API
   - Sistema de retry resiliente
   - Backoff exponencial
   - Tratamento de falhas HTTP 5xx
   - Logging profissional
   ⏯️  Pressione ENTER para executar...

✅ PARTE 2 CONCLUÍDA!

🎉 DEMONSTRAÇÃO CONCLUÍDA!
📊 Sistema 100% funcional e testado!
```

---

## 🎯 **PRÓXIMOS PASSOS (Sugestões)**

### **Melhorias Possíveis:**
- 🔄 **Dashboard web** com Flask
- 📊 **Métricas em tempo real** 
- 🐳 **Containerização** com Docker
- 🧪 **Testes automatizados** com pytest
- 📈 **Monitoramento** com Prometheus

---

## 📞 **CONTATO E SUPORTE**

**Desenvolvedor:** [Seu Nome]  
**Email:** [seu.email@exemplo.com]  
**LinkedIn:** [linkedin.com/in/seuprofile]  
**GitHub:** [github.com/seuusuario]  

---

## 📄 **LICENÇA**

Este projeto foi desenvolvido como parte de um processo seletivo para demonstrar competências técnicas em desenvolvimento Python e integração de sistemas.

---

**🎉 Projeto desenvolvido com dedicação para demonstrar competências técnicas em desenvolvimento Python! 🚀**
