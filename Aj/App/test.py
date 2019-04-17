# _*_ coding: utf-8 _*_
# @time     : 2019/04/15
# @Author   : Amir
# @Site     : 
# @File     : test.py
# @Software : PyCharm


class Login:
    def __init__(self, name, password):
        self.name = name
        self.pwd = password

    def login(self): pass

    @staticmethod
    def get_usr_pwd(xx):  # 静态方法
        usr = input('用户名 ：')
        pwd = input('密码 ：')
        print(xx)
        Login(usr, pwd)


Login.get_usr_pwd('dd')
