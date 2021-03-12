import zipfile

class ZipUtil():
    def __init__(self, source_zip_file_path: str, dist_dir_path: str):
        self.source_zip_file_path = source_zip_file_path
        self.dist_dir_path = dist_dir_path

    def unzip(self, num: int):
        with zipfile.ZipFile(self.source_zip_file_path) as zip:
            zip.extractall(self.dist_dir_path)

