# coding: utf-8
import flask
from flask import Flask, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_PATH = os.path.join(os.path.dirname(__file__), "images")


@app.route("/")
def hello_world():
    return "hello world"


@app.route("/upload/", methods=['POST', 'GET'])
def upload():
    if flask.request.method == 'GET':
        return render_template("upload.html")
    else:
        # 获取描述信息
        desc = flask.request.form.get("desc")
        avatar = flask.request.files.get("avatar")
        file_name = secure_filename(avatar.file_name)
        avatar.save(os.path.join(UPLOAD_PATH, file_name))
        return "文件上传成功"


@app.route("/images/<file_name>")
def get_images(file_name):
    return send_from_directory(UPLOAD_PATH, file_name)


if __name__ == '__main__':
    app.run(debug=True)
