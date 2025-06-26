#!/bin/bash
# Script de instalação para Linux/Raspberry Pi
# Agente IA para Navegação em Feira de Ciências

echo "🚀 Instalando Agente IA para Feira de Ciências..."
echo "📍 Sistema: Linux/Raspberry Pi"

# Verificar se o Python está instalado
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 não encontrado. Instalando..."
    sudo apt update
    sudo apt install -y python3 python3-pip
fi

# Instalar dependências do sistema para áudio
echo "🔧 Instalando dependências de áudio..."
sudo apt update
sudo apt install -y \
    python3-pyaudio \
    portaudio19-dev \
    python3-dev \
    gcc \
    mpg123 \
    alsa-utils \
    pulseaudio

# Criar ambiente virtual
echo "🌿 Criando ambiente virtual..."
python3 -m venv .venv

# Ativar ambiente virtual
echo "🔄 Ativando ambiente virtual..."
source .venv/bin/activate

# Atualizar pip
echo "📦 Atualizando pip..."
pip install --upgrade pip

# Instalar dependências Python
echo "📚 Instalando dependências Python..."
pip install -r requirements.txt

# Teste de microfone
echo "🎤 Testando configuração de áudio..."
python3 scripts/diagnosticar_audio.py

echo ""
echo "✅ Instalação concluída!"
echo ""
echo "📋 Para executar o agente:"
echo "   ./scripts/start_agent.sh"
echo ""
echo "📋 Para executar manualmente:"
echo "   source .venv/bin/activate"
echo "   python3 src/main.py"
echo ""
echo "🔧 Se houver problemas com áudio, execute:"
echo "   python3 scripts/diagnosticar_audio.py"
