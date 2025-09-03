# 📚 APRENDIZADO - Versões de Estudo

Esta pasta contém os arquivos relacionados ao **aprendizado e desenvolvimento** do projeto GoParts.

## 📁 Arquivos inclusos:

### 🧪 `Teste.py`
- **Propósito**: Versão inicial de aprendizado
- **Características**:
  - Usa dados **hardcoded** (string interna)
  - Lógica básica de limpeza de dados
  - Boa para **entender conceitos fundamentais**
  - Não trata problemas de encoding

### 📊 `produtos_limpos.csv`
- **Gerado por**: `Teste.py`
- **Conteúdo**: 23 produtos com dados simulados (0-22).
- **Encoding**: UTF-8
- **Propósito**: Resultado do script de aprendizado

---

## 🎯 Diferença para a versão principal:

| Aspecto | APRENDIZADO/Teste.py | src/data_cleaner.py (principal) |
|---------|---------------------|------------------------------|
| **Dados** |   String interna    | Arquivo CSV real |
| **Encoding** | Não considera | Detecção automática |
| **Vírgulas extras** | Não trata | Corrige inconsistências |
| **Robustez** | Básica | Avançada |
| **Uso** | 📚 Aprendizado | 🚀 Produção |


## 💡 Para que serve esta pasta:



**💭 Nota**: Os arquivos desta pasta são mantidos para fins educacionais e de comparação. A versão principal do projeto está no arquivo `src/data_cleaner.py`.
