# encoding: utf-8
"""
@author: shipeng
@contact: peng_shi@shannonai.com

@version: 1.0
@file: setting_manager.py
@time: 2018/6/13 下午7:48

这一行开始写关于本文件的说明与解释
"""

import os


class _Settings(object):
    def __init__(self):
        #  当前脚本所在的目录：
        # self.PACKAGE_PATH = os.path.relpath(__file__)
        self.PACKAGE_PATH = os.path.dirname(os.path.abspath(__file__))
        #  当前脚本所在的上一层目录：
        self.PROJECT_PATH = os.path.dirname(self.PACKAGE_PATH)

    def load_conf(self):
        pass


config = _Settings()

if __name__ == '__main__':
    print("path:::",os.path.relpath(__file__))
    print("path:::",os.path.relpath(__file__))
    print("path:::",os.path.abspath(__file__))
    print("path:::",os.path.dirname(os.path.relpath(__file__)))
