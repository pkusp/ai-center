# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: w2v_train.py
@time: 2018/6/21 下午9:11

这一行开始写关于本文件的说明与解释
"""
import logging
import os
from datetime import datetime
import jieba
from gensim.models import Word2Vec

from experiments.nlp import config

raw_doc_path = os.path.join(config.PACKAGE_PATH, 'doc')

print('raw::',raw_doc_path)


class Word2VecTrain(object):
    """


    """
    def __init__(self, input_docs_path, model_name=None):
        self.class_name = self.__class__.__name__
        self.input_docs_path = input_docs_path
        self.project_path = os.path.join(config.PACKAGE_PATH, 'word2vec')
        print('PATH::::::::',config.PACKAGE_PATH)
        self.docs_path = os.path.join(self.project_path,'doc')
        self.now_str = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        self.model_name = 'w2v_model_'+self.now_str
        # self.model_path = os.path.join(self.project_path, model_name)
        if model_name is None:
            self.model = self.train_w2v(self.input_docs_path)
            self.save_w2v(self.docs_path,self.model_name)
        else:
            self.model = self.load_w2v(self.docs_path)

    def __repr__(self):
        return self.class_name

    def date_pre(self):
        pass

    def jieba_cut(self, sentence_path)->list:
        """
        # TODO: BUG HERE
        Args:
            sentence_path: 文件路径

        Returns: jieba分词后的list

        """
        cut_sentences = []
        with open(sentence_path,mode='r') as f:
            sentence = f.readlines()
            print(sentence)
            cut_sentence = jieba.cut(sentence[0])
            cut_sentences+=cut_sentence
        return cut_sentence

    def train_w2v(self, docs_path,doc_name=None):
        """
        sentence: input sentence

        1.sg=1是skip-gram算法，对低频词敏感；默认sg=0为CBOW算法。

        2.size是输出词向量的维数，值太小会导致词映射因为冲突而影响结果，值太大则会耗内存并使算法计算变慢，一般值取为100到200之间。

        3.window是句子中当前词与目标词之间的最大距离，3表示在目标词前看3-b个词，后面看b个词（b在0-3之间随机）。

        4.min_count是对词进行过滤，频率小于min-count的单词则会被忽视，默认值为5。

        5.negative和sample可根据训练结果进行微调，sample表示更高频率的词被随机下采样到所设置的阈值，默认值为1e-3。

        6.hs=1表示层级softmax将会被使用，默认hs=0且negative不为0，则负采样将会被选择使用。

        7.workers控制训练的并行，此参数只有在安装了Cpython后才有效，否则只能使用单核。

        """
        if doc_name is None:
            doc_name = os.listdir(docs_path)[3]
            print('[训练文件]：{}'.format(doc_name))
        else:
            print('[训练文件]：{}'.format(doc_name))
        train_doc_path = os.path.join(docs_path,doc_name)
        sentence = self.jieba_cut(train_doc_path)
        print(sentence)
        # print(sentence)
        # print([s for s in sentence])
        model = Word2Vec(sentences=sentence, sg=1, size=100, window=5,
                         min_count=5, negative=3, sample=0.001, hs=1, workers=4)
        return model

    def save_w2v(self, save_path,save_name):
        self.model.save(os.path.join(save_path,save_name))

    def load_w2v(self, load_path):
        for file_name in os.listdir(load_path):
            if file_name.startswith('w2v_model_'):
                model = Word2Vec.load(os.path.join(load_path,file_name))
                return model
            else:
                raise Exception('No model in {}, please train a new model'.format(load_path))

    def model_action(self, method, *word):
        self.model.most_similar(positive=['woman', 'king'], negative=['man'])  # 输出[('queen', 0.50882536), ...]
        self.model.doesnt_match('cat dog pig dinner'.split())  # output: dinner
        self.model.similarity('woman', 'man')  # output: 0.732
        self.model(['computer'])  # raw numpy vector of a word, array([,,,,])

        w2v_compute = getattr(self.model, method)
        w2v_compute(*word)


def w2v_action():
    model_name = 'simple_model'
    w2v = Word2VecTrain(input_docs_path=raw_doc_path, model_name=None)
    w2v.model_action('similarity', 'man', 'woman')


def w2v_construct():
    pass


if __name__ == '__main__':

    w2v_action()
