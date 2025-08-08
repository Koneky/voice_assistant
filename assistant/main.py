from assistant.config import load_config
from assistant.tts import Speaker
from assistant.stt import Listener
from assistant.intents import handle_command
from assistant.wake_word import WakeWordDetector


def main():
    config = load_config()
    speaker = Speaker(config)
    listener = Listener(config)
    wake_detector = WakeWordDetector(config)

    speaker.speak("Ассистент запущен. Скажите ключевое слово для активации.")

    try:
        while True:
            
            if not wake_detector.wait_for_wake_word():
                continue

            speaker.speak("Слушаю вас.")

            command = listener.listen()

            if not command:
                continue

            response = handle_command(command, config)
            speaker.speak(response)
    except KeyboardInterrupt:
        speaker.speak("Ассистент завершает работу.")


if __name__ == "__main__":
    main()
