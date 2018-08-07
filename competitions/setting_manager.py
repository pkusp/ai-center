# encoding: utf-8
"""
@author: pkusp
@contact: pkudp@outlook.com

@version: 1.0
@file: setting_manager.py
@time: 2018/6/13 下午7:50

这一行开始写关于本文件的说明与解释
"""
import os


class _Settings(object):
    def __init__(self):
        #  当前脚本所在的目录：
        # self.PACKAGE_PATH = os.path.relpath(__file__)
        self.PACKAGE_PATH = os.path.abspath(__file__)
        #  当前脚本所在的上一层目录：
        self.PROJECT_PATH = os.path.dirname(self.PACKAGE_PATH)

    def load_conf(self):
        pass


config = _Settings()
