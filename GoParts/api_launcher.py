#!/usr/bin/env python3
"""
🚀 GoParts API Integration Launcher
Script principal para executar integração com API
"""

import sys
import os
import subprocess
import argparse

def print_banner():
    """Exibe banner do programa"""
    print("🔗 GoParts API Integration Suite v1.0")
    print("=" * 50)
    print("Opções disponíveis:")
    print("  1. 🧪 API Local (Flask) - Falhas simuladas")
    print("  2. 🌐 HTTPBin.org - Simulação externa")
    print("  3. 🔧 Iniciar API de teste")
    print("=" * 50)

def check_api_running():
    """Verifica se a API local está rodando"""
    try:
        import requests
        response = requests.get('http://localhost:5000/health', timeout=2)
        return response.status_code == 200
    except:
        return False

def start_test_api():
    """Inicia a API de teste"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    api_script = os.path.join(script_dir, 'test_api.py')
    
    print("🧪 Iniciando API de teste...")
    print("📋 Para parar a API, pressione Ctrl+C")
    print("-" * 30)
    
    try:
        subprocess.run([sys.executable, api_script])
    except KeyboardInterrupt:
        print("\n⚠️ API interrompida pelo usuário")

def run_local_api_integration():
    """Executa integração com API local"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    integration_script = os.path.join(script_dir, 'api_integration.py')
    
    # Verifica se API está rodando
    if not check_api_running():
        print("⚠️ API local não está rodando!")
        print("\n💡 Para iniciar a API de teste:")
        print("   Opção 1: Execute este script com --start-api")
        print("   Opção 2: Em outro terminal, execute:")
        print(f"            python {os.path.join(script_dir, 'test_api.py')}")
        print("\n   Depois execute novamente a integração.")
        return 1
    
    print("✅ API local detectada, iniciando integração...")
    return subprocess.run([sys.executable, integration_script]).returncode

def run_httpbin_integration():
    """Executa integração com HTTPBin"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    httpbin_script = os.path.join(script_dir, 'httpbin_integration.py')
    
    print("🌐 Iniciando integração com HTTPBin.org...")
    return subprocess.run([sys.executable, httpbin_script]).returncode

def main():
    """Função principal"""
    parser = argparse.ArgumentParser(description='GoParts API Integration Launcher')
    parser.add_argument('--mode', choices=['local', 'httpbin', 'start-api'], 
                       help='Modo de execução')
    parser.add_argument('--start-api', action='store_true', 
                       help='Inicia apenas a API de teste')
    
    args = parser.parse_args()
    
    # Se foi passado --start-api, inicia apenas a API
    if args.start_api or args.mode == 'start-api':
        start_test_api()
        return 0
    
    # Se foi especificado um modo, executa diretamente
    if args.mode == 'local':
        return run_local_api_integration()
    elif args.mode == 'httpbin':
        return run_httpbin_integration()
    
    # Modo interativo
    print_banner()
    
    while True:
        try:
            choice = input("\n🔸 Escolha uma opção (1-3) ou 'q' para sair: ").strip()
            
            if choice.lower() in ['q', 'quit', 'exit']:
                print("👋 Até logo!")
                break
            
            elif choice == '1':
                print("\n🧪 Executando integração com API local...")
                run_local_api_integration()
                
            elif choice == '2':
                print("\n🌐 Executando integração com HTTPBin...")
                run_httpbin_integration()
                
            elif choice == '3':
                print("\n🔧 Iniciando API de teste...")
                start_test_api()
                
            else:
                print("❌ Opção inválida! Digite 1, 2, 3 ou 'q'")
                
        except KeyboardInterrupt:
            print("\n\n👋 Programa interrompido pelo usuário")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
