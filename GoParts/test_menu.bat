@echo off
echo.
echo 🧪 GoParts API Integration - Guia de Testes
echo =====================================================
echo.
echo Escolha uma opcao de teste:
echo.
echo 1. 🌐 Teste com HTTPBin.org (Recomendado)
echo 2. 🏠 Teste com API Local
echo 3. 🔧 Iniciar API de Teste
echo 4. 📋 Teste de Verificacao
echo 5. 📊 Ver Logs
echo.
set /p choice="Digite sua escolha (1-5): "

if "%choice%"=="1" goto httpbin
if "%choice%"=="2" goto local
if "%choice%"=="3" goto start_api
if "%choice%"=="4" goto verify
if "%choice%"=="5" goto logs
echo Opcao invalida!
goto end

:httpbin
echo.
echo 🌐 Executando teste com HTTPBin.org...
echo ====================================
echo.
C:/GoParts/.venv/Scripts/python.exe src/httpbin_integration.py
goto end

:local
echo.
echo 🏠 Executando teste com API Local...
echo ==================================
echo IMPORTANTE: Certifique-se de que a API esta rodando!
echo Para iniciar a API, escolha a opcao 3 em outro terminal.
echo.
pause
C:/GoParts/.venv/Scripts/python.exe src/api_integration.py
goto end

:start_api
echo.
echo 🔧 Iniciando API de Teste...
echo ==========================
echo A API sera iniciada na porta 5000
echo Para parar, pressione Ctrl+C
echo.
C:/GoParts/.venv/Scripts/python.exe src/test_api.py
goto end

:verify
echo.
echo 📋 Executando verificacao...
echo ==========================
C:/GoParts/.venv/Scripts/python.exe test_integration.py
goto end

:logs
echo.
echo 📊 Listando logs disponiveis...
echo =============================
dir logs\*.log
echo.
echo Para ver um log especifico, use:
echo type logs\nome_do_arquivo.log
goto end

:end
echo.
echo Teste concluido!
pause
