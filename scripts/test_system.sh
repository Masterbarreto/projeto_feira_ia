#!/bin/bash
# Script de teste rápido para verificar se tudo está funcionando

echo "🧪 TESTE RÁPIDO DO SISTEMA"
echo "========================="

# Verificar se estamos no diretório correto
if [ ! -f "src/main.py" ]; then
    echo "❌ Execute este script no diretório raiz do projeto"
    exit 1
fi

# Verificar Python
echo "🐍 Verificando Python..."
python3 --version

# Verificar ambiente virtual
if [ ! -d ".venv" ]; then
    echo "❌ Ambiente virtual não encontrado. Execute ./install.sh primeiro"
    exit 1
fi

# Ativar ambiente virtual
source .venv/bin/activate

# Verificar dependências principais
echo "📦 Verificando dependências..."
python3 -c "import speech_recognition, gtts, google.generativeai, pandas; print('✅ Dependências OK')"

# Verificar dados
echo "📊 Verificando dados..."
if [ -f "data/projects_data.csv" ]; then
    lines=$(wc -l < data/projects_data.csv)
    echo "✅ Dados carregados: $lines linhas"
else
    echo "❌ Arquivo de dados não encontrado"
    exit 1
fi

# Verificar assets
echo "🖼️  Verificando imagens..."
if [ -f "assets/Terreo (2).jpg" ] && [ -f "assets/superior.jpg" ]; then
    echo "✅ Imagens encontradas"
else
    echo "❌ Imagens não encontradas"
    exit 1
fi

echo ""
echo "✅ TESTE CONCLUÍDO COM SUCESSO!"
echo "🚀 Sistema pronto para uso!"
echo ""
echo "Para executar: ./scripts/start_agent.sh"
