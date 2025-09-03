# 📋 Lista Completa de Comandos e Seus Significados


## 📊 **Comandos Pandas - Manipulação de Dados**

### **Importação e Leitura**
```python
import pandas as pd
```
**Significado**: Importa a biblioteca pandas com o apelido `pd` (convenção padrão).

```python
import io
```
**Significado**: Importa o módulo `io` para trabalhar com fluxos de dados na memória.

```python
df = pd.read_csv(io.StringIO(csv_data))
```
**Significado**: 
- `io.StringIO()`: Transforma uma string em um objeto que simula um arquivo

- `pd.read_csv()`: Lê dados CSV e cria um DataFrame

- `df`: Variável que armazena o DataFrame (tabela de dados)

### **Manipulação de Colunas**
```python
df['preco'] = df['preco'].astype(str)
```
**Significado**: Converte todos os valores da coluna 'preco' para o tipo string (texto).

```python
df['preco'] = df['preco'].apply(normalizar_preco)
```
**Significado**: Aplica a função `normalizar_preco` a cada valor da coluna 'preco'.

```python
df['estoque'] = df['estoque'].replace(valores_invalidos, 0)
```
**Significado**: Substitui todos os valores listados em `valores_invalidos` por 0 na coluna 'estoque'.

```python
df['estoque'] = df['estoque'].fillna(0)
```
**Significado**: Preenche valores vazios (NaN - Not a Number) com 0.

```python
df['estoque'] = df['estoque'].astype(int)
```
**Significado**: Converte toda a coluna 'estoque' para números inteiros.

```python
df['nome_produto'] = df['nome_produto'].str.strip()
```
**Significado**: Remove espaços em branco no início e fim de cada nome de produto.

### **Análise e Estatísticas**
```python
len(df)
```
**Significado**: Retorna o número de linhas (registros) no DataFrame.


```python
df['estoque'].sum()
```
**Significado**: Soma todos os valores da coluna 'estoque'.

### **Visualização**
```python
df.head(5)
```
**Significado**: Mostra apenas as primeiras 5 linhas do DataFrame.

```python
df.to_string()
```
**Significado**: Converte o DataFrame inteiro em uma string formatada como tabela.

### **Exportação**
```python
df.to_csv(output_filename, index=False, encoding='utf-8-sig')
```
**Significado**: 
- `to_csv()`: Salva o DataFrame como arquivo CSV
- `index=False`: Não inclui números de linha no arquivo
- `encoding='utf-8-sig'`: Usa codificação UTF-8 com BOM para caracteres especiais

---

## 🔧 **Comandos de String - Manipulação de Texto**

### **Limpeza e Formatação**
```python
str(valor).strip()
```
**Significado**: Converte para string e remove espaços no início e fim.

```python
s.replace("R$", "")
```
**Significado**: Remove todas as ocorrências de "R$" da string.

```python
s.replace(" ", "")
```
**Significado**: Remove todos os espaços da string.

```python
s.replace(".", "").replace(",", ".")
```
**Significado**: Remove pontos e substitui vírgulas por pontos (conversão BR→US).

### **Verificações**
```python
if not s or s.lower() in {"nan", "none"}:
```
**Significado**: Verifica se a string está vazia OU se contém "nan" ou "none" (em minúsculas).

```python
if "," in s and "." in s:
```
**Significado**: Verifica se a string contém tanto vírgula quanto ponto.

---

## 🖥️ **Comandos de Terminal/PowerShell**

### **Navegação**
```powershell
cd "c:\Teste_Fuçar"
```
**Significado**: Muda o diretório atual para a pasta do projeto.

### **Execução de Scripts**
```powershell
python Teste.py
```
**Significado**: Executa o script Python usando o interpretador padrão do sistema.

```powershell
.\.venv\Scripts\python.exe Teste.py
```
**Significado**: Executa o script usando especificamente o Python do ambiente virtual.

### **Controle de Processos**
```powershell
Ctrl + C
```
**Significado**: Interrompe a execução do comando atual (cancelar).

---



### **Formatação de Strings**
```python
print(f"📊 Total: {len(df)}")
```
**Significado**: f-string - permite inserir variáveis diretamente na string com `{}`.

```python
print(f"💰 Preço: R$ {valor:.2f}")
```
**Significado**: Formata número com 2 casas decimais usando `:.2f`.

### **Elementos Visuais**
```python
print("=" * 60)
```
**Significado**: Imprime 60 sinais de igual (linha decorativa).

```python
print("\n")
```
**Significado**: Imprime uma linha em branco (`\n` = nova linha).

---

## 🔍 **Comandos de Conversão - Tipos de Dados**

### **Conversões Básicas**
```python
float(s)
```
**Significado**: Converte string para número decimal (ponto flutuante).

```python
int(valor)
```
**Significado**: Converte para número inteiro.

```python
str(valor)
```
**Significado**: Converte qualquer tipo para string (texto).

### **Tratamento de Erros**
```python
try:
    return float(s)
except ValueError:
    return 0.0
```
**Significado**: Tenta converter para float; se der erro, retorna 0.0.

---

## 🎯 **Comandos de Lógica - Estruturas de Controle**

### **Condicionais**
```python
if valor is None:
    return 0.0
```
**Significado**: Se o valor for nulo, retorna 0.0.

```python
elif "," in s:
    # fazer algo
```
**Significado**: "Senão, se" - condição adicional caso a primeira seja falsa.

### **Funções**
```python
def normalizar_preco(valor) -> float:
```
**Significado**: Define uma função que recebe `valor` e retorna um `float`.

```python
"""Documentação da função"""
```
**Significado**: Docstring - documentação explicativa da função.

---

## 📁 **Comandos de Arquivo - Sistema**

### **Codificação**
```python
encoding='utf-8-sig'
```
**Significado**: Usa codificação UTF-8 com BOM para suportar acentos em programas como Excel.

---

---


