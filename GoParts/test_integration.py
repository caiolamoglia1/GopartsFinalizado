#!/usr/bin/env python3
"""
🧪 Script de Teste Simples para GoParts API Integration
"""

print("🧪 GoParts API Integration - Teste Simples")
print("=" * 50)

try:
    # Teste 1: Imports
    print("1️⃣ Testando imports...")
    import pandas as pd
    import requests
    print("   ✅ pandas e requests OK")
    
    # Teste 2: CSV
    print("2️⃣ Testando carregamento do CSV...")
    import os
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CSV_FILE = os.path.join(BASE_DIR, 'data', 'output', 'produtos_limpos_utf8.csv')
    
    if os.path.exists(CSV_FILE):
        df = pd.read_csv(CSV_FILE)
        print(f"   ✅ CSV carregado: {len(df)} produtos")
        print(f"   📄 Arquivo: {CSV_FILE}")
    else:
        print(f"   ❌ CSV não encontrado: {CSV_FILE}")
        
    # Teste 3: Conexão HTTPBin
    print("3️⃣ Testando conexão com HTTPBin...")
    try:
        response = requests.get('https://httpbin.org/status/200', timeout=5)
        if response.status_code == 200:
            print("   ✅ HTTPBin.org acessível")
        else:
            print(f"   ⚠️ HTTPBin retornou: {response.status_code}")
    except Exception as e:
        print(f"   ❌ Erro ao conectar: {e}")
    
    # Teste 4: Estrutura do projeto
    print("4️⃣ Verificando estrutura do projeto...")
    scripts = [
        'src/httpbin_integration.py',
        'src/api_integration.py', 
        'src/test_api.py',
        'api_launcher.py'
    ]
    
    for script in scripts:
        script_path = os.path.join(BASE_DIR, script)
        if os.path.exists(script_path):
            print(f"   ✅ {script}")
        else:
            print(f"   ❌ {script} não encontrado")
    
    print("\n" + "=" * 50)
    print("✅ Teste básico concluído!")
    print("\n💡 Para testar a integração:")
    print("   python src/httpbin_integration.py")
    
except Exception as e:
    print(f"❌ Erro durante o teste: {e}")
    import traceback
    traceback.print_exc()
