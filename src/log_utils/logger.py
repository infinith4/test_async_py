import logging.config

# def __init__(self, base_path: str, config_file_name: str):
#     self.logging_config_file_path = os.path.join(base_path, config_file_name)

class Logger():
    def __init__(self, logging_config_file_path: str):
        logging.config.fileConfig(logging_config_file_path)
        logging.basicConfig(filename='logfile/logger.log', level=logging.DEBUG)
        self.logger = logging.getLogger()

    def info(self, message, console=False):
        if console:
            print(f'[Info] {message}')
        self.logger.info(message)

    def debug(self, message, console=False):
        if console:
            print(f'[Debug] {message}')
        self.logger.debug(message)
