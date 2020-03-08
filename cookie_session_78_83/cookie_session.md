# cookie

1、cookie 有有效期，服务器可以设置有效期，以后浏览器会自动清除过期的 cookie

2、cookie 有域名的概念，只有访问同一个域名，才会把之前的相同域名返回的cookie 携带给服务器。
也就是说访问谷歌的 cookie 不会返回给百度。

# flask 中的 cookie
1、设置 cookie
设置 cookie是应该在Response 对象上进行设置，`flask.Response`对象有一个`set_cookie`方法，可以通过这个来设置`cookie`<br/>
2、删除 cookie
通过`flask.Response.delete_cookie`，指定 `cookie`的`key`，就可以删除`cookie`了<br/>
3、设置 cookie 的有效期
<li> max_age： 以秒为单位，距离现在多少秒之后过期</li>
<li> expires: 为 datetime 类型，这个时间为格林尼治时间，也就是距离北京时间需要少 8 小时</li>
<li> 如果 max_age 和 expires 都设置了，以 max_age 为准</li>
<li> max_age 在 IE8以下的浏览器是不支持的。expires 虽然在新版 HTTP 协议中是被废弃了，但是到目前为止，所有浏览器还是能够支持的。所以，如果想兼容 IE8以下的浏览器，应该使用 expires，否则可以使用 max_age</li>
<li> 默认过期时间：如果没有显式地指定过期时间，那么这个cookie 将会在浏览器全部关闭后过期</li>

```

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
```
4、设置 cookie 的有效域名
