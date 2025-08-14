import speech_recognition as sr
from assistant.config import load_config


class WakeWordDetector:

    def __init__(self, config):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()


    def get_current_wake_word(self):
        config = load_config()
        current_voice = config["current_voice"]
        return config["voices"][current_voice]["wake_word"].lower(), config.get("language", "ru-RU")


    def wait_for_wake_word(self):
        wake_word, language = self.get_current_wake_word()

        with self.microphone as source:
            print(f"[WakeWord] Ожидаю ключевое слово: '{wake_word}'...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognizer.listen(source)

        
        try:
            text = self.recognizer.recognize_google(audio, language=language).lower()
            print(f"[WakeWord] Распознано: {text}")
            return wake_word in text
        except sr.UnknownValueError:
            return False
        except sr.RequestError:
            print("[WakeWord] Ошибка сервиса распознавания речи.")
            return False
