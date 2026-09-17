# Installeer eerst gtts via je command prompt / terminal: pip install gtts
import os
from gtts import gTTS

print("Start met het genereren van 36 audiobestanden...")
for i in range(1, 37):
    num_str = f"{i:02d}"
    text = f"Opname {num_str}"
    
    # Genereer Nederlandse spraak
    tts = gTTS(text=text, lang='nl')
    
    filename = f"opname_{num_str}.mp3"
    tts.save(filename)
    print(f"Aangemaakt: {filename}")

print("Klaar! Alle 36 bestanden staan in deze map.")
