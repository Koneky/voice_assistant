import pyttsx3

class Speaker:

    def __init__(self, config):
        self.engine = pyttsx3.init()
        self.voice = config.get("voice", 0)
        self.set_voice(self.voice_index)

    def set_voice(self, index):
        voices = self.engine.getProperty('voices')

        if index < len(voices):
            self.engine.setProperty('voice', voices[index].id)
        else:
            self.engine.setProperty('voice', voices[0].id)

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    def list_voices(self):
        voices = self.engine.getProperty('voices')
        return [(i, voice.name) for i, voice in enumerate(voices)]
