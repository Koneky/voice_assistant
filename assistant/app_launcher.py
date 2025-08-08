import os
import platform
import subprocess


def launch_app(app_name):
    system = platform.system()

    # Кроссплатформенный способ поиска и запуска приложений
    if system == "Windows":
        possible_paths = {
            "chrome": [
                os.path.expandvars(r"%ProgramFiles%\\Google\\Chrome\\Application\\chrome.exe"),
                os.path.expandvars(r"%ProgramFiles(x86)%\\Google\\Chrome\\Application\\chrome.exe")
            ]
        }
        paths = possible_paths.get(app_name.lower(), [])
        
        for path in paths:

            if os.path.exists(path):
                os.startfile(path)
                return f"Запускаю {app_name}"
        return f"{app_name} не найден."
    
    elif system == "Darwin": # macOS
        try:
            subprocess.run(["open", f"-a{app_name}"])
            return f"Запускаю {app_name}"
        except FileNotFoundError:
            return f"{app_name} не найден."
        
    elif system == "Linux":
        try:
            subprocess.Popen([app_name])
            return f"Запускаю {app_name}"
        except FileNotFoundError:
            return f"{app_name} не найден."
        
    return "Операционная система не поддерживается."
