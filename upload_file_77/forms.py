# coding: utf-8
# 判断输入类型
from wtforms import Form, FileField, StringField
# 载入 输入必须的
from wtforms.validators import InputRequired
# 判断输入文件类型
from flask_wtf.file import FileRequired, FileAllowed


class UploadForm(Form):
    # 图片上传类型
    # FileRequired() 表示必须上传
    # FileAllowed(["类型 1", "类型 2", "类型 3"]) 表示上传的文件必须得以"类型 1", "类型 2", "类型 3" 结尾
    avatar = FileField(validators=[FileRequired(), FileAllowed(["jpg", "png", "gif"])])
    desc = StringField(validators=[InputRequired()])
