#!/bin/bash
# Script de execução para Linux/Raspberry Pi
# Agente IA para Navegação em Feira de Ciências

echo "🤖 Iniciando Agente IA para Feira de Ciências..."

# Verificar se o ambiente virtual existe
if [ ! -d ".venv" ]; then
    echo "❌ Ambiente virtual não encontrado!"
    echo "🔧 Execute primeiro: ./install.sh"
    exit 1
fi

# Ativar ambiente virtual
source .venv/bin/activate

# Verificar se as dependências estão instaladas
if ! python3 -c "import speech_recognition, gtts, google.generativeai, pandas" 2>/dev/null; then
    echo "❌ Dependências não instaladas!"
    echo "🔧 Execute primeiro: ./install.sh"
    exit 1
fi

# Executar o agente
echo "🚀 Executando o agente..."
python3 src/main.py
