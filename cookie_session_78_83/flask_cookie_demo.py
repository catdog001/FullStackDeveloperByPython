# coding: utf-8
from flask import Flask, Request, Response
from datetime import datetime, timedelta

app = Flask(__name__)


@app.route("/")
def set_cookie():
    resp = Response("设置 cookie")
    # max_age s为单位
    # resp.set_cookie("username", "zhiliao", max_age=60)
    # expires 在浏览器展示时会自动加 8 个小时，因为我们处于东八区，默认是格林尼治时间，要相对北京时间少 8 小时
    # 设置绝对时间
    expires = datetime(year=2020, month=3, day=9, hour=0, minute=0, second=0)
    # 相对时间, 比如，31 天过期，考虑到 8 小时时差，应该设置距离现在 30 天 16 小时
    expires = datetime.now() + timedelta(days=30, hours=16)
    # expires 在新 http 协议中被废弃，但是截至目前为止，仍然可以使用
    # max_age 在 IE8 以下的浏览器不支持
    # 如果同时设置 expires 和 max_age两个参数，以 max_age 为准
    # 如果都不设置 expires 和 max_age两个参数，默认以浏览器会话结束为截止日期，浏览会话结束是指整个浏览器全部关闭，而不是指关闭网页
    resp.set_cookie("username", "zhiliao", expires=expires)
    return resp


@app.route("/del/")
def delete_cookie():
    resp = Response("删除 cookie")
    resp.delete_cookie("username")
    return resp


if __name__ == '__main__':
    app.run(debug=True)