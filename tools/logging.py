import logging
import sys


class Logger(logging.Logger):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        encoding='utf-8',
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    @classmethod
    def info(cls, message):
        logging.info(message)

    @classmethod
    def error(cls, message):
        logging.error(message)
