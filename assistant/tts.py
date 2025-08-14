import os
import tempfile
import sounddevice as sd
import soundfile as sf
from TTS.api import TTS
from assistant.config import load_config


class Speaker:
    def __init__(self, config=None):
        if config is None:
            config = load_config()
        
        self.config = config

        # Загружаем текущий голос
        voice_name = self.config["current_voice"]
        model_path = self.config["voices"][voice_name]["model"]

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Модель TTS не найдена: {model_path}")

        # Загружаем модель Coqui
        print(f"[TTS] Загружаю модель: {model_path}")
        self.tts = TTS(model_path)

    
    def set_voice(self, voice_name):
        """Меняет модель TTS"""
        if voice_name not in self.config["voices"]:
            raise ValueError(f"Голос '{voice_name}' не найден в конфиге.")
        
        model_path = self.config["voices"][voice_name]["model"]

        if not os.path.exists(model_path):
            raise FileNotFoundError(f"Модель TTS не найдена: {model_path}")
        
        self.tts = TTS(model_path)
        self.config["current_voice"] = voice_name

    
    def speak(self, text):
        """Говорит заданным голосом."""
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            tmp_path = tmp_file.name

        self.tts.tts_to_file(text=text, file_path=tmp_path)

        # Воспроизведение
        data, samplerate = sf.read(tmp_path)
        sd.play(data, samplerate)
        sd.wait()

        os.remove(tmp_path)

    
    def list_voices(self):
        """Список голосов (имена из конфига)"""
        return list(self.config["voices"].keys())
