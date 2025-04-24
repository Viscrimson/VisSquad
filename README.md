# VisSquad# VisSquad

A unified **STT/TTS + AI NPC squad** framework for VRChat.  
Talk as a player or let your four “sisters” Lyra, Xyla, Ayda and Tyfa respond in real time—with Whisper transcription, Edge/AWS/ElevenLabs TTS, GPT-powered dialogue, and OSC routing.

---

## Features

- **Player Speech**: live mic/keyboard → Whisper STT, spell-check, segmented chat  
- **Multi-Persona TTS**: EdgeTTS (default), Polly or ElevenLabs per character  
- **AI NPC Squad**: GPT-driven responses, context logging, role splitting  
- **OSC Integration**: per-character & “All” chat to VRChat instances  
- **Modular Design**: `player/`, `ai/`, `tts/`, `osc/`, `locomotion/`  

---

## Quick Start

```bash
git clone https://github.com/Viscrimson/VisSquad.git
cd VisSquad
python3.11 -m venv .venv
# macOS/Linux:
source .venv/bin/activate
# Windows PowerShell:
.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python src/main.py
