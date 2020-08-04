import flask
import loguru

from simple_downloader import downloader

mod = flask.Blueprint("views", __name__)


@mod.route("/")
def get_index():
    return flask.render_template("index.html", downloads=downloader.get_sorted_downloaded_files())


@mod.route("/delete/<name>")
def get_delete(name):
    try:
        downloader.LocalFile(name).delete()
        flask.flash(f"File '{name}' was deleted.")
    except Exception as e:
        loguru.logger.error(str(e))
        flask.flash(str(e))

    return flask.redirect(flask.url_for("views.get_index"))


@mod.route("/downloads")
def get_downloads():
    data = [f.to_dict() for f in downloader.get_sorted_downloaded_files()]

    return flask.jsonify(data=data)


@mod.route("/download", methods=["POST"])
def post_download():
    try:
        file = downloader.RemoteFile(flask.request.form["url"])
        file.download()
        flask.flash(f"Download of '{file.name}' was started.")
    except Exception as e:
        loguru.logger.error(str(e))
        flask.flash(str(e))

    return flask.redirect(flask.url_for("views.get_index"))
