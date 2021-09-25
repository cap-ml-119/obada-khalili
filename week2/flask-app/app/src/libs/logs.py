import logging

import sys

logger = logging.getLogger(__name__)
console_handler = logging.StreamHandler(sys.stdout)
log_formatter = logging.Formatter("[%(asctime)s] [%(process)s] [%(levelname)s]  %(message)s",
                                  datefmt='%Y-%m-%d %H:%M:%S +0000')
console_handler.setFormatter(log_formatter)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)


def get_logger():
    return logger
