# -*- coding: utf-8 -*-
import sys
import platform

def verificar_dependencias():
    """Verifica se as dependências estão instaladas."""
    print("🔍 Verificando dependências...")
    
    modulos = {
        'speech_recognition': 'SpeechRecognition',
        'gtts': 'gTTS',
        'google.generativeai': 'google-generativeai',
        'pandas': 'pandas',
        'pydub': 'pydub'
    }
    
    modulos_faltando = []
    
    for modulo, nome_pip in modulos.items():
        try:
            __import__(modulo)
            print(f"✅ {nome_pip}")
        except ImportError:
            print(f"❌ {nome_pip} - NÃO INSTALADO")
            modulos_faltando.append(nome_pip)
    
    # Verificar PyAudio separadamente
    try:
        import pyaudio
        print("✅ PyAudio")
    except ImportError:
        print("❌ PyAudio - NÃO INSTALADO")
        sistema = platform.system().lower()
        if 'linux' in sistema:
            print("   💡 Para instalar: sudo apt install python3-pyaudio")
        elif 'windows' in sistema:
            print("   💡 Para instalar: pip install pyaudio")
    
    return len(modulos_faltando) == 0

def diagnosticar_audio():
    print("🔍 DIAGNÓSTICO DE ÁUDIO - AGENTE IA")
    print("=" * 50)
    print(f"🖥️  Sistema: {platform.system()} {platform.release()}")
    print(f"🐍 Python: {sys.version.split()[0]}")
    
    # Verificar dependências
    print("\n1. Dependências:")
    deps_ok = verificar_dependencias()
    
    if not deps_ok:
        print("\n❌ Execute primeiro: install.bat (Windows) ou ./install.sh (Linux)")
        return False
    
    # Teste básico de áudio
    print("\n2. Testando módulos de áudio...")
    try:
        import speech_recognition as sr
        print("✅ SpeechRecognition OK")
        
        from gtts import gTTS
        print("✅ gTTS OK")
        
        try:
            import pyaudio
            p = pyaudio.PyAudio()
            device_count = p.get_device_count()
            print(f"✅ PyAudio OK - {device_count} dispositivos")
            p.terminate()
        except:
            print("⚠️  PyAudio com problemas - use modo texto")
            
    except Exception as e:
        print(f"❌ Erro nos módulos: {e}")
        return False
    
    print("\n" + "=" * 50)
    print("✅ SISTEMA PRONTO PARA USO!")
    print("\n🚀 Para executar:")
    if platform.system() == 'Windows':
        print("   scripts\\start_agent.bat")
    else:
        print("   ./scripts/start_agent.sh")
    return True

if __name__ == "__main__":
    diagnosticar_audio()
