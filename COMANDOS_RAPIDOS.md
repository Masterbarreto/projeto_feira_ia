# 🚀 COMANDOS RÁPIDOS - AGENTE IA FEIRA

## ⚡ Windows (HOJE)

```bash
# 1. Instalar
install.bat

# 2. Configurar API
# Edite src/main.py e coloque sua chave Google Gemini

# 3. Executar
scripts\start_agent.bat

# 4. Diagnóstico (se problemas)
python scripts\diagnosticar_audio.py
```

---

## 🥧 Raspberry Pi 4 (AMANHÃ)

```bash
# 1. Preparar sistema
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3 python3-pip python3-venv git
sudo apt install -y python3-pyaudio portaudio19-dev python3-dev gcc
sudo apt install -y mpg123 alsa-utils pulseaudio

# 2. Dar permissões
chmod +x install.sh scripts/*.sh

# 3. Instalar
./install.sh

# 4. Configurar API
nano src/main.py
# Substitua pela sua chave Google Gemini
# Salvar: Ctrl+O, Enter | Sair: Ctrl+X

# 5. Executar
./scripts/start_agent.sh

# 6. Diagnóstico (se problemas)
python3 scripts/diagnosticar_audio.py
```

---

## 🔑 Obter Chave API Google Gemini

1. Acesse: https://makersuite.google.com/app/apikey
2. Clique "Create API Key"
3. Copie a chave
4. Cole em `src/main.py` na linha:
   `genai.configure(api_key="SUA_CHAVE_AQUI")`

---

## 🛠️ Problemas Comuns

### PyAudio não instala
**Windows:** `pip install pipwin && pipwin install pyaudio`
**Raspberry Pi:** `sudo apt install python3-pyaudio`

### Microfone não funciona
**Windows:** Execute `python scripts\diagnosticar_audio.py`
**Raspberry Pi:** Execute `arecord -l` para ver microfones

### Áudio não reproduz
**Raspberry Pi:** Execute `sudo raspi-config` → Advanced → Audio → Force 3.5mm

---

## ✅ Sistema Pronto!

- **58 projetos** carregados
- **Reconhecimento de voz** funcionando  
- **IA generativa** configurada
- **Compatível** Windows + Raspberry Pi
