import os
import glob

from log_utils.logger import Logger
from format_utils.yaml_config import YamlConfig
from archive_utils.zip_util import ZipUtil

def do_unzip(zip_file_path: str, logger: Logger):
    logger.info(f"zip_file_path: {zip_file_path}")
    zip_basename_without_ext: str = os.path.splitext(os.path.basename(zip_file_path))[0]
    zip_dir_path: str = os.path.dirname(zip_file_path)
    dist_zip_dir_path: str = os.path.join(zip_dir_path, f"test_{zip_basename_without_ext}")
    zip_util = ZipUtil(zip_file_path, dist_zip_dir_path)
    zip_util.unzip()

if __name__ == "__main__":
    current_dir_path: str = os.path.dirname(__file__)
    config_yaml_path: str = os.path.join(current_dir_path, "config.yaml")
    app_config: YamlConfig = YamlConfig(config_yaml_path).content
    app_config = app_config["app"]
    logging_config_path: str = app_config["logging_config_path"]
    logging_config_absolute_path: str = os.path.abspath(logging_config_path)
    logger: Logger = Logger(logging_config_absolute_path)

    logger.info(f"start {__file__}")
    logger.info(f"logging_config_absolute_path: {logging_config_absolute_path}")

    source_zip_dir_path: str = app_config["source_zip_dir_path"]
    zip_glob_list = glob.glob(source_zip_dir_path + "/*.zip")
    is_unzipped: bool = bool(app_config["is_unzipped"])
    if(is_unzipped):
        for zip_file_path in sorted(zip_glob_list):
            do_unzip(zip_file_path)
