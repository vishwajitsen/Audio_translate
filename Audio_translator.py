import os
from pathlib import Path
import whisper
from gtts import gTTS
from transformers import pipeline

# ---------------------------
# CONFIG
# ---------------------------
# Path to your audio file
audio_path = r"C:\Users\win11\OneDrive\Documents\MiSpy Documents\Audio_translate\mary-had-a-little-lamb_short-236651.mp3"

# Output file names
english_text_file = "transcription_english.txt"
hindi_text_file = "translation_hindi.txt"
hindi_audio_file = "translation_hindi.mp3"

# ---------------------------
# STEP 1: Transcribe English audio
# ---------------------------
print("[INFO] Loading Whisper model...")
model = whisper.load_model("small")  # choose: tiny, base, small, medium, large
print("[INFO] Transcribing audio...")
result = model.transcribe(audio_path, language="en")
english_text = result["text"].strip()

# Save English transcription
with open(english_text_file, "w", encoding="utf-8") as f:
    f.write(english_text)
print(f"[INFO] English transcription saved to {english_text_file}")

# ---------------------------
# STEP 2: Translate English to Hindi
# ---------------------------
print("[INFO] Loading translation pipeline...")
translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-hi")
translation = translator(english_text, max_length=512)
hindi_text = translation[0]['translation_text'].strip()

# Save Hindi translation
with open(hindi_text_file, "w", encoding="utf-8") as f:
    f.write(hindi_text)
print(f"[INFO] Hindi translation saved to {hindi_text_file}")

# ---------------------------
# STEP 3: Convert Hindi text to speech
# ---------------------------
print("[INFO] Converting Hindi text to speech...")
tts = gTTS(hindi_text, lang='hi')
tts.save(hindi_audio_file)
print(f"[INFO] Hindi speech saved to {hindi_audio_file}")

print("[✓] All done!")
