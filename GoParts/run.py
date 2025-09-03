#!/usr/bin/env python3
"""
🚗 GoParts Data Cleaner
Script principal para execução do sistema de limpeza de dados

Uso:
    python run.py              # Executa limpeza padrão
    python run.py --help       # Mostra ajuda
"""

import sys
import os
import argparse

def main():
    parser = argparse.ArgumentParser(description='GoParts Data Cleaner')
    parser.add_argument('--input', '-i', help='Arquivo CSV de entrada')
    parser.add_argument('--output', '-o', help='Arquivo CSV de saída')
    parser.add_argument('--verbose', '-v', action='store_true', help='Modo verboso')
    
    args = parser.parse_args()
    
    # Adiciona o diretório src ao path
    sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

    try:
        import subprocess
        
        print("🚀 GoParts Data Cleaner v1.0")
        print("=" * 50)
        
        # Monta o comando
        cmd = [sys.executable, os.path.join(os.path.dirname(__file__), 'src', 'data_cleaner.py')]
        
        # Executa o script de limpeza
        result = subprocess.run(cmd, capture_output=False)
        
        if result.returncode == 0:
            print("=" * 50)
            print("✅ Processamento concluído com sucesso!")
            print("📁 Arquivo limpo salvo em: data/output/produtos_limpos_utf8.csv")
            print("🔍 Para visualizar: code data/output/produtos_limpos_utf8.csv")
        else:
            print("❌ Erro durante o processamento")
            return 1
            
    except KeyboardInterrupt:
        print("\n⚠️ Operação cancelada pelo usuário")
        return 1
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
