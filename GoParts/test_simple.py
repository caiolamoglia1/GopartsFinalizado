#!/usr/bin/env python3
"""
🧪 Teste de integração API - versão simplificada
"""

import requests
import time

print("🔗 Teste de Integração API GoParts")
print("=" * 40)

# Testa conexão com API
try:
    response = requests.get('http://localhost:5000/health', timeout=5)
    if response.status_code == 200:
        print("✅ API local está respondendo")
        health_data = response.json()
        print(f"📊 Status: {health_data.get('status')}")
        print(f"📊 Stats: {health_data.get('stats')}")
    else:
        print(f"❌ API retornou status: {response.status_code}")
except Exception as e:
    print(f"❌ Erro ao conectar: {e}")

# Teste de envio de produto
print("\n📤 Testando envio de produto...")
produto_teste = {
    'nome_produto': 'Produto Teste',
    'codigo': 'TEST001',
    'preco': 99.99,
    'estoque': 10
}

try:
    response = requests.post(
        'http://localhost:5000/produtos',
        json=produto_teste,
        timeout=10
    )
    
    if response.status_code in [200, 201]:
        print("✅ Produto enviado com sucesso!")
        print(f"📊 Resposta: {response.json()}")
    else:
        print(f"❌ Falha ao enviar produto: HTTP {response.status_code}")
        print(f"📊 Resposta: {response.text}")
        
except Exception as e:
    print(f"❌ Erro ao enviar produto: {e}")

print("\n🏁 Teste concluído!")
