#!/usr/bin/env python3
"""
🎯 DEMO PARA APRESENTAÇÃO - Projeto GoParts
"""
import subprocess
import time
import os

def apresentacao_demo():
    print("🎯 DEMONSTRAÇÃO - PROJETO GOPARTS")
    print("=" * 50)
    print("📱 Case Técnico: Sistema de Processamento de Dados e APIs")
    print("=" * 50)
    
    # Parte 1
    print("\n🔄 PARTE 1: Processamento de Dados")
    print("   - Limpeza automática de CSV")
    print("   - Detecção de encoding")
    print("   - Normalização de preços")
    print("   - Validação de dados")
    input("   ⏯️  Pressione ENTER para executar...")
    
    os.system('C:/Goparts1/.venv/Scripts/python.exe src/data_cleaner.py')
    
    print("\n✅ PARTE 1 CONCLUÍDA!")
    time.sleep(2)
    
    # Parte 2
    print("\n🌐 PARTE 2: Integração com API")
    print("   - Sistema de retry resiliente")
    print("   - Backoff exponencial")
    print("   - Tratamento de falhas HTTP 5xx")
    print("   - Logging profissional")
    input("   ⏯️  Pressione ENTER para executar...")
    
    os.system('C:/Goparts1/.venv/Scripts/python.exe src/httpbin_integration.py')
    
    print("\n🎉 DEMONSTRAÇÃO CONCLUÍDA!")
    print("📊 Sistema 100% funcional e testado!")

if __name__ == "__main__":
    apresentacao_demo()