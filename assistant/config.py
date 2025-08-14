import json
import os


CONFIG_PATH = "config.json"

DEFAULT_CONFIG = {
    "voices": {
        "morra": {
            "model": "resources/voices/morra_model.pth",
            "wake_word": "Хермеус"
        },
        "default": {
            "model": "resources/voices/default_model.pth",
            "wake_word": "Ассистент"
        }
    },
    "current_voice": "default",
    "language": "ru-RU",
    "tts_engine": "coqui",
    "stt_engine": "speech_recognotition"
}

def load_config():
    """Загружает конфиг, если его нет - создаёт новый"""
    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)

    with open(CONFIG_PATH, "R", encoding="utf-8") as f:
        return json.load(f)


def save_config(config):
    """Сохраняет конфиг."""
    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=1)


def set_current_voice(voice_name) -> bool:
    """Меняет текущий голос."""
    config = load_config()

    if voice_name in config["voices"]:
        config["current_voice"] = voice_name
        save_config(config)
        return True
    return False


def set_wake_word(voice_name, new_wake_word) -> bool:
    """Меняет wake word для указанного голоса."""
    config = load_config()

    if voice_name in config["voices"]:
        config["voices"][voice_name]["wake_word"] = new_wake_word
        save_config(config)
        return True
    return False
