import logging
import os

def setup_logger(name, log_file="log.log", level=logging.INFO):
    format = logging.Formatter(fmt=f'%(asctime)s.%(msecs)03d {os.getpid():7d} %(name)s %(levelname)s %(message)s',
                               datefmt='%Y-%m-%d %H:%M:%S')

    fileHandler = logging.FileHandler(log_file, mode='a')
    fileHandler.setFormatter(format)
    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(format)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(fileHandler)
    logger.addHandler(consoleHandler)

    return logger