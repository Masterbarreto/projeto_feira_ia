# 🤖 Agente IA - Centro de Convenções Senac

## 📋 Descrição

Agente inteligente para ajudar visitantes na feira de projetos do Centro de Convenções Senac. Usa IA generativa com dados em CSV para responder perguntas sobre localização de projetos e navegação no local.

## ✨ Funcionalidades

- 🔍 Busca inteligente por nome ou palavra-chave  
- 🎤 Reconhecimento de voz (se disponível)  
- 🔊 Respostas com síntese de voz (TTS)  
- 🗺️ Direções detalhadas  
- 🤖 Fallback com IA para perguntas genéricas

---

## 🚀 Instalação e Uso

### 💻 Windows 10/11

#### Passo 1: Preparar o Sistema
```bash
python --version  # Verifique o Python
cd projeto_feira_ia  # Baixe ou clone o repositório
```

#### Passo 2: Instalação Automática
```bash
install.bat
```

#### Passo 3: Configurar API
```python
# Abra src/main.py
genai.configure(api_key="SUA_CHAVE_AQUI")  # Substitua pela sua chave da API
```

#### Passo 4: Executar
```bash
scripts\start_agent.bat  # Script automático
python src\main.py       # Ou manual
```

#### Passo 5: Diagnóstico
```bash
python scripts\diagnosticar_audio.py
```

---

### 🥧 Raspberry Pi 4

#### Passo 1: Preparar o Sistema
```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv git
cd projeto_feira_ia
```

#### Passo 2: Dependências de áudio
```bash
sudo apt install -y python3-pyaudio portaudio19-dev python3-dev gcc
sudo apt install -y mpg123 alsa-utils pulseaudio
```

#### Passo 3: Instalação
```bash
chmod +x install.sh scripts/start_agent.sh
./install.sh
```

#### Passo 4: Configurar API
```bash
nano src/main.py
# Altere a chave da API
# Salvar: Ctrl+O | Sair: Ctrl+X
```

#### Passo 5: Executar
```bash
./scripts/start_agent.sh  # Script automático
source .venv/bin/activate && python3 src/main.py  # Manual
```

#### Passo 6: Diagnóstico
```bash
python3 scripts/diagnosticar_audio.py
```

---

### 🎤 Áudio no Raspberry Pi

```bash
aplay -l         # Verifica saída de áudio
arecord -l       # Verifica microfones
sudo raspi-config  # Vá em Advanced Options > Audio
aplay /usr/share/sounds/alsa/Front_Left.wav
```

---

## 📁 Estrutura do Projeto

```
projeto_feira_ia/
├── src/
│   ├── main.py
│   └── project_search.py
├── data/
│   └── projects_data.csv
├── assets/
│   ├── Terreo (2).jpg
│   └── superior.jpg
├── scripts/
│   ├── start_agent.bat
│   ├── start_agent.sh
│   └── diagnosticar_audio.py
├── docs/
│   └── INSTALACAO_RASPBERRY_PI.md
├── install.bat
├── install.sh
└── requirements.txt
```

---

## 🎯 Exemplos de Perguntas

**Projetos:**
- "Onde fica o projeto Ecos do Silício?"
- "Projeto sobre inteligência artificial"

**Curso:**
- "Projetos do curso IOT"
- "Curso de Administração"

**Turma:**
- "Projetos da turma 3"
- "Turma 2 ADM"

**Navegação:**
- "Onde fica o banheiro?"
- "Como chegar ao segundo andar?"

---

## 🧠 Interação

1. 🎤 Voz (se microfone disponível)  
2. ⌨️ Texto (pelo terminal)

---

## 💡 Tecnologias

- **IA Generativa:** Google Gemini 1.5 Flash  
- **TTS:** Google Text-to-Speech  
- **Reconhecimento de voz:** Google Speech Recognition  
- **Processamento:** Python 3.x, Pandas

---

## 🛠️ Resolução de Problemas

### ❌ PyAudio não instala

**Windows:**
```bash
pip install pipwin
pipwin install pyaudio
```

**Raspberry Pi:**
```bash
sudo apt install python3-pyaudio portaudio19-dev
```

---

### ❌ Microfone não detectado

**Windows:**
- Verifique o cabo
- Execute `python scripts\diagnosticar_audio.py`

**Raspberry Pi:**
```bash
arecord -l
arecord -D plughw:X,Y -f cd test.wav
```

---

### ❌ Áudio não reproduz

**Windows:**
- Verifique se os alto-falantes funcionam  
- O sistema usa o dispositivo padrão do Windows

**Raspberry Pi:**
```bash
sudo apt install mpg123
mpg123 --test
```

---

### ❌ Erro de API do Gemini

- Confirme a chave no `src/main.py`
- Verifique no [Google AI Studio](https://makersuite.google.com/app/apikey)
- Veja se a internet está funcionando

---

### ❌ Dados não carregam

- O arquivo `data/projects_data.csv` existe?  
- Está na pasta certa?  
- Rode o diagnóstico:

```bash
# Windows
python scripts\diagnosticar_audio.py

# Raspberry Pi
python3 scripts/diagnosticar_audio.py
```

---

## ⚡ Guia Rápido

### 🏃‍♂️ Windows
```bash
install.bat
# edite src/main.py com sua chave
scripts\start_agent.bat
```

### 🏃‍♂️ Raspberry Pi
```bash
chmod +x install.sh scripts/*.sh
./install.sh
nano src/main.py
./scripts/start_agent.sh
```

---

## 🔑 Obter chave da API Gemini

1. Vá em: https://makersuite.google.com/app/apikey  
2. Clique em **Create API Key**  
3. Copie e cole em `src/main.py`

---

## 📞 Suporte

Encontrou problemas?

1. Rode o diagnóstico  
2. Confira esta documentação  
3. Veja se a API está configurada corretamente  

✅ Sistema testado no Windows 11 e pronto para rodar no Raspberry Pi 4.
