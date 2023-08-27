

from logging.handlers import RotatingFileHandler
import logging
import colorama
colorama.init(autoreset=True)


max_filesize_in_mbs = 20
log_filename = "captcha_solver_logs.log"
file_encoding = "UTF-8"

logging_format = logging.Formatter(
    "%(levelname)s:[%(filename)s:%(lineno)s]:%(asctime)s: %(message)s")
logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler()
console_handler.setFormatter(logging_format)
file_handler = RotatingFileHandler(log_filename, mode='a', maxBytes=max_filesize_in_mbs * 1024 * 1024,
                                   backupCount=2, encoding=file_encoding, delay=False)
file_handler.setFormatter(logging_format)

logger.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)
console_handler.setLevel(logging.DEBUG)

logger.addHandler(console_handler)
logger.addHandler(file_handler)
