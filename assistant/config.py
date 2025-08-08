import json
import os


DEFAULT_CONFIG = {
    "voice": 0,
    "language": "ru-RU",
    "wake_word": "Хермеус",
    "tts_engine": "pyttsx3",
    "stt_engine": "speech_recogition"
}

CONFIG_PATH = "config.json"

def load_config():

    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
    
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)
    
def save_config(config):
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=4)
