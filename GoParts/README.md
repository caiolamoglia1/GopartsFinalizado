# 🚗 GoParts - Sistema de Limpeza de Dados


## 📁 Estrutura do Projeto

```
GoParts/
├── 📂 src/                          # Código fonte
│   └── data_cleaner.py             # Script principal de limpeza
├── 📂 data/                        # Arquivos de dados
│   ├── input/                      # Dados de entrada
│   │   └── produtos_bagunçados_latin1.csv
│   └── output/                     # Dados processados
│       └── produtos_limpos_utf8.csv
├── 📂 docs/                        # Documentação
│   ├── COMANDOS.md                 # Referência de comandos
│   └── funcionamentoencoding.md    # Guia de encoding
├── 📂 APRENDIZADO/                 # Versões de estudo
│   ├── Teste.py                    # Versão inicial
│   ├── produtos_limpos.csv         # Resultado de estudo
│   └── README.md                   # Documentação de aprendizado
├── 📂 .vscode/                     # Configurações VS Code
└── 📄 README.md                    # Este arquivo
```

## ⚙️ Pré-requisitos

```bash
# Instalar dependências necessárias
pip install pandas chardet
```

## 🚀 Como Usar

### 1. **Configurar Ambiente**
```bash
# Ativar ambiente virtual
C:/GoParts/.venv/Scripts/Activate.ps1

# Navegar para o diretório do projeto
cd C:\GoParts\GoParts
```

### 2. **Executar Limpeza**
```bash
# Executar script principal (do diretório raiz do projeto)
python src\data_cleaner.py
```

### 3. **Verificar Resultados**
- **Entrada**: `data/input/produtos_bagunçados_latin1.csv`
- **Saída**: `data/output/produtos_limpos_utf8.csv`

## 🔧 Funcionalidades

### 💰 **Normalização de Preços**
| Entrada | Saída |
|---------|--------|
| `R$1.250,00` | `1250.00` |
| `"100,50"` | `100.50` |
| `R$ 200,00` | `200.00` |

### 📦 **Limpeza de Estoque**
| Entrada | Saída |
|---------|--------|
| `-1` | `0` |
| `None` | `0` |
| `n/a` | `0` |
| `""` | `0` |

### 🔤 **Correção de Encoding**
| Antes | Depois |
|-------|--------|
| `PivÃ´ de SuspensÃ£o` | `Pivô de Suspensão` |
| `LÃ¢mpada` | `Lâmpada` |
| `VÃ¡lvula` | `Válvula` |

## 🛠️ Tecnologias

- **Python 3.11+**
- **Pandas** - Manipulação de dados
- **Chardet** - Detecção automática de encoding 
- **Correção estrutural de CSV**

## 📊 Resultados

- ✅ **20 produtos** processados com sucesso
- ✅ **Acentos preservados** perfeitamente  
- ✅ **Estrutura corrigida** automaticamente
- ✅ **Compatibilidade UTF-8** garantida

## 📚 Documentação

- 📖 **[Comandos](docs/COMANDOS.md)** - Referência completa de comandos
- 🔤 **[Encoding](docs/funcionamentoencoding.md)** - Guia detalhado de encoding
- 🎓 **[Aprendizado](APRENDIZADO/README.md)** - Versões de estudo

## 🎓 Para Desenvolvedores

### **Versão de Produção**: `src/data_cleaner.py`
- Lê arquivos CSV reais
- Utiliza Chardet para detecção automática de encoding (não manual)
- Correção de inconsistências estruturais
- Robusta para dados do mundo real

### **Versão de Estudo**: `APRENDIZADO/Teste.py`  
- Dados hardcoded para aprendizado
- Lógica básica simplificada

## 🔄 Processo de Limpeza

1. **🔍 Detecção** - Usa Chardet para detectar automaticamente o encoding (não manual)
2. **🔧 Correção** - Realinha colunas desorganizadas  
3. **💰 Normalização** - Converte formatos monetários
4. **📦 Validação** - Limpa valores de estoque
5. **🏷️ Formatação** - Remove espaços extras
6. **💾 Exportação** - Salva em UTF-8

---

**🏆 Projeto desenvolvido para demonstrar expertise em limpeza de dados e resolução de problemas reais de encoding.**
