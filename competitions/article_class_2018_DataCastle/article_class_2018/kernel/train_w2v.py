# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: train_w2v.py
@time: 2018/7/29 下午5:15

这一行开始写关于本文件的说明与解释
"""
import os
from datetime import datetime
from competitions import config
import jieba
from gensim.models import Word2Vec


class ArticleNumberW2V(object):
    """
    训练用数字表示文字的word2vec

    """
    def __init__(self, input_docs_path, save_model_name=None):
        self.class_name = self.__class__.__name__
        self.input_docs_path = input_docs_path
        self.project_path = os.path.join(config.PACKAGE_PATH, 'word2vec')
        print('PATH::::::::',config.PACKAGE_PATH)
        self.docs_path = os.path.join(self.project_path,'doc')
        self.now_str = datetime.now().strftime("%Y-%m-%d-%H:%M:%S")
        self.model_name = 'w2v_model_'+self.now_str

    def __repr__(self):
        return self.model_name

    def date_pre(self):
        pass

    def jieba_cut(self, sentence_path)->list:
        """
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
