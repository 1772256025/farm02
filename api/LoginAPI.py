"""
    封装类:
        封装请求函数(只有一个登录函数)
"""
import app


class Login:

    # 调用 初始化 函数，封装 URL
    def __init__(self):
        self.login_url = app.BASE_URL + "/api/sys/login"

    # 编写登录函数:
    # 参数： session + mobile + password
    # 响应: 响应结果返回给调用者
    def login(self,session,mobile,password):
        my_login = {"mobile":mobile,
                    "password":password}
        return session.post(self.login_url,json=my_login)

