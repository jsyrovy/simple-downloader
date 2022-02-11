import datetime
import enum
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
ESCAPED_NAME_SEPARATOR = "|"
IGNORED_FILES = (".ds_store", "._.ds_store")


class InvalidUrlError(Exception):
    ...


class RemoteFile:
    def __init__(self, url: str) -> None:
        self.__url = urllib.parse.urlparse(url)
        self.name = pathlib.Path(self.__url.path).name

        if not self.__is_valid():
            raise InvalidUrlError("URL isn't valid.")

    def download(self) -> None:
        Downloader().download(self.__url.geturl(), self.name)

    def __is_valid(self) -> bool:
        return all([self.__url.scheme, self.__url.netloc, self.__url.path])


class Downloader:
    def __init__(self) -> None:
        self.__app = "wget"

        if not self.__is_available():
            raise AttributeError("<a href='https://www.gnu.org/software/wget/' target='_blank' "
                                 "rel='noopener noreferrer'>WGET</a> isn't installed.")

    def download(self, url: str, name: str) -> None:
        args = [self.__app, "-bc", "-o", f"wget_logs/{name}", "-P", "downloads", url]
        subprocess.run(args)
        loguru.logger.debug(f"Process {args} was run.")

    def __is_available(self) -> bool:
        return shutil.which(self.__app) is not None


class FileType(enum.Enum):
    GENERAL = "file-o"
    ARCHIVE = "file-archive-o"
    AUDIO = "file-audio-o"
    IMAGE = "file-image-o"
    PDF = "file-pdf-o"
    VIDEO = "file-video-o"


class LocalFile:
    def __init__(self, path: pathlib.Path) -> None:
        self.path = path
        self.name = self.path.name if str(self.path.parent) == FOLDER_DOWNLOADS else "/".join(self.path.parts[1:])
        self.escaped_name = self.name.replace("/", ESCAPED_NAME_SEPARATOR)
        self.type = get_file_type(self.path)
        self.__date = datetime.datetime.fromtimestamp(self.path.stat().st_ctime)
        self.size = hurry.filesize.size(self.path.stat().st_size)
        self.__wget_log = WgetLog(self.name)
        self.progress = self.__wget_log.progress

    def delete(self) -> None:
        self.__wget_log.delete()
        self.path.unlink()
        loguru.logger.debug(f"LocalFile '{self.name}' was deleted.")

    def get_date(self) -> datetime.datetime:
        if self.__wget_log.date:
            return self.__wget_log.date

        return self.__date

    def to_dict(self) -> dict:
        return {"type": f"<i class='fa fa-{self.type.value}'></i>",
                "name": self.name,
                "date": self.get_date().strftime("%Y-%m-%d %H:%M:%S"),
                "size": self.size,
                "progress": self.progress,
                "actions": f"<a href='{flask.url_for('views.get_delete', name=self.escaped_name)}'><i class='fa fa-trash'></i></a>"
                           "&nbsp;&nbsp;&nbsp;"
                           f"<a href='https://www.google.com/search?q={self.__get_clean_name()}' target='_blank' "
                           "rel='noopener noreferrer'><i class='fa fa-info'></i></a>"}

    def __get_clean_name(self):
        name = self.path.name.replace(self.path.suffix, "")
        banned_chars = [".", "-", "_"]

        for char in banned_chars:
            name = name.replace(char, " ")

        return name

    @staticmethod
    def from_escaped_name(name: str) -> "LocalFile":
        path = pathlib.Path(FOLDER_DOWNLOADS) / name.replace(ESCAPED_NAME_SEPARATOR, "/")
        return LocalFile(path)


class WgetLog:
    def __init__(self, name: str) -> None:
        self.__name = name
        self.__path = pathlib.Path(FOLDER_WGET_LOGS) / name
        self.__lines = ""
        self.progress = "N/A"
        self.date = None

        if not self.__path.exists():
            loguru.logger.warning(f"Path '{self.__path}' doesn't exist.")
            return

        self.__set_lines()
        self.__set_progress()
        self.date = datetime.datetime.fromtimestamp(self.__path.stat().st_ctime)

    def delete(self) -> None:
        if self.__path.exists():
            self.__path.unlink()
            loguru.logger.debug(f"WgetLog '{self.__name}' was deleted.")

    def __set_lines(self) -> None:
        with open(self.__path, "r", encoding="utf-8") as f:
            self.__lines = f.read().split("\n")

    def __set_progress(self) -> None:
        for line in reversed(self.__lines):
            match = re.search(r"\d*%", line)
            if match:
                self.progress = match.group(0)
                return


def get_sorted_downloaded_files() -> list[LocalFile]:
    dirs = [path for path in pathlib.Path(FOLDER_DOWNLOADS).rglob("*") if path.is_dir() and not is_dir_hidden(path)]
    dirs.append(pathlib.Path(FOLDER_DOWNLOADS))
    files = []

    for directory in dirs:
        files.extend([LocalFile(path) for path in directory.glob("*") if path.is_file() and path.name.lower() not in IGNORED_FILES])

    files.sort(key=lambda f: f.get_date(), reverse=True)
    loguru.logger.debug([file.name for file in files])
    return files


def is_dir_hidden(path: pathlib.Path) -> bool:
    hidden_file = path / ".hidden"
    return hidden_file.exists()


def get_file_type(path: pathlib.Path) -> FileType:
    extension = path.suffix.lower()[1:]

    if extension in ["7z", "gz", "rar", "tar", "zip"]:
        return FileType.ARCHIVE

    if extension in ["amr", "flac", "m4a", "mid", "mp3", "ogg", "wav"]:
        return FileType.AUDIO

    if extension in ["bmp", "gif", "ico", "jpeg", "jpg", "png", "psd", "tif"]:
        return FileType.IMAGE

    if extension == "pdf":
        return FileType.PDF

    if extension in ["avi", "flv", "m4v", "mkv", "mov", "mp4", "mpg", "webm", "wmv"]:
        return FileType.VIDEO

    return FileType.GENERAL
