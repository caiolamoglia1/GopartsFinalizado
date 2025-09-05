#!/usr/bin/env python3
"""
Teste rápido da API GoParts
"""
import requests
import time
import json

def testar_api():
    print("🧪 Teste da API GoParts")
    print("=" * 40)
    
    try:
        # Teste 1: Health check
        print("1️⃣ Testando endpoint /health...")
        response = requests.get('http://localhost:5000/health', timeout=5)
        if response.status_code == 200:
            print("   ✅ API está online!")
            data = response.json()
            print(f"   📊 Stats: {data.get('stats', {})}")
        else:
            print(f"   ❌ API retornou status {response.status_code}")
            return False
            
        # Teste 2: Enviar um produto
        print("\n2️⃣ Testando envio de produto...")
        produto_teste = {
            "nome_produto": "Amortecedor Teste",
            "codigo": "TEST001",
            "preco": 150.00,
            "estoque": 10
        }
        
        response = requests.post(
            'http://localhost:5000/produtos',
            json=produto_teste,
            timeout=5
        )
        
        if response.status_code == 201:
            print("   ✅ Produto enviado com sucesso!")
            print(f"   📦 Resposta: {response.json()}")
        else:
            print(f"   ⚠️ Resposta: {response.status_code} - {response.text}")
        
        # Teste 3: Estatísticas
        print("\n3️⃣ Verificando estatísticas...")
        response = requests.get('http://localhost:5000/stats', timeout=5)
        if response.status_code == 200:
            stats = response.json()
            print("   📊 Estatísticas atuais:")
            for key, value in stats.items():
                print(f"      {key}: {value}")
        
        print("\n✅ Teste da API concluído!")
        return True
        
    except requests.ConnectionError:
        print("❌ Erro: Não foi possível conectar à API")
        print("💡 Certifique-se de que a API está rodando em http://localhost:5000")
        return False
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return False

if __name__ == "__main__":
    testar_api()
