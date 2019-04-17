# _*_ coding: utf-8 _*_
# @time     : 2019/04/15
# @Author   : Amir
# @Site     : 
# @File     : __init__.py.py
# @Software : PyCharm

from flask import Flask

from App.ext import init_ext
from App.settings import envs
from App.user_views import init_user_blueprint
from App.house_views import init_house_blueprint
from App.order_views import init_order_blueprint


def create_app():
    app = Flask(__name__,
                template_folder=settings.TEMPLATE_FOLDER,
                static_folder=settings.STATIC_FOLDER)
    # 初始化配置
    app.config.from_object(envs.get('develop'))
    # 初始化蓝图
    init_user_blueprint(app)
    init_house_blueprint(app)
    init_order_blueprint(app)

    # 初始化第三方插件
    init_ext(app)
    return app