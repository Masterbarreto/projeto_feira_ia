@echo off
echo ========================================
echo     AGENTE IA - FEIRA DE CIENCIAS
echo ========================================
echo.
echo Iniciando sistema...
echo.
cd /d "%~dp0.."
@.venv\Scripts\python.exe src\main.py
echo.
echo ========================================
echo Sistema encerrado. Pressione qualquer tecla para sair...
pause >nul
