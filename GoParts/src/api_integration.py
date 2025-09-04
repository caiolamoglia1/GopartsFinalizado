#!/usr/bin/env python3
"""
🔗 GoParts API Integration
Script para enviar produtos limpos para API REST com retries e backoff exponencial
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

# Configuração de logging
def setup_logging():
    """Configura o sistema de logging"""
    # Cria diretório de logs se não existir
    log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
    os.makedirs(log_dir, exist_ok=True)
    
    # Nome do arquivo de log com timestamp
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    log_file = os.path.join(log_dir, f'api_integration_{timestamp}.log')
    
    # Configuração do logging
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
    initial_delay: float = 1.0  # segundos
    max_delay: float = 32.0     # segundos
    backoff_factor: float = 2.0
    retry_on_status: list = None
    
    def __post_init__(self):
        if self.retry_on_status is None:
            self.retry_on_status = [500, 502, 503, 504, 408]  # Códigos para retry

@dataclass
class APIStats:
    """Estatísticas de envio para API"""
    total_products: int = 0
    successful: int = 0
    failed: int = 0
    retries_used: int = 0
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    
    def add_success(self):
        self.successful += 1
    
    def add_failure(self):
        self.failed += 1
    
    def add_retry(self):
        self.retries_used += 1
    
    def success_rate(self) -> float:
        if self.total_products == 0:
            return 0.0
        return (self.successful / self.total_products) * 100
    
    def duration(self) -> float:
        if self.start_time and self.end_time:
            return (self.end_time - self.start_time).total_seconds()
        return 0.0

class APIClient:
    """Cliente para comunicação com API REST com retry automático"""
    
    def __init__(self, base_url: str, retry_config: RetryConfig = None):
        self.base_url = base_url.rstrip('/')
        self.retry_config = retry_config or RetryConfig()
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'GoParts-Client/1.0'
        })
        self.logger = logging.getLogger(__name__)
    
    def _calculate_delay(self, attempt: int) -> float:
        """Calcula delay para backoff exponencial"""
        delay = self.retry_config.initial_delay * (self.retry_config.backoff_factor ** (attempt - 1))
        return min(delay, self.retry_config.max_delay)
    
    def _should_retry(self, response: requests.Response = None, exception: Exception = None) -> bool:
        """Determina se deve tentar novamente"""
        if exception:
            # Retry em timeouts e connection errors
            return isinstance(exception, (requests.Timeout, requests.ConnectionError))
        
        if response:
            return response.status_code in self.retry_config.retry_on_status
        
        return False
    
    def send_produto(self, produto: Dict[str, Any]) -> Tuple[bool, Dict[str, Any]]:
        """
        Envia produto para API com retry automático
        Returns: (sucesso: bool, resposta: dict)
        """
        url = f"{self.base_url}/produtos"
        
        for attempt in range(1, self.retry_config.max_attempts + 1):
            try:
                self.logger.info(f"📤 Enviando produto: {produto['nome_produto']} (tentativa {attempt})")
                
                response = self.session.post(
                    url,
                    json=produto,
                    timeout=10  # 10 segundos de timeout
                )
                
                # Sucesso
                if response.status_code in [200, 201]:
                    self.logger.info(f"✅ Produto enviado com sucesso: {produto['codigo']} (HTTP {response.status_code})")
                    return True, response.json()
                
                # Verifica se deve tentar novamente
                if self._should_retry(response=response) and attempt < self.retry_config.max_attempts:
                    delay = self._calculate_delay(attempt)
                    self.logger.warning(f"⚠️ Erro HTTP {response.status_code}, tentando novamente em {delay:.1f}s...")
                    time.sleep(delay)
                    continue
                
                # Falha definitiva
                self.logger.error(f"❌ Falha definitiva: HTTP {response.status_code} - {response.text}")
                return False, {
                    'error': f'HTTP {response.status_code}',
                    'message': response.text,
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
        """Testa conexão com a API"""
        try:
            response = self.session.get(f"{self.base_url}/health", timeout=5)
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
    
    print("🔗 GoParts API Integration v1.0")
    print("=" * 50)
    
    # Configurações
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    CSV_FILE = os.path.join(BASE_DIR, 'data', 'output', 'produtos_limpos_utf8.csv')
    API_URL = "http://localhost:5000"  # URL da API de teste
    
    # Configuração de retry
    retry_config = RetryConfig(
        max_attempts=5,
        initial_delay=1.0,
        backoff_factor=2.0,
        max_delay=16.0
    )
    
    logger.info(f"📁 Arquivo CSV: {CSV_FILE}")
    logger.info(f"🌐 API URL: {API_URL}")
    logger.info(f"📝 Log file: {log_file}")
    logger.info(f"🔄 Retry config: max_attempts={retry_config.max_attempts}, backoff={retry_config.backoff_factor}x")
    
    try:
        # Carrega produtos
        logger.info("📊 Carregando produtos do CSV...")
        df = load_produtos_csv(CSV_FILE)
        logger.info(f"✅ {len(df)} produtos carregados")
        
        # Cria cliente API
        client = APIClient(API_URL, retry_config)
        
        # Testa conexão
        logger.info("🔍 Testando conexão com API...")
        if not client.test_connection():
            logger.warning("⚠️ API não está respondendo. Certifique-se de que está executando.")
            print("\n💡 Para iniciar a API de teste, execute em outro terminal:")
            print(f"   cd \"{os.path.dirname(os.path.abspath(__file__))}\"")
            print("   python test_api.py")
            return 1
        
        logger.info("✅ Conexão com API estabelecida")
        
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
                stats.add_success()
            else:
                stats.add_failure()
                failed_products.append({
                    'produto': produto,
                    'error': response
                })
                
                # Log do erro
                error_msg = response.get('message', 'Erro desconhecido')
                attempts = response.get('attempts', 'N/A')
                logger.error(f"❌ Falha ao enviar {produto['codigo']}: {error_msg} (tentativas: {attempts})")
            
            # Pequena pausa entre envios
            time.sleep(0.1)
        
        stats.end_time = datetime.now()
        
        # Relatório final
        print("\n" + "=" * 60)
        print("📊 RELATÓRIO FINAL")
        print("=" * 60)
        print(f"⏱️  Duração total: {stats.duration():.1f}s")
        print(f"📦 Total de produtos: {stats.total_products}")
        print(f"✅ Enviados com sucesso: {stats.successful}")
        print(f"❌ Falhas: {stats.failed}")
        print(f"📈 Taxa de sucesso: {stats.success_rate():.1f}%")
        print(f"🔄 Total de retries: {stats.retries_used}")
        
        logger.info(f"📊 RESUMO: {stats.successful}/{stats.total_products} produtos enviados ({stats.success_rate():.1f}% sucesso)")
        
        # Log de produtos que falharam
        if failed_products:
            print(f"\n❌ Produtos que falharam ({len(failed_products)}):")
            for item in failed_products:
                produto = item['produto']
                error = item['error']
                print(f"   - {produto['codigo']} ({produto['nome_produto']}): {error.get('error', 'Erro desconhecido')}")
        
        print(f"\n📝 Log completo salvo em: {log_file}")
        print("=" * 60)
        
        return 0 if stats.failed == 0 else 1
        
    except Exception as e:
        logger.error(f"❌ Erro fatal: {e}")
        print(f"❌ Erro: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(main())
