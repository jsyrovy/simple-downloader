import flask
import loguru

import downloader

__version__ = "1.1"

app = flask.Flask(__name__)
app.config["SECRET_KEY"] = "jGa7jSevicjvhXtUGhpkLKxfpvghFu5e"


@app.route("/")
def get_index():
    return flask.render_template("index.html", downloads=downloader.get_sorted_downloaded_files())


@app.route("/delete/<name>")
def get_delete(name):
    try:
        downloader.LocalFile(name).delete()
        flask.flash(f"File '{name}' was deleted.")
    except Exception as e:
        loguru.logger.error(str(e))
        flask.flash(str(e))

    return flask.redirect(flask.url_for("get_index"))


@app.route("/downloads")
def get_downloads():
    data = [f.to_dict() for f in downloader.get_sorted_downloaded_files()]

    return flask.jsonify(data=data)


@app.route("/download", methods=["POST"])
def post_download():
    try:
        file = downloader.RemoteFile(flask.request.form["url"])
        file.download()
        flask.flash(f"Download of '{file.name}' was started.")
    except Exception as e:
        loguru.logger.error(str(e))
        flask.flash(str(e))

    return flask.redirect(flask.url_for("get_index"))


if __name__ == "__main__":
    app.run(debug=True)
