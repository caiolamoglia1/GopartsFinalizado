@echo off
echo.
echo 🚀 CASE TECNICO GOPARTS - SETUP AUTOMATICO
echo =========================================
echo.

REM Verificar se estamos no diretorio correto
if not exist "src\data_cleaner.py" (
    echo ❌ Erro: Execute este script a partir do diretorio principal do projeto
    echo 💡 Navegue para: c:\GoParts\GopartsFinalizado\GoParts
    pause
    exit /b 1
)

echo ✅ Diretorio correto verificado
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python nao encontrado
    echo 💡 Instale Python 3.8+ antes de continuar
    pause
    exit /b 1
)

echo ✅ Python encontrado
python --version
echo.

REM Instalar dependencias
echo 📦 Instalando dependencias...
pip install pandas chardet requests flask
if errorlevel 1 (
    echo ❌ Erro ao instalar dependencias
    pause
    exit /b 1
)

echo ✅ Dependencias instaladas com sucesso
echo.

REM Verificar estrutura de arquivos
echo 🔍 Verificando estrutura do projeto...
if not exist "data\raw\produtos.csv" (
    echo ⚠️  Aviso: Arquivo data\raw\produtos.csv nao encontrado
    echo 💡 Copie o arquivo de dados para continuar
)

if not exist "data\output" mkdir data\output
if not exist "logs" mkdir logs

echo ✅ Estrutura do projeto verificada
echo.

echo 🎉 SETUP CONCLUIDO COM SUCESSO!
echo.
echo 🎯 Para executar o projeto:
echo    python demo_apresentacao.py
echo.
echo 📖 Para documentacao completa:
echo    README_EXECUCAO.md
echo.
pause
