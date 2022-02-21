import logging
from logging.handlers import TimedRotatingFileHandler
import os

def format_header():
    hander = logging.StreamHandler()
    hander.setFormatter(logging.Formatter('[%(asctime)s %(name)s] %(levelname)s: %(message)s', "%Y/%m/%d %H:%M:%S"))
    return hander

def file_hander(name: str):
    if not os.path.exists("./logs/"):
        os.makedirs("./logs/")
    handler = TimedRotatingFileHandler(f"./logs/app-{name}", when="midnight", interval=1, encoding='utf-8')
    handler.suffix = "%Y%m%d.log"
    return handler

def logd(name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    format = format_header()
    fh = file_hander(name)
    fh.setFormatter(format)
    logger.addHandler(fh)
    logger.addHandler(format)
    return logger
    
log: logging.Logger = logd("main")