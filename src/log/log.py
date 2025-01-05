import logging
from constants.constant import LOG_FOLDER

def log_geral():
    logger = logging.getLogger('RegistroGeral')
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        file_log = logging.FileHandler(LOG_FOLDER / "RegistroGeral.log")
        file_log.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(message)s', datefmt="%d/%m/%Y - %H:%M:%S")
        file_log.setFormatter(formatter)
        logger.addHandler(file_log)
    return logger

