# Audio_translate# 🎙️ Audio Transcribe & Translate (English → Hindi)

This project takes an **English audio file**, transcribes it into text using **OpenAI Whisper**, translates the text into **Hindi** with a Hugging Face model, and finally converts the translated text into **Hindi speech** using **gTTS**.

---

## 📂 Features
- **Speech-to-Text**: Transcribes English audio into text with Whisper.
- **Text Translation**: Translates English text into Hindi using `Helsinki-NLP/opus-mt-en-hi`.
- **Text-to-Speech**: Converts Hindi translation into an `.mp3` audio file.
- **Automated Workflow**: One script handles all steps from audio → text → translation → audio.

---

## 🛠️ Tech Stack
- **Python 3.8+**
- [OpenAI Whisper](https://github.com/openai/whisper) — Automatic Speech Recognition (ASR)
- [Hugging Face Transformers](https://huggingface.co/transformers/) — Translation models
- [gTTS (Google Text-to-Speech)](https://pypi.org/project/gTTS/) — Speech synthesis
- **Pathlib & OS** — File handling

---

## 📦 Installation

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/vishwajitsen/Audio_translate
cd Audio_translate
