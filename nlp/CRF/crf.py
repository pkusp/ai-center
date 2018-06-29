# encoding: utf-8
"""
@author: shipeng
@contact: peng_shi@shannonai.com

@version: 1.0
@file: crf.py
@time: 2018/6/15 下午8:04

这一行开始写关于本文件的说明与解释
"""
import codecs
import sys

import CRFPP  # CRF++


class CRFModel(object):
    def __init__(self):
        pass

    def __repr__(self):
        pass


class CRFTrain(object):
    def __init__(self):
        self.class_name = self.__class__.__name__
        self.CRF_SOURCE = ''
        self.ref_url = 'https://blog.csdn.net/u010189459/article/details/38546115'
        self.corpus = 'http://sighan.cs.uchicago.edu/bakeoff2005/'
        self.ref_url_52nlp = 'http://www.52nlp.cn/%E4%B8%AD%E6%96%87%E5%88%86%E8%AF%8D%E5%85%A5%E9%97%A8%E4%B9%8B%E5%AD%97%E6%A0%87%E6%B3%A8%E6%B3%954'
        self.strategy = ['2-tag','4-tag','6-tag']

    def __repr__(self):
        return self.class_name




