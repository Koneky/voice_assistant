import speech_recognition as sr


class Listener:

    def __init__(self, config):
        self.recognizer = sr.Recognizer()
        self.language = config.get("language", "ru-RU")
        self.microphone = sr.Microphone()

    def listen(self):

        with self.microphone as source:
            print("[CTT] Слушаю...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            audio = self.recognizer.listen(source)

        try:
            print("[CTT] Распознаю речь...")
            text = self.recognizer.recognize_google(audio, language=self.language)
            print(f"[CTT] Вы сказали, {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("[CTT] Не удалось распознать речь.")
            return None
        except sr.RequestError:
            print("[CTT] Ошибка сервиса распознавания речи.")
            return None

