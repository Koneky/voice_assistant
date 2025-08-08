import re
from assistant import app_launcher
from assistant.voice_manager import VoiceManager


def handle_command(command, config):
    command = command.lower()

    # Приветствие
    if "привет" in command:
        return "Привет! Чем могу помочь?"
    
    # Открыть приложение
    open_match = re.search(r"открой|запусти\s+(\w+)", command)

    if open_match:
        app_name = open_match.group(1)
        response = app_launcher.launch_app(app_name)
        return response
    
    # Смена голоса
    if "смена голоса" in command or "поменяй голос" in command:
        vm = VoiceManager(config)
        # пробуем найти число в команде
        numbers = re.findall(r"\d+", command)

        if numbers:
            index = int(numbers[0])
            return vm.set_voice(index)
        # пробуем найти ключевые слова
        if "женский" in command:
            return vm.set_voice(0)
        elif "мужской" in command:
            return vm.set_voice(1)
        else:
            voices = vm.list_voices()
            voices_list = ", ".join([f"{i}: {name}" for i, name in voices])
            return f"Скажите номер голоса для переключения. Доступные голоса: {voices_list}"
        
    return "Извините, я не понимаю эту команду."
