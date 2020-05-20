import datetime
import pathlib
import re
import shutil
import subprocess
import urllib.parse

import flask
import hurry.filesize
import loguru

FOLDER_DOWNLOADS = "downloads"
FOLDER_WGET_LOGS = "wget_logs"


class RemoteFile:
    def __init__(self, url):
        self.__url = urllib.parse.urlparse(url)
        self.name = pathlib.Path(self.__url.path).name

        if not self.__is_valid():
            raise AttributeError("URL isn't valid.")

    def download(self):
        Downloader().download(self.__url.geturl(), self.name)

    def __is_valid(self):
        return all([self.__url.scheme, self.__url.netloc, self.__url.path])


class Downloader:
    def __init__(self):
        self.__app = "wget"

        if not self.__is_available():
            raise AttributeError("<a href='https://www.gnu.org/software/wget/' target='_blank' "
                                 "rel='noopener noreferrer'>WGET</a> isn't installed.")

    def download(self, url, name):
        args = [self.__app, "-bc", "-o", f"wget_logs/{name}", "-P", "downloads", url]
        subprocess.run(args)
        loguru.logger.debug(f"Process {args} was run.")

    def __is_available(self):
        return shutil.which(self.__app) is not None


class LocalFile:
    def __init__(self, name):
        self.name = name
        self.path = pathlib.Path(FOLDER_DOWNLOADS) / name
        self.creation_date = datetime.datetime.fromtimestamp(self.path.stat().st_ctime).strftime("%Y-%m-%d %H:%M:%S")
        self.size = hurry.filesize.size(self.path.stat().st_size)
        self.__wget_log = WgetLog(self.name)
        self.progress = self.__wget_log.progress
        self.delete_url = flask.url_for("get_delete", name=self.name)

    def delete(self):
        self.__wget_log.delete()
        self.path.unlink()
        loguru.logger.debug(f"LocalFile '{self.name}' was deleted.")


class WgetLog:
    def __init__(self, name):
        self.__name = name
        self.__path = pathlib.Path(FOLDER_WGET_LOGS) / name
        self.__lines = ""
        self.progress = "N/A"

        if not self.__path.exists():
            loguru.logger.warning(f"Path '{self.__path}' doesn't exist.")
            return

        self.__set_lines()
        self.__set_progress()

    def delete(self):
        if self.__path.exists():
            self.__path.unlink()
            loguru.logger.debug(f"WgetLog '{self.__name}' was deleted.")

    def __set_lines(self):
        with open(self.__path, "r", encoding="utf-8") as f:
            self.__lines = f.read().split("\n")

    def __set_progress(self):
        for line in reversed(self.__lines):
            match = re.search(r"\d*%", line)
            if match:
                self.progress = match.group(0)
                return


def get_sorted_downloaded_files():
    files = [LocalFile(path.name) for path in pathlib.Path(FOLDER_DOWNLOADS).glob("*")]
    files.sort(key=lambda f: f.creation_date, reverse=True)
    loguru.logger.debug([file.name for file in files])
    return files
