from assistant.tts import Speaker
from assistant.config import load_config, save_config


class VoiceManager:
    def __init__(self):
        self.config = load_config()
        self.speaker = Speaker(self.config)

    
    def list_voices(self):
        """Возвращает список доступных голосов."""
        return list(self.config["voices"].keys())
    

    def set_voice(self, voice_name):
        """Меняет голос и wake word."""
        if voice_name not in self.config["voices"]:
            return f"Голос '{voice_name}' не найден."
        
        self.config["current_voice"] = voice_name
        save_config(self.config)

        # Перезагружаем спикера с новым конфигом
        self.speaker = Speaker(self.config)

        # Получаем wake word
        wake_word = self.config["voices"][voice_name]["wake_word"]

        # Озвучивание
        self.speaker.speak(f"Голос изменён на {voice_name}. Ключевое слово — {wake_word}.")

        return f"Голос переключён на {voice_name}, wake word: {wake_word}"
    

    def preview_voice(self, voice_name):
        """Тест нового голоса без сохранения"""
        if voice_name not in self.config["voices"]:
            return f"Голос '{voice_name}' не найден."
        
        temp_config = dict(self.config)
        temp_config["current_voice"] = voice_name
        temp_speaker = Speaker(temp_config)
        temp_speaker.speak("Это тест нового голоса.")
