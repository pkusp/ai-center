# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: word2vec.py
@time: 2018/6/13 下午5:54

这一行开始写关于本文件的说明与解释
"""
import os

from experiments.nlp import config


class World2VecModel(object):
    def __init__(self):
        self.class_name = self.__class__.__name__
        self.key_words = ['负采样','哈夫曼树','CBOW','SKIPGRAM','']
        self.ref_url = 'https://blog.csdn.net/u014595019/article/details/51884529'

    def __repr__(self):
        return self.class_name


if __name__ == '__main__':
    raw_doc_path = os.path.join(config.PACKAGE_PATH,'doc')

