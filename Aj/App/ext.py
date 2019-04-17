# _*_ coding: utf-8 _*_
# @time     : 2019/04/15
# @Author   : Amir
# @Site     : 
# @File     : ext.py
# @Software : PyCharm


from flask_migrate import Migrate
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
migrate = Migrate()
se = Session()


def init_ext(app):
    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    se.init_app(app=app)