# 🚀 Guia de Instalação - Raspberry Pi 4

## 📋 Pré-requisitos
- Raspberry Pi 4 com Raspberry Pi OS
- Python 3.8+ instalado
- Conexão com internet
- Microfone USB ou hat de áudio

## 🔧 Instalação Passo a Passo

### 1. Preparar o Sistema
```bash
# Atualizar o sistema
sudo apt update && sudo apt upgrade -y

# Instalar dependências do sistema
sudo apt install -y python3-pip python3-venv git
```

### 2. Instalar Dependências de Áudio
```bash
# Instalar PyAudio e bibliotecas de áudio
sudo apt install -y python3-pyaudio portaudio19-dev python3-dev gcc

# Instalar reprodutores de áudio
sudo apt install -y mpg123 alsa-utils pulseaudio

# Testar áudio (opcional)
aplay /usr/share/sounds/alsa/Front_Left.wav
```

### 3. Configurar o Projeto
```bash
# Navegar para a pasta do projeto
cd projeto_feira_ia

# Tornar scripts executáveis
chmod +x install.sh scripts/start_agent.sh

# Executar instalação
./install.sh
```

### 4. Configurar API
```bash
# Editar o arquivo principal
nano src/main.py

# Substitua a linha:
# genai.configure(api_key="AIzaSyBeJhhq9V6MGg-q9gZyINavKvvowCVzjsE")
# Por:
# genai.configure(api_key="SUA_CHAVE_AQUI")
```

### 5. Executar o Sistema
```bash
# Executar diretamente
./scripts/start_agent.sh

# OU executar manualmente
source .venv/bin/activate
python3 src/main.py
```

## 🛠️ Resolução de Problemas

### Problema: PyAudio não instala
```bash
sudo apt install python3-pyaudio portaudio19-dev
```

### Problema: Áudio não funciona
```bash
# Verificar dispositivos
aplay -l
amixer

# Configurar dispositivo padrão
sudo raspi-config
# Advanced Options > Audio > Force 3.5mm jack
```

### Problema: Microfone não detectado
```bash
# Verificar microfones
arecord -l

# Testar gravação
arecord -D plughw:1,0 -f cd test.wav
```

### Problema: Dependências não instalam
```bash
# Usar o arquivo específico do Raspberry Pi
pip install -r requirements-rpi.txt

# Instalar PyAudio manualmente
sudo apt install python3-pyaudio
```

## ✅ Verificação Final
```bash
# Executar diagnóstico
python3 scripts/diagnosticar_audio.py

# Se tudo estiver OK, você verá:
# ✅ SISTEMA PRONTO PARA USO!
```

## 🎯 Pronto!
Agora o sistema está pronto para rodar no seu Raspberry Pi 4. Execute `./scripts/start_agent.sh` para começar!
