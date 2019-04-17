# _*_ coding: utf-8 _*_
# @time     : 2019/04/15
# @Author   : Amir
# @Site     : 
# @File     : settings.py
# @Software : PyCharm


import os
import redis

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_FOLDER = os.path.join(BASE_DIR, 'templates')
STATIC_FOLDER = os.path.join(BASE_DIR, 'static')
UPLOAD_FOLDER = os.path.join(STATIC_FOLDER, 'upload')


def get_db_uri(dbinfo):
    ENGINE = dbinfo.get('ENGINE') or 'mysql'
    DRIVER = dbinfo.get('DRIVER') or 'pymysql'
    USER = dbinfo.get('USER') or 'root'
    PASSWORD = dbinfo.get('PASSWORD') or '123456'
    HOST = dbinfo.get('HOST') or 'localhost'
    PORT = dbinfo.get('PORT') or '3306'
    NAME = dbinfo.get('NAME') or 'test'

    return '{}+{}://{}:{}@{}:{}/{}'.format(ENGINE, DRIVER, USER, PASSWORD, HOST, PORT, NAME)


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = 'sfsdfkjgjkbdf55s6765434sdf64sds'
    SESSION_TYPE = 'redis'
    SESSION_REDIS = redis.Redis(host='127.0.0.1', port=6379)
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopConfig(Config):
    DEBUG = True
    DATABASE = {
        'ENGINE': 'mysql',
        # 'DRIVER': 'pymysql',
        'DRIVER': 'mysqlconnector',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'aj'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class TestingConfig(Config):
    TESTING = True
    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'flaskproject'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class StagingConfig(Config):
    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'flaskproject'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


class ProductConfig(Config):
    DATABASE = {
        'ENGINE': 'mysql',
        'DRIVER': 'pymysql',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
        'NAME': 'flaskproject'
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(DATABASE)


envs = {
    'develop': DevelopConfig,
    'testing': TestingConfig,
    'product': ProductConfig,
    'staging': StagingConfig
}
