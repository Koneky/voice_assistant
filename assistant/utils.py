import platform
import logging


def setup_logger(name=__name__, level=logging.DEBUG):
    logger = logging.getLogger(name)

    if not logger.hasHandlers():
        handler = logger.StreamHandler()
        formatter = logger.Formatter('[%(asctime)s] %(levelname)s: %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(level)
    return logger

def get_os():
    return platform.system()

def clean_text(text):
    return ' '.join(text.strip().split())

def seconds_to_hms(seconds):
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h:02}:{m:02}:{s:02}"
