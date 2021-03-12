from log_utils.logger import Logger

import os
logging_config_path: str = "src/logging_debug.conf"
logging_config_absolute_path = os.path.abspath(logging_config_path)
print(logging_config_absolute_path)
logger = Logger(logging_config_absolute_path)

logger.info("infotest")