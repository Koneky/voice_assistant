from assistant.config import load_config
from assistant.tts import Speaker
from assistant.stt import Listener
from assistant.intents import handle_command


def main():
    config = load_config()
    speaker = Speaker(config)
    listener = Listener(config)

    speaker.speak("Ассистент запущен. Скажите команду.")

    try:
        while True:
            command = listener.listen()

            if not command:
                continue

            response = handle_command(command, config)
            speaker.speak(response)
    except KeyboardInterrupt:
        speaker.speak("Ассистент завершает работу.")


if __name__ == "__main__":
    main()
