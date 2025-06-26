# AI Agent - Science Fair Navigation System

A conversational AI agent designed to help visitors navigate the Senac Convention Center during science fairs. The system combines structured data search with AI-powered natural language processing to provide accurate project information and detailed directions.

## Features

- **Project Search**: Find specific projects by name, course, class, or location
- **Intelligent Directions**: AI-generated step-by-step navigation using floor maps
- **Voice & Text Interface**: Support for both microphone input and text input
- **Natural Audio Output**: Text-to-speech with emoji filtering and natural language conversion
- **Bilingual Support**: Portuguese language processing and speech synthesis

## Requirements

- Python 3.8+
- Google Gemini API key
- Microphone (optional, for voice input)
- Audio output device

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure your Google Gemini API key in `src/main.py`
4. Run the system:
   ```bash
   scripts/start_agent.bat
   ```

## Project Structure

```
├── src/
│   ├── main.py           # Main application
│   └── project_search.py # Project data search module
├── data/
│   └── projects_data.csv # Projects database
├── assets/
│   ├── Terreo (2).jpg   # Ground floor map
│   └── superior.jpg     # Upper floor map
├── scripts/
│   └── start_agent.bat  # Windows startup script
├── docs/
├── requirements.txt
└── README.md
```

## Usage

The system provides two interaction modes:
- **Voice Mode**: Speak your questions using the microphone
- **Text Mode**: Type your questions using the keyboard

Example queries:
- "Where is the Silicon Echoes project?"
- "IoT course projects"
- "Class 3 projects"
- "Where is the bathroom?"

## Technical Details

- **Data Processing**: Pandas for CSV data manipulation
- **AI Integration**: Google Gemini for natural language processing and computer vision
- **Speech Processing**: SpeechRecognition for voice input, gTTS for speech synthesis
- **Audio Handling**: Pydub and playsound for audio processing

## License

This project is developed for educational purposes at Senac.
