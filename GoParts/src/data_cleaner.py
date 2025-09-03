import pandas as pd
import os
import chardet  # Importação direta do chardet para detecção automática (não manual)

print("✅ Chardet disponível - usando detecção automática de encoding")

# Função para detectar encoding do arquivo
def detectar_encoding(caminho_arquivo):
    """
    Detecta o encoding de um arquivo usando chardet (detecção automática)
    """
    print("🔍 Usando chardet para detecção automática...")
    with open(caminho_arquivo, 'rb') as file:
        raw_data = file.read(10000)  # Lê os primeiros 10KB
        resultado = chardet.detect(raw_data)
        encoding_detectado = resultado['encoding']
        confianca = resultado['confidence']
        print(f"   📊 Encoding detectado: {encoding_detectado} (confiança: {confianca:.2%})")
        return encoding_detectado

# Define o diretório base do projeto
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INPUT_FILE = os.path.join(BASE_DIR, 'data', 'input', 'produtos_bagunçados_latin1.csv')
OUTPUT_FILE = os.path.join(BASE_DIR, 'data', 'output', 'produtos_limpos_utf8.csv')

# Detecta o encoding usando chardet (automaticamente)
encoding_detectado = detectar_encoding(INPUT_FILE)
# Prioriza o encoding detectado, mas mantém outros como fallback
encodings_para_testar = [encoding_detectado, 'utf-8', 'latin1', 'iso-8859-1']  

for encoding in encodings_para_testar:
    try:
        print(f"🔍 Tentando encoding: {encoding}")
        # Lê linha por linha para tratar inconsistências manualmente
        linhas = []
        with open(INPUT_FILE, 'r', encoding=encoding) as file:
            for i, linha in enumerate(file):
                if i == 0:  # Header
                    linhas.append(linha.strip())
                    continue
                
                # Divide a linha em campos
                campos = linha.strip().split(',')
                
                # Se há mais de 4 campos, junta os extras no campo 'estoque'
                if len(campos) > 4:
                    # Mantém nome_produto, codigo, preco
                    nome_produto = campos[0]
                    codigo = campos[1] 
                    preco = campos[2]
                    # Junta todos os campos restantes como estoque (pega o último válido)
                    estoque = campos[3] if campos[3].strip() else (campos[4] if len(campos) > 4 and campos[4].strip() else '')
                    
                    linha_corrigida = f"{nome_produto},{codigo},{preco},{estoque}"
                    linhas.append(linha_corrigida)
                else:
                    linhas.append(linha.strip())
        
        # Agora cria o DataFrame a partir das linhas corrigidas
        import io
        csv_corrigido = '\n'.join(linhas)
        df = pd.read_csv(io.StringIO(csv_corrigido))
        
        print(f"✅ Arquivo carregado com encoding: {encoding}")
        print(f"📊 Exemplo de nome: {df['nome_produto'].iloc[1]}")
        break
        
    except (UnicodeDecodeError, FileNotFoundError) as e:
        print(f"❌ Erro com {encoding}: {e}")
        continue
else:
    print("❌ Nenhum encoding funcionou!")
    exit()

print(f"\n📊 Dados ANTES da limpeza ({len(df)} produtos):")
print("Estrutura das colunas:", list(df.columns))
print(df.to_string())

def normalizar_preco(valor) -> float:
    """Normaliza valores de preço em diferentes formatos"""
    # Verifica se o valor é nulo, NaN ou vazio
    if valor is None or pd.isna(valor) or valor == '':
        return 0.0
    
    s = str(valor).strip()
    # Verifica valores inválidos (incluindo representações de NaN)
    if not s or s.lower() in {"nan", "none", "null", "n/a", "na"}:
        return 0.0
    
    # Remove R$ e espaços
    s = s.replace("R$", "").replace(" ", "")
    
    # Corrige formato brasileiro: 1.250,00 -> 1250.00
    if "," in s and "." in s:
        s = s.replace(".", "").replace(",", ".")
        print(f"  🔄 Formato brasileiro: {valor} → {s}")
    elif "," in s:
        s = s.replace(",", ".")
        print(f"  🔄 Vírgula decimal: {valor} → {s}")
    
    try:
        return float(s)
    except ValueError:
        print(f"  ⚠️ Erro ao converter: {valor}")
        return 0.0

print("\n💰 Normalizando preços...")
# Conta quantos NaN temos antes
nan_count_preco = df['preco'].isna().sum()
if nan_count_preco > 0:
    print(f"  📊 Encontrados {nan_count_preco} valores NaN em preços - convertendo para 0.0")
    
df['preco'] = df['preco'].apply(normalizar_preco)

print("\n📦 Limpando estoque...")
# Conta quantos NaN temos antes
nan_count_estoque = df['estoque'].isna().sum()
if nan_count_estoque > 0:
    print(f"  📊 Encontrados {nan_count_estoque} valores NaN em estoque - convertendo para 0")

# Valores inválidos para o estoque (incluindo todas as representações de NaN)
valores_invalidos = ['None', 'n/a', 'N/A', 'nan', 'NaN', 'null', 'NULL', 'na', 'NA', -1, '-1', '', ' ']
df['estoque'] = df['estoque'].replace(valores_invalidos, 0)
# Preenche NaN com 0 (valores vazios no CSV)  
df['estoque'] = df['estoque'].fillna(0)
# Converte para numérico, colocando 0 para valores que não conseguir converter
df['estoque'] = pd.to_numeric(df['estoque'], errors='coerce').fillna(0).astype(int)

print("\n🏷️ Limpando nomes dos produtos...")
df['nome_produto'] = df['nome_produto'].str.strip()

# Salva com encoding UTF-8 para preservar acentos
df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')

print("\n" + "=" * 60)
print(f"\n🔍 Dados DEPOIS da limpeza ({len(df)} produtos):")
print(df.to_string())
print(f"\n✅ Arquivo salvo como: {OUTPUT_FILE}")
print("\n" + "=" * 60)

