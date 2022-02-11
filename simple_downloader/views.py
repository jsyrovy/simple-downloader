import flask
import loguru
from flask import Response

from simple_downloader import downloader
from simple_downloader import drive_space
from simple_downloader.downloader import InvalidUrlError
from simple_downloader.utils import allow_cors

mod = flask.Blueprint("views", __name__)


@mod.route("/delete/<name>")
def get_delete(name):
    try:
        local_file = downloader.LocalFile.from_escaped_name(name)
        local_file.delete()
        flask.flash(f"File '{local_file.name}' was deleted.")
    except Exception as e:
        loguru.logger.error(str(e))
        flask.flash(str(e))

    return flask.redirect(flask.url_for("views.get_index"))


@mod.route("/downloads")
@allow_cors
def get_downloads():
    data = [f.to_dict() for f in downloader.get_sorted_downloaded_files()]

    return flask.jsonify(downloads=data)


@mod.route("/download", methods=["POST"])
def post_download():
    def _get_response(message: str, status_code: int = 200) -> tuple[Response, int]:
        if status_code >= 400:
            loguru.logger.error(message)
        return flask.jsonify(message=message), status_code

    try:
        file = downloader.RemoteFile(flask.request.form["url"])
        file.download()
        return _get_response(f"Download of '{file.name}' was started.")
    except InvalidUrlError as e:
        return _get_response(str(e), 422)
    except Exception as e:
        return _get_response(str(e), 500)


@mod.route("/drive-space")
@allow_cors
def get_drive_space():
    return flask.jsonify(drive_space.get_drive_space(downloader.FOLDER_DOWNLOADS))
