import logging

class Logger:
    def __init__(self, filename='html_parser.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s'):
        self.filename = filename
        self.level = level
        self.format = format
        logging.basicConfig(filename=self.filename, level=self.level, format=self.format)

    def log_info(self, message):
        logging.info(message)

    def log_error(self, message):
        logging.error(message)