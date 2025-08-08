import speech_recognition as sr


class WakeWordDetector:

    def __init__(self, config):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.wake_word = config.get("wake_word", "хермеус").lower()
        self.language = config.get("language", "ru-RU")

    def wait_for_wake_word(self):

        with self.microphone as source:
            print("[WakeWord] Ошидаю ключевое слово...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language=self.language).lower()
            print(f"[WakeWord] Распознано: {text}")
            return self.wake_word in text
        except sr.UnknownValueError:
            return False
        except sr.RequestError:
            print("[WakeWord] Ошибка сервиса распознавания речи.")
            return False
