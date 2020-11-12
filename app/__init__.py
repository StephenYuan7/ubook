from .app import Flask


def register_blueprints(app):
    from app.api.v2 import create_blueprint_v2
    app.register_blueprint(create_blueprint_v2(), url_prefix='/v2')


# 注册flask的核心对象
def create_app():
    # __name__为当前文件
    app = Flask(__name__)

    register_blueprints(app)
    return app
