from .app import Flask


# 注册flask的核心对象
def create_app():
    # __name__为当前文件
    app = Flask(__name__)
    return app