#!/usr/bin/env python3
"""
🌐 GoParts API Integration - HTTPBin Version
Script para enviar produtos para httpbin.org simulando uma API REST
"""

import pandas as pd
import requests
import time
import logging
import json
import sys
import os
from typing import Dict, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import random

# Configuração de logging
def setup_logging():
    """Configura o sistema de logging"""
    log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(log_dir, f'httpbin_integration_{timestamp}.log')
    
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file, encoding='utf-8'),
            logging.StreamHandler(sys.stdout)
        ]
    )
    
    return logging.getLogger(__name__), log_file

@dataclass
class RetryConfig:
    """Configurações para retry com backoff exponencial"""
    max_attempts: int = 5
    initial_delay: float = 1.0
    max_delay: float = 32.0
    backoff_factor: float = 2.0

@dataclass
class APIStats:
    """Estatísticas de envio para API"""
    total_products: int = 0
    successful: int = 0
    failed: int = 0
    retries_used: int = 0
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    
    def success_rate(self) -> float:
        if self.total_products == 0:
            return 0.0
        return (self.successful / self.total_products) * 100
    
    def duration(self) -> float:
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0.0

class HTTPBinClient:
    """Cliente que simula falhas usando httpbin.org"""
    
    def __init__(self, retry_config: RetryConfig = None):
        self.retry_config = retry_config or RetryConfig()
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'GoParts-HTTPBin-Client/1.0'
        })
        self.logger = logging.getLogger(__name__)
        self.failure_rate = 0.3  # 30% de falha simulada
    
    def _calculate_delay(self, attempt: int) -> float:
        """Calcula delay para backoff exponencial"""
        delay = self.retry_config.initial_delay * (self.retry_config.backoff_factor ** (attempt - 1))
        return min(delay, self.retry_config.max_delay)
    
    def _simulate_api_failure(self) -> bool:
        """Simula falha da API baseada na taxa de falha"""
        return random.random() < self.failure_rate
    
    def send_produto(self, produto: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """
        Envia produto simulando falhas intermitentes
        Uses httpbin.org/post para simular POST requests
        """
        
        for attempt in range(1, self.retry_config.max_attempts + 1):
            try:
                self.logger.info(f"📤 Enviando produto: {produto['nome_produto']} (tentativa {attempt})")
                
                # Simula falha intermitente
                if self._simulate_api_failure():
                    # Simula diferentes tipos de erro
                    error_codes = [500, 502, 503, 504]
                    simulated_status = random.choice(error_codes)
                    
                    self.logger.warning(f"🔴 Simulando erro HTTP {simulated_status}")
                    
                    if attempt < self.retry_config.max_attempts:
                        delay = self._calculate_delay(attempt)
                        self.logger.warning(f"⚠️ Tentando novamente em {delay:.1f}s...")
                        time.sleep(delay)
                        continue
                    else:
                        return False, {
                            'error': f'Simulated HTTP {simulated_status}',
                            'attempts': attempt
                        }
                
                # Envia para httpbin.org (sempre retorna 200)
                response = self.session.post(
                    'https://httpbin.org/post',
                    json={
                        'produto': produto,
                        'timestamp': datetime.now().isoformat(),
                        'attempt': attempt
                    },
                    timeout=10
                )
                
                if response.status_code == 200:
                    self.logger.info(f"✅ Produto enviado com sucesso: {produto['codigo']}")
                    return True, {
                        'message': 'Produto enviado com sucesso',
                        'httpbin_response': response.json(),
                        'attempts': attempt
                    }
                
            except (requests.Timeout, requests.ConnectionError) as e:
                if attempt < self.retry_config.max_attempts:
                    delay = self._calculate_delay(attempt)
                    self.logger.warning(f"⚠️ Erro de conexão: {str(e)}, tentando novamente em {delay:.1f}s...")
                    time.sleep(delay)
                    continue
                
                self.logger.error(f"❌ Erro de conexão definitivo: {str(e)}")
                return False, {
                    'error': 'ConnectionError',
                    'message': str(e),
                    'attempts': attempt
                }
            
            except Exception as e:
                self.logger.error(f"❌ Erro inesperado: {str(e)}")
                return False, {
                    'error': 'UnexpectedError',
                    'message': str(e),
                    'attempts': attempt
                }
        
        return False, {'error': 'MaxAttemptsExceeded', 'attempts': self.retry_config.max_attempts}
    
    def test_connection(self) -> bool:
        """Testa conexão com httpbin.org"""
        try:
            response = self.session.get('https://httpbin.org/status/200', timeout=5)
            return response.status_code == 200
        except:
            return False

def load_produtos_csv(file_path: str) -> pd.DataFrame:
    """Carrega produtos do CSV limpo"""
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
        return df
    except Exception as e:
        raise Exception(f"Erro ao carregar CSV: {e}")

def main():
    """Função principal"""
    logger, log_file = setup_logging()
    
    print("🌐 GoParts HTTPBin Integration v1.0")
    print("=" * 50)
    
    # Configurações
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CSV_FILE = os.path.join(BASE_DIR, 'data', 'output', 'produtos_limpos_utf8.csv')
    
    # Configuração de retry
    retry_config = RetryConfig(
        max_attempts=5,
        initial_delay=1.0,
        backoff_factor=2.0,
        max_delay=16.0
    )
    
    logger.info(f"📁 Arquivo CSV: {CSV_FILE}")
    logger.info(f"🌐 API: httpbin.org (simulando falhas)")
    logger.info(f"📝 Log file: {log_file}")
    logger.info(f"🔄 Retry config: max_attempts={retry_config.max_attempts}, backoff={retry_config.backoff_factor}x")
    logger.info(f"💥 Taxa de falha simulada: 30%")
    
    try:
        # Carrega produtos
        logger.info("📊 Carregando produtos do CSV...")
        df = load_produtos_csv(CSV_FILE)
        logger.info(f"✅ {len(df)} produtos carregados")
        
        # Cria cliente
        client = HTTPBinClient(retry_config)
        
        # Testa conexão
        logger.info("🔍 Testando conexão com httpbin.org...")
        if not client.test_connection():
            logger.error("❌ Não foi possível conectar ao httpbin.org")
            return 1
        
        logger.info("✅ Conexão com httpbin.org estabelecida")
        
        # Estatísticas
        stats = APIStats()
        stats.total_products = len(df)
        stats.start_time = datetime.now()
        
        # Processa cada produto
        logger.info(f"🚀 Iniciando envio de {len(df)} produtos...")
        
        failed_products = []
        
        for index, row in df.iterrows():
            produto = {
                'nome_produto': row['nome_produto'],
                'codigo': row['codigo'],
                'preco': float(row['preco']),
                'estoque': int(row['estoque'])
            }
            
            success, response = client.send_produto(produto)
            
            if success:
                stats.successful += 1
            else:
                stats.failed += 1
                failed_products.append({
                    'produto': produto,
                    'error': response
                })
                
                # Log do erro
                error_msg = response.get('message', response.get('error', 'Erro desconhecido'))
                attempts = response.get('attempts', 'N/A')
                logger.error(f"❌ Falha ao enviar {produto['codigo']}: {error_msg} (tentativas: {attempts})")
            
            # Pequena pausa entre envios
            time.sleep(0.2)
        
        stats.end_time = datetime.now()
        
        # Relatório final
        print("\n" + "=" * 60)
        print("📊 RELATÓRIO FINAL - HTTPBin Integration")
        print("=" * 60)
        print(f"⏱️  Duração total: {stats.duration():.1f}s")
        print(f"📦 Total de produtos: {stats.total_products}")
        print(f"✅ Enviados com sucesso: {stats.successful}")
        print(f"❌ Falhas: {stats.failed}")
        print(f"📈 Taxa de sucesso: {stats.success_rate():.1f}%")
        print(f"💥 Taxa de falha esperada: ~30%")
        
        logger.info(f"📊 RESUMO: {stats.successful}/{stats.total_products} produtos enviados ({stats.success_rate():.1f}% sucesso)")
        
        # Log de produtos que falharam
        if failed_products:
            print(f"\n❌ Produtos que falharam ({len(failed_products)}):")
            for item in failed_products[:5]:  # Mostra apenas os primeiros 5
                produto = item['produto']
                error = item['error']
                print(f"   - {produto['codigo']} ({produto['nome_produto']}): {error.get('error', 'Erro desconhecido')}")
            
            if len(failed_products) > 5:
                print(f"   ... e mais {len(failed_products) - 5} produtos")
        
        print(f"\n📝 Log completo salvo em: {log_file}")
        print("=" * 60)
        
        return 0
        
    except Exception as e:
        logger.error(f"❌ Erro fatal: {e}")
        print(f"❌ Erro: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
