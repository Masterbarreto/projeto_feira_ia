# -*- coding: utf-8 -*-
import os
import base64
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
import google.generativeai as genai
from project_search import carregar_dados_projetos, buscar_projeto

# ✅ CONFIGURE SUA CHAVE DA API DO GEMINI
genai.configure(api_key="AIzaSyBeJhhq9V6MGg-q9gZyINavKvvowCVzjsE")

# 📂 Caminho para as imagens locais (relativo ao diretório do script)
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
IMG_TERREO_PATH = os.path.join(script_dir, "..", "assets", "Terreo (2).jpg")
IMG_SUPERIOR_PATH = os.path.join(script_dir, "..", "assets", "superior.jpg")

# 🔄 Função para converter imagem para base64
def carregar_imagem_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# 🎤 Função para verificar se há microfone disponível
def verificar_microfone():
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            return True
    except OSError:
        return False

# 🎙️ Função para ouvir pergunta pelo microfone
def ouvir_microfone():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("🎧 Ouvindo sua pergunta (você tem 30s para começar)...")
            r.adjust_for_ambient_noise(source, duration=1)
            audio = r.listen(source, timeout=30, phrase_time_limit=15)
        
        texto = r.recognize_google(audio, language="pt-BR")
        print(f"🎤 Você disse: {texto}")
        return texto
    except sr.WaitTimeoutError:
        print("⏱️ Tempo esgotado! Você não começou a falar a tempo.")
        return None
    except sr.UnknownValueError:
        print("❌ Não entendi. Tente novamente.")
        return None
    except sr.RequestError as e:
        print(f"❌ Erro no reconhecimento de voz: {e}")
        return None
    except OSError as e:
        print(f"❌ Erro de microfone: {e}")
        return None
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")
        return None

# ⌨️ Função para entrada de texto
def ouvir_texto():
    try:
        pergunta = input("💬 Digite sua pergunta: ").strip()
        if pergunta:
            print(f"✏️ Você digitou: {pergunta}")
            return pergunta
        return None
    except KeyboardInterrupt:
        print("\n👋 Encerrando o agente...")
        return "SAIR"

# 🔊 Função para falar a resposta com gTTS (CORRIGIDA)
def falar_texto(texto):
    """
    Função TTS que aguarda o término da reprodução antes de liberar a interface.
    Converte informações estruturadas em texto natural para melhor áudio.
    """
    try:
        import tempfile
        import re
        
        # Converte texto estruturado em texto natural para áudio
        texto_para_audio = converter_para_texto_natural(texto)
        
        # Remove emojis e símbolos especiais do texto para TTS
        texto_limpo = re.sub(r'[^\w\s\.,\!\?\-\:\;\(\)]', ' ', texto_para_audio)
        # Remove múltiplos espaços
        texto_limpo = re.sub(r'\s+', ' ', texto_limpo).strip()
        
        # Se o texto ficar muito pequeno após limpeza, não tenta falar
        if len(texto_limpo) < 10:
            return
        
        # Cria um arquivo temporário
        with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
            temp_path = temp_file.name
            
            # Gera o áudio com texto limpo e configurações otimizadas
            tts = gTTS(text=texto_limpo, lang="pt", slow=False)
            tts.save(temp_path)
        
        # Reproduz o áudio e AGUARDA o término
        try:
            from playsound import playsound
            playsound(temp_path)
        except Exception:
            # Se playsound falhar, usa método alternativo
            if os.name == "nt":  # Windows
                import subprocess
                subprocess.run(['start', '/wait', temp_path], shell=True)
            else:  # Linux/Mac/Raspberry
                import subprocess
                subprocess.run(['mpg123', temp_path])
        
        # Remove o arquivo temporário
        try:
            import os
            os.unlink(temp_path)
        except:
            pass  # Se não conseguir deletar, não é crítico
            
    except Exception as e:
        print(f"❌ Erro ao gerar/reproduzir áudio: {e}")

# 🎵 Função para converter informações estruturadas em texto natural
def converter_para_texto_natural(texto):
    """
    Converte as informações estruturadas do projeto em texto corrido para áudio.
    """
    import re
    
    # Se não contém informações de projeto estruturadas, retorna o texto original
    if not ("📌 Projeto:" in texto and "📍 Local:" in texto):
        return texto
    
    # Extrai as informações do projeto
    linhas = texto.split('\n')
    projeto = ""
    local = ""
    tipo = ""
    curso = ""
    turma = ""
    direcoes = ""
    
    capturando_direcoes = False
    
    for linha in linhas:
        if linha.startswith("📌 Projeto:"):
            projeto = linha.replace("📌 Projeto:", "").strip()
        elif linha.startswith("📍 Local:"):
            local = linha.replace("📍 Local:", "").strip()
        elif linha.startswith("🎯 Tipo:"):
            tipo = linha.replace("🎯 Tipo:", "").strip()
        elif linha.startswith("📚 Curso:"):
            curso = linha.replace("📚 Curso:", "").strip()
        elif linha.startswith("👥 Turma:"):
            turma = linha.replace("👥 Turma:", "").strip()
        elif linha.startswith("🗺️ COMO CHEGAR:"):
            capturando_direcoes = True
            continue
        elif capturando_direcoes and linha.strip():
            direcoes += linha.strip() + " "
    
    # Constrói o texto natural para áudio
    texto_natural = ""
    
    if projeto:
        texto_natural += f"Encontrei o projeto {projeto}. "
    
    if local:
        texto_natural += f"Ele está localizado na {local}. "
    
    if tipo:
        texto_natural += f"É um projeto de {tipo.lower()}. "
    
    if curso and turma:
        texto_natural += f"É do curso {curso}, turma {turma}. "
    elif curso:
        texto_natural += f"É do curso {curso}. "
    
    if direcoes:
        texto_natural += f"Para chegar lá: {direcoes.strip()}"
    
    return texto_natural

# 🧠 Função que processa a pergunta usando CSV primeiro, depois Gemini
def processar_pergunta(pergunta, dados_projetos=None):
    try:
        # Primeiro tenta buscar nos dados dos projetos da feira
        if dados_projetos is not None:
            print("🔍 Buscando nos projetos da feira...")
            resultado_projetos = buscar_projeto(pergunta, dados_projetos)
            
            if resultado_projetos:
                print("✅ Encontrado nos dados da feira!")
                
                # Extrai o local do resultado dos projetos
                linhas = resultado_projetos.split('\n')
                local = None
                for linha in linhas:
                    if linha.startswith("📍 Local:"):
                        local = linha.replace("📍 Local:", "").strip()
                        break
                
                if local:
                    print("🗺️ Gerando direções para o local...")
                    # Usa o Gemini para dar direções específicas para o local encontrado
                    img_terreo = carregar_imagem_base64(IMG_TERREO_PATH)
                    img_superior = carregar_imagem_base64(IMG_SUPERIOR_PATH)

                    vision_model = genai.GenerativeModel("gemini-1.5-flash")

                    direcoes = vision_model.generate_content(
                        contents=[
                            {"role": "user", "parts": [
                                "Você é um Agente de IA de localização interna dentro de um centro de convenções do Senac. Seu nome é 'Senalexa'.",
                                "As imagens enviadas representam os dois andares do prédio. O arquivo 'Terreo.jpg' é o andar térreo (parte de baixo) e 'superior.jpg' é o andar superior (parte de cima).",
                                "Neste prédio, existem DUAS escadas principais que conectam os andares:",
                                "- A primeira escada fica próxima ao espaço chamado 'Cavalo'.",
                                "- A segunda escada fica próxima ao 'Auditório'.",
                                "Use essas escadas como referências para orientar o usuário quando for necessário subir de andar.",
                                "Observe a posição das salas, corredores e áreas demarcadas para guiar o usuário.",
                                "Se o espaço procurado estiver no andar superior, oriente o usuário a 'ir até a escada mais próxima', 'subir' e depois explique o caminho passo a passo após subir.",
                                "Se estiver no andar térreo, explique o caminho apenas com direções horizontais.",
                                "Fale de forma informal e clara, como um guia humano faria. Exemplo: 'Siga até a escada perto do Auditório, suba, vire à esquerda, a segunda sala é a Multiuso 3'.",
                                "Sempre use pontos de referência como escadas, corredores e outras salas próximas para facilitar a localização.",
                                "Agora, dê direções claras e passo a passo para chegar ao seguinte local:",
                                {"inline_data": {"mime_type": "image/jpeg", "data": img_terreo}},
                                {"inline_data": {"mime_type": "image/jpeg", "data": img_superior}},
                                f"Local de destino: {local}"
                            ]}
                        ]
                    )
                    
                    # Combina as informações do projeto com as direções
                    resposta_completa = resultado_projetos + "\n\n🗺️ COMO CHEGAR:\n" + direcoes.text
                    return resposta_completa
                
                return resultado_projetos
        
        # Se não encontrar nos projetos, usa o Gemini para localização geral
        print("🤖 Consultando IA para localização...")
        img_terreo = carregar_imagem_base64(IMG_TERREO_PATH)
        img_superior = carregar_imagem_base64(IMG_SUPERIOR_PATH)

        vision_model = genai.GenerativeModel("gemini-1.5-flash")

        resposta = vision_model.generate_content(
            contents=[
                {"role": "user", "parts": [
                    "Você é um Agente de IA de localização interna dentro de um centro de convenções do Senac. Seu nome é 'Agente de IA'.",
                    "As imagens enviadas representam os dois andares do prédio. O arquivo 'Terreo.jpg' é o andar térreo (parte de baixo) e 'superior.jpg' é o andar superior (parte de cima).",
                    "Neste prédio, existem DUAS escadas principais que conectam os andares:",
                    "- A primeira escada fica próxima ao espaço chamado 'Cavalo'.",
                    "- A segunda escada fica próxima ao 'Auditório'.",
                    "Use essas escadas como referências para orientar o usuário quando for necessário subir de andar.",
                    "Observe a posição das salas, corredores e áreas demarcadas para guiar o usuário.",
                    "Se o espaço procurado estiver no andar superior, oriente o usuário a 'ir até a escada mais próxima', 'subir' e depois explique o caminho passo a passo após subir.",
                    "Se estiver no andar térreo, explique o caminho apenas com direções horizontais.",
                    "Fale de forma informal e clara, como um guia humano faria. Exemplo: 'Siga até a escada perto do Auditório, suba, vire à esquerda, a segunda sala é a Multiuso 3'.",
                    "Sempre use pontos de referência como escadas, corredores e outras salas próximas para facilitar a localização.",
                    "Agora, responda à seguinte pergunta de forma clara e passo a passo:",
                    {"inline_data": {"mime_type": "image/jpeg", "data": img_terreo}},
                    {"inline_data": {"mime_type": "image/jpeg", "data": img_superior}},
                    f"Pergunta: {pergunta}"
                ]}
            ]
        )
        return resposta.text
    except Exception as e:
        return f"❌ Erro ao processar pergunta: {e}"

# 🚀 Loop principal
if __name__ == "__main__":
    print("🤖 Agente de IA do Centro de Convenções Senac")
    print("=" * 50)
    
    # Carrega os dados dos projetos da feira
    print("📂 Carregando dados dos projetos da feira...")
    dados_projetos = carregar_dados_projetos()
    if dados_projetos is not None:
        print(f"✅ {len(dados_projetos)} projetos carregados!")
    else:
        print("⚠️ Dados dos projetos não disponíveis - usando apenas localização geral")
    
    # Verifica se há microfone disponível
    microfone_disponivel = verificar_microfone()
    
    if microfone_disponivel:
        print("🎤 Microfone detectado! Você pode usar voz ou texto.")
        print("📝 Escolha o modo:")
        print("  1 - Entrada por voz (microfone)")
        print("  2 - Entrada por texto (teclado)")
        
        try:
            modo = input("Digite 1 ou 2: ").strip()
        except KeyboardInterrupt:
            print("\n👋 Encerrando...")
            exit()
            
        usar_voz = modo == "1"
    else:
        print("🎤 Nenhum microfone detectado.")
        print("📝 Usando modo texto (teclado).")
        usar_voz = False
    
    print("\n" + "=" * 50)
    print("🤖 Agente pronto para perguntas!")
    print("💡 Exemplos: 'Onde fica a Multiuso 4?', 'Como chego ao laboratório?'")
    print("⚠️  Digite 'sair' para encerrar")
    print("=" * 50)

    while True:
        try:
            if usar_voz:
                pergunta = ouvir_microfone()
                if pergunta is None:
                    print("🔄 Tentando novamente... (ou digite 'texto' para mudar para modo texto)")
                    continue
            else:
                pergunta = ouvir_texto()
            
            if pergunta is None:
                continue
            
            if pergunta.lower() in ['sair', 'exit', 'quit', 'SAIR']:
                print("👋 Encerrando o agente...")
                break
            
            if pergunta.lower() == 'texto':
                usar_voz = False
                print("📝 Mudando para modo texto...")
                continue
            
            if pergunta.lower() == 'voz' and microfone_disponivel:
                usar_voz = True
                print("🎤 Mudando para modo voz...")
                continue
            
            print("\n🤖 Processando sua pergunta...")
            resposta = processar_pergunta(pergunta, dados_projetos)
            
            print("\n" + "="*50)
            print("🤖 RESPOSTA:")
            print(resposta)
            print("="*50)
              # Reproduz o áudio completo antes de liberar para próxima pergunta
            if not resposta.startswith("❌"):
                print("🔊 Reproduzindo resposta em áudio...")
                falar_texto(resposta)
                print("✅ Áudio concluído!")
            
            print("\n🔄 Pronto para a próxima pergunta...\n")
            
        except KeyboardInterrupt:
            print("\n👋 Encerrando o agente...")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")
            print("🔄 Tentando continuar...")
