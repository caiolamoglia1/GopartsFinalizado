#!/usr/bin/env python3
"""
🚗 GoParts Data Cleaner - Launcher
Script de entrada que redireciona para o projeto principal
"""

import os
import sys
import subprocess

def main():
    # Caminho para o projeto principal
    projeto_path = os.path.join(os.path.dirname(__file__), 'GoParts')
    run_py_path = os.path.join(projeto_path, 'run.py')
    
    if not os.path.exists(run_py_path):
        print("❌ Erro: Projeto GoParts não encontrado!")
        print(f"   Esperado em: {projeto_path}")
        return 1
    
    print("🚀 Redirecionando para GoParts Data Cleaner...")
    print(f"📁 Projeto: {projeto_path}")
    print("-" * 50)
    
    # Executa o run.py do projeto principal
    try:
        os.chdir(projeto_path)
        result = subprocess.run([sys.executable, 'run.py'] + sys.argv[1:])
        return result.returncode
    except Exception as e:
        print(f"❌ Erro ao executar: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
