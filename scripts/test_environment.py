# -*- coding: utf-8 -*-
import os
import sys

def test_imports():
    """Test all required imports"""
    print("Testing imports...")
    
    try:
        import speech_recognition as sr
        print("✅ speech_recognition imported successfully")
    except ImportError as e:
        print(f"❌ speech_recognition import failed: {e}")
        return False
    
    try:
        from gtts import gTTS
        print("✅ gtts imported successfully")
    except ImportError as e:
        print(f"❌ gtts import failed: {e}")
        return False
    
    try:
        from pydub import AudioSegment
        print("✅ pydub imported successfully")
    except ImportError as e:
        print(f"❌ pydub import failed: {e}")
        return False
    
    try:
        import google.generativeai as genai
        print("✅ google.generativeai imported successfully")
    except ImportError as e:
        print(f"❌ google.generativeai import failed: {e}")
        return False
    
    try:
        import pyaudio
        print("✅ pyaudio imported successfully")
    except ImportError as e:
        print(f"❌ pyaudio import failed: {e}")
        return False
    
    return True

def test_files():
    """Test if required files exist"""
    print("\nTesting files...")
    
    files_to_check = [
        "imagens/Terreo (2).jpg",
        "imagens/superior.jpg"
    ]
    
    for file_path in files_to_check:
        if os.path.exists(file_path):
            print(f"✅ {file_path} exists")
        else:
            print(f"❌ {file_path} not found")
            return False
    
    return True

def main():
    print("🧪 Testing AI Agent Environment\n")
    
    imports_ok = test_imports()
    files_ok = test_files()
    
    if imports_ok and files_ok:
        print("\n🎉 All tests passed! Your AI agent environment is ready.")
        print("\n⚠️  Note: You still need to:")
        print("1. Set your Google Gemini API key in agente_ia_feira.py")
        print("2. Replace 'SUA_CHAVE_API_AQUI' with your actual API key")
    else:
        print("\n❌ Some tests failed. Please check the errors above.")

if __name__ == "__main__":
    main()
