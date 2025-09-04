#!/usr/bin/env python3
"""
🧪 API de Teste para GoParts
API que simula falhas intermitentes para testar retries
"""

from flask import Flask, request, jsonify
import random
import time
import logging

app = Flask(__name__)

# Configuração de logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Estatísticas da API
stats = {
    'total_requests': 0,
    'successful': 0,
    'failed': 0,
    'products_received': []
}

@app.route('/health', methods=['GET'])
def health():
    """Endpoint de saúde da API"""
    return jsonify({
        'status': 'healthy',
        'timestamp': time.time(),
        'stats': stats
    })

@app.route('/produtos', methods=['POST'])
def create_produto():
    """
    Endpoint que simula cadastro de produto com falhas intermitentes
    Falha em aproximadamente 30% das requisições
    """
    stats['total_requests'] += 1
    
    # Simula delay de processamento
    time.sleep(random.uniform(0.1, 0.5))
    
    # 30% de chance de falha
    if random.random() < 0.3:
        stats['failed'] += 1
        error_type = random.choice([500, 502, 503, 504])
        
        logger.warning(f"🔴 Simulando erro {error_type} - Request #{stats['total_requests']}")
        
        error_messages = {
            500: "Erro interno do servidor",
            502: "Bad Gateway",
            503: "Serviço indisponível",
            504: "Gateway Timeout"
        }
        
        return jsonify({
            'error': error_messages.get(error_type, 'Erro desconhecido'),
            'code': error_type,
            'timestamp': time.time(),
            'request_id': stats['total_requests']
        }), error_type
    
    # Sucesso
    stats['successful'] += 1
    produto_data = request.get_json()
    
    if not produto_data:
        return jsonify({'error': 'Dados do produto são obrigatórios'}), 400
    
    # Simula validação
    required_fields = ['nome_produto', 'codigo', 'preco', 'estoque']
    for field in required_fields:
        if field not in produto_data:
            return jsonify({'error': f'Campo obrigatório: {field}'}), 400
    
    # Adiciona timestamp e ID
    produto_data['id'] = stats['total_requests']
    produto_data['created_at'] = time.time()
    
    stats['products_received'].append(produto_data)
    
    logger.info(f"✅ Produto cadastrado: {produto_data['nome_produto']} - Request #{stats['total_requests']}")
    
    return jsonify({
        'message': 'Produto cadastrado com sucesso',
        'produto': produto_data,
        'request_id': stats['total_requests']
    }), 201

@app.route('/stats', methods=['GET'])
def get_stats():
    """Retorna estatísticas da API"""
    success_rate = (stats['successful'] / stats['total_requests']) * 100 if stats['total_requests'] > 0 else 0
    
    return jsonify({
        'total_requests': stats['total_requests'],
        'successful': stats['successful'],
        'failed': stats['failed'],
        'success_rate': f"{success_rate:.1f}%",
        'products_count': len(stats['products_received'])
    })

@app.route('/reset', methods=['POST'])
def reset_stats():
    """Reset das estatísticas"""
    global stats
    stats = {
        'total_requests': 0,
        'successful': 0,
        'failed': 0,
        'products_received': []
    }
    return jsonify({'message': 'Estatísticas resetadas'})

if __name__ == '__main__':
    print("🚀 Iniciando API de Teste GoParts")
    print("📊 Configuração:")
    print("   - Taxa de falha: ~30%")
    print("   - Porta: 5000")
    print("   - Endpoints:")
    print("     GET  /health     - Status da API")
    print("     POST /produtos   - Cadastrar produto")
    print("     GET  /stats      - Estatísticas")
    print("     POST /reset      - Reset estatísticas")
    print("=" * 50)
    
    app.run(host='0.0.0.0', port=5000, debug=False)
