from assistant.tts import Speaker
from assistant.config import save_config


class VoiceManager:
    
    def __init__(self, config):
        self.config = config
        self.speaker = Speaker(config)

    def list_voices(self):
        return self.speaker.list_voices()
    
    def set_voice(self, index):
        self.config["voice"] = index
        save_config(self.config)
        self.speaker.set_voice(index)
        return f"Голос переключён на {index}"
    
    def preview_voice(self, index):
        self.speaker.set_voice(index)
        self.speaker.speak("Это тест нового голоса.")
