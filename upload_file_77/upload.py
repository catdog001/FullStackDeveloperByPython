# coding: utf-8
import flask
from flask import Flask, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
from upload_file_77.forms import UploadForm
# 将两个不可变字典组合成一个字典
from werkzeug.datastructures import CombinedMultiDict

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
        # 用CombinedMultiDict 合并两个不可变的字典
        form = UploadForm(CombinedMultiDict([flask.request.form, flask.request.files]))
        # 如果验证成功
        if form.validate():
            # 获取描述信息, request.form不可变字典
            desc = flask.request.form.get("desc")
            avatar = flask.request.files.get("avatar")
            """
            desc 和 avator 也可以用这两行，只需要把上面两行 get 代码换成下面两行也是对的
            desc = form.desc.data
            avatar = form.avatar.data
            """
            filename = secure_filename(avatar.filename)
            avatar.save(os.path.join(UPLOAD_PATH, filename))
            print(desc)
            return "文件上传成功"
        else:
            print(form.errors)
            return "fail"


@app.route("/images/<file_name>")
def get_images(file_name):
    return send_from_directory(UPLOAD_PATH, file_name)


if __name__ == '__main__':
    app.run(debug=True)
