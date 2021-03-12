import logging.config

class Logger():
    def __init__(self, logging_config_file_path: str):
        logging.config.fileConfig(logging_config_file_path)
        self.logger = logging.getLogger()

    def exception(self, message: str, exception: Exception, console: bool = False):
        if console:
            print(f'[Error] {message}; {exception}')
        self.logger.exception(message, exception)

    def info(self, message: str, console: bool = False):
        if console:
            print(f'[Info] {message}')
        self.logger.info(message)

    def debug(self, message: str, console: bool = False):
        if console:
            print(f'[Debug] {message}')
        self.logger.debug(message)