


### 💰 Preços em Formatos Variados
- `100` → `100.00`
- `R$100` → `100.00`
- `"R$1.250,00"` → `1250.00`
- `"100,50"` → `100.50`
- `R$ 200,00` → `200.00`

### 📦 Valores de Estoque Inválidos
- `-1` → `0`
- `None` → `0`
- `n/a` → `0`
- Campos vazios → `0`

### 🏷️ Nomes de Produtos com Problemas / strip, (stripados)
- `" Bieleta  "` → `"Bieleta"`
- Remoção de espaços extras

## 📋 Estrutura do Projeto

```
GoParts/
├── � src/
│   └── 📄 data_cleaner.py      # Script principal de limpeza
├── � data/
│   ├── input/                  # Dados de entrada
│   │   └── produtos_bagunçados_latin1.csv
│   └── output/                 # Dados processados
│       └── produtos_limpos_utf8.csv
├── 📂 APRENDIZADO/             # Versões de estudo
│   ├── 📄 Teste.py             # Versão simplificada para aprendizado
│   ├── 📊 produtos_limpos.csv  # Exemplo de saída de teste
│   └── 📖 README.md            # Documentação de aprendizado
├── 📄 run.py                  # Interface unificada para execução
├── 📖 README.md                # Documentação principal
└── 🔧 .venv/                   # Ambiente virtual Python
    └── Scripts/
        └── python.exe          # Interpretador Python isolado
```

## 🛠️ Tecnologias Utilizadas

- **Python 3.11+**
- **Pandas** - Manipulação e análise de dados
- **Chardet** - Detecção automática de encoding (não manual)
- **io** - Manipulação de fluxos de dados
- **os** - Manipulação de caminhos e arquivos



### 1. Clone ou Baixe o Projeto
```bash
# Se usando Git
git clone <url-do-repositorio>
cd Teste_Fuçar



### 2. Configure o Ambiente Virtual
```powershell
# Criar ambiente virtual (se não existir)
python -m venv .venv

# Ativar ambiente virtual
C:/GoParts/.venv/Scripts/Activate.ps1

# Instalar dependências
pip install pandas chardet
```

### 3. Execute o Script
```powershell
# Executar via interface unificada (recomendado)
python run.py

# Ou executar diretamente o script principal
python src/data_cleaner.py

# Ou executar a versão de aprendizado
python APRENDIZADO/Teste.py
```

## 🎮 Como Usar

### Execução Básica
1. Abra o terminal na raiz do projeto `C:\GoParts`
2. Ative o ambiente virtual: `C:/GoParts/.venv/Scripts/Activate.ps1`
3. Execute o script unificado: `python run.py`
4. Observe a saída detalhada no terminal
5. Verifique o arquivo gerado em `GoParts/data/output/produtos_limpos_utf8.csv`

### Usando Seus Próprios Dados
Para usar seus próprios dados:

1. Substitua o arquivo de entrada em `GoParts/data/input/`
2. Mantenha o mesmo formato CSV com as colunas:
   - nome_produto
   - codigo
   - preco
   - estoque

### Versão de Aprendizado
A versão simplificada em `APRENDIZADO/Teste.py` usa dados embutidos para demonstração:

```python
csv_data = """nome_produto,codigo,preco,estoque
Amortecedor Traseiro,K12345LA,100,50
Pivô de Suspensão,K54321BR,R$100,50
Bomba d'água,K67890US,"100,50",
"""
```

## 📊 Exemplo de Saída

### Dados de Entrada (Brutos)
```
nome_produto          | codigo    | preco        | estoque
 Bieleta              | K45454LA  | "100,50"     | 2
Lanterna Traseira     | K33445EU  | "R$1.250,00" | 
Radiador              | K66666LA  | R$99         | 90
```

### Dados de Saída (Limpos)
```
nome_produto          | codigo    | preco   | estoque
Bieleta              | K45454LA  | 100.50  | 2
Lanterna Traseira    | K33445EU  | 1250.00 | 0
Radiador             | K66666LA  | 99.00   | 90
```

## 🔍 Análise Detalhada do Código

### Funções Principais

#### `detectar_encoding()`
```python
def detectar_encoding(caminho_arquivo):
    """
    Detecta o encoding de um arquivo usando chardet (detecção automática)
    
    Lógica:
    1. Lê os primeiros bytes do arquivo
    2. Usa chardet para analisar o padrão de bytes
    3. Retorna o encoding com maior probabilidade
    4. Inclui porcentagem de confiança da detecção
    """
```

#### `normalizar_preco()`
```python
def normalizar_preco(valor):
    """
    Normaliza valores de preço em diferentes formatos brasileiros.
    
    Lógica:
    1. Verifica se é None ou NaN e retorna 0
    2. Remove símbolos de moeda (R$) e espaços
    3. Detecta formato brasileiro: "1.250,00"
    4. Detecta vírgula decimal: "100,50"
    5. Mantém formato americano: "100.50"
    6. Converte para float ou retorna 0.0 em caso de erro
    """
```

### Etapas de Processamento

1. **🔍 Detecção**: Usa Chardet para detectar automaticamente o encoding do arquivo
2. **📋 Carregamento**: Lê e corrige linhas mal formatadas com colunas extras
3. **💰 Preços**: Normaliza formato monetário brasileiro para padrão americano
4. **📦 Estoque**: Substitui valores inválidos, NaN, None, e -1 por 0
5. **🏷️ Nomes**: Remove espaços extras dos nomes dos produtos
6. **💾 Salvamento**: Exporta dados limpos para CSV em UTF-8
7. **📊 Relatório**: Exibe estatísticas e comparação antes/depois


## 🐛 Solução de Problemas

### Erro: "ModuleNotFoundError: No module named 'pandas' ou 'chardet'"
```powershell
# Ative o ambiente virtual
C:/GoParts/.venv/Scripts/Activate.ps1

# Instale as dependências
pip install pandas chardet
```

### Problemas de Encoding e Acentuação
O sistema usa detecção automática de encoding com chardet e salva em UTF-8, resolvendo problemas de caracteres especiais.

### Arquivo de Entrada não Encontrado
Certifique-se que o arquivo existe em:
```
GoParts/data/input/produtos_bagunçados_latin1.csv
```

### Erro na Execução
Use o script unificado que trata erros automaticamente:
```powershell
python run.py
```
