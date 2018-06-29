# encoding: utf-8
"""
@author: shipeng
@contact: peng_shi@shannonai.com

@version: 1.0
@file: play.py
@time: 2018/6/28 下午11:08

这一行开始写关于本文件的说明与解释
"""
from experiments.nlp import config
import os

path = config.PACKAGE_PATH

print(path)

sanguo = os.path.join(path, 'doc/三国演义(第一回).txt')

with open(sanguo, mode='r', encoding='utf-8') as f:

    # for line in f:
    #     print(type(line))
    # for line in f.readlines():
    #     print('read:', type(line))
    print(type(f.readlines()))
    print(f.readline())
    print(f.readline())
    print(f.readline())
    print(type(f.readline()))

