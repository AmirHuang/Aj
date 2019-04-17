# _*_ coding: utf-8 _*_
# @time     : 2019/04/15
# @Author   : Amir
# @Site     : 
# @File     : user_is_login.py
# @Software : PyCharm

from flask import session, redirect, url_for

from functools import wraps


def is_login(func):
    """
    装饰器用于登录验证
    session['user_id']
    """
    @wraps(func)
    def check_login(*args, **kwargs):
        # 验证登陆
        # 获取是否有user_id
        user_session = session.get('user_id')
        if user_session:
            return func(*args, **kwargs)
        else:
            return redirect(url_for('user.login'))
    return check_login
