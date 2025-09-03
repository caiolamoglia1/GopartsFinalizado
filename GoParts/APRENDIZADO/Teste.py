
import pandas as pd  # Biblioteca principal para manipulação de dados
import io           # Biblioteca para trabalhar com fluxos de dados na memória

csv_data = """nome_produto,codigo,preco,estoque
Amortecedor ,K12345LA,100,10
Pivô de Suspensão,K54321BR,R$100,-1
Bomba d'Água,K67890US,100.5,
Embreagem,K11223EU,R$ 250,None
Lâmpada,K99887BR,75,0
Filtro de Óleo,K55667LA,10,n/a
Para-choque,K77889US,1.25,20
Lanterna Traseira,K33445EU,"R$1.250,00",
Velocímetro,K11111BR,89,9
Freio Dianteiro,K22222LA,1050.7,15
Kit Correia,K33333US,"R$ 1.050",70
Coxim do Motor,K44444EU,55,0
Junta Homocinética,K55555BR,99,-1
Radiador ,K66666LA,R$99,90
Disco de Freio,K77777US,199.5,
Pastilha de Freio,K88888EU,"R$ 200,00",None
Sensor de Rotação,K99999BR,300,0
Bobina de Ignição,K12121LA,25,n/a
Válvula Termostática,K23232US,10,5
Reservatório de Água,K34343EU,R$ 75,-1
 Bieleta  ,K45454LA,"100,50",2
 Junta Tampa Válvulas,K19191BR,R$ 80.50,-1
 Vela de Ignição,K78787US,25,None
 """


# io.StringIO() transforma a string em um "arquivo" que o pandas pode ler
df = pd.read_csv(io.StringIO(csv_data))


print("\n📊 Visualização dos dados ANTES da limpeza:")
print(df.to_string())  # Mostra todos os dados


# verificar os tipos de dados a serem substituídos #
def normalizar_preco(valor) -> float:
    """
    Função para normalizar valores de preço em diferentes formatos.
    
    Exemplos de entrada:
    - 100 → 100.0
    - "R$100" → 100.0  
    - "100,50" → 100.5
    - "R$1.250,00" → 1250.0
    - "R$ 200,00" → 200.0
    
    Retorna:
    - float: Valor numérico limpo
    - 0.0: Se for null ou inválido
    """
   
    # Verifica se o valor é nulo
    if valor is None:
        return 0.0
    
    # Converte para string e remove espaços das extremidades
    s = str(valor).strip()
    
    # Verifica se é vazio ou contém valores inválidos
    if not s or s.lower() in {"nan", "none"}:
        return 0.0
    
    # Remove (R$) e espaços internos
    s = s.replace("R$", "").replace(" ", "")
    
    
    # COMO interpretar pontos e vírgulas

    if "," in s and "." in s:
        # Caso: "1.250,00" 
        # Ponto = separador de milhares, Vírgula = separador decimal
        s = s.replace(".", "").replace(",", ".")
        print(f"  🔄 Convertendo formato brasileiro: {valor} → {s}")
        
    elif "," in s:
        # Caso: "100,50" (vírgula como decimal)
        s = s.replace(",", ".")
        print(f"  🔄 Convertendo vírgula decimal: {valor} → {s}")
        
    
    # Tenta converter para número
    try:
        resultado = float(s)
        return resultado
    except ValueError:
        print(f"  ⚠️  Erro ao converter '{valor}' - usando 0.0")
        return 0.0

print("\n" + "=" * 60)
# Aplica a função de normalização em toda a coluna

df['preco'] = df['preco'].astype(str)  # Garante que tudo seja string primeiro
df['preco'] = df['preco'].apply(normalizar_preco)



# Define quais valores considerar inválidos
valores_invalidos = ['None', 'n/a', -1, '-1']


# Substitui valores inválidos por 0
df['estoque'] = df['estoque'].replace(valores_invalidos, 0)

# Preenche campos vazios (NaN) com 0
df['estoque'] = df['estoque'].fillna(0)

# Converte toda a coluna para números inteiros
df['estoque'] = df['estoque'].astype(int)


#LIMPEZA DA COLUNA 'NOME_PRODUTO'

# Remove espaços extras no início e fim dos nomes
# Exemplo: " Bieleta  " → "Bieleta"
df['nome_produto'] = df['nome_produto'].str.strip()

# PASSO 7: SALVAR DADOS LIMPOS
# ============================

output_filename = 'produtos_limpos.csv'
df.to_csv(output_filename, index=False, encoding='utf-8-sig')

# PASSO 8: EXIBIR RESULTADOS
# ==========================
print("\n" + "=" * 60)

print("\n🔍 Pré-visualização dos dados limpos:")
print(df.to_string())

print("\n" + "=" * 60)
