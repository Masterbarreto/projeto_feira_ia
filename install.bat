@echo off
echo ========================================
echo     AI AGENT - INSTALLATION SETUP
echo ========================================
echo.
echo Installing dependencies...
echo.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
echo.
echo ========================================
echo Installation complete!
echo.
echo Next steps:
echo 1. Configure your Google Gemini API key in src/main.py
echo 2. Run: scripts/start_agent.bat
echo.
pause
