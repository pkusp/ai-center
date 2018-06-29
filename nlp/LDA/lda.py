# encoding: utf-8
"""
@author: shipeng
@contact: peng_shi@shannonai.com

@version: 1.0
@file: lda.py
@time: 2018/6/14 下午7:51

这一行开始写关于本文件的说明与解释
"""
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from experiments.nlp import config
from collections import namedtuple
import os
import jieba


class LDAModel(object):
    def __init__(self):
        self.ref_url = 'https://blog.csdn.net/wind_blast/article/details/53815757'

    def __repr__(self):
        return self.ref_url


class LDATrain(object):
    def __init__(self):
        self.ref_url_1 = 'https://www.cnblogs.com/pinard/p/6908150.html'
        self.ref_readline = 'https://www.jianshu.com/p/a672f39287c4'
        self.doc_path = os.path.join(config.PACKAGE_PATH, 'LDA/doc')
        self.doc_name_list = os.listdir(self.doc_path)
        self.stop_words_file = os.path.join(config.PACKAGE_PATH, 'doc/stop_words.txt')

    def __repr__(self):
        return self.ref_url_1

    def data_processing(self):
        doc_tuple_list = self.jieba_cut()
        self.save_cut_file(doc_tuple_list)

    def jieba_cut(self) -> list:  # [(filename,content),(),...]
        """

        Returns: 读取/doc下的文件(不以'cut.txt'结尾),并用cut返回文件名和对应cut后的内容的list

        """
        doc_tuple_list = []
        jieba.suggest_freq('<需要强行被切分出来的词>', True)
        jieba.suggest_freq('<需要强行被切分出来的词>', True)
        for filename in self.doc_name_list:
            if not filename.endswith('cut.txt'):
                with open(os.path.join(self.doc_path, filename), mode='r', encoding='GBK') as f:
                    document = f.read()  # read([size]) 默认全部读完
                    doc_cut_list = jieba.cut(document)
                    doc_cut_content = ' '.join(doc_cut_list)
                    doc_tuple_list.append((filename, doc_cut_content))
        return doc_tuple_list

    def save_cut_file(self, doc_tuple_list: list):
        """

        Args:
            doc_tuple_list: [(<raw文件名>，<after_cut文件内容str>)，...]

        Returns: 将传入的doc_tuple分别写入文件，新文件名为旧文件名加上后缀'_cut.txt'

        """
        for filename, doc_cut in doc_tuple_list:
            with open(os.path.join(self.doc_path, filename[:len('.txt')] + '_cut.txt'), mode='w', encoding='GBK') as f:
                f.write(doc_cut)

    def get_stopwords(self) -> list:
        file_full_name = self.stop_words_file
        with open(file_full_name, mode='r', encoding='utf-8') as f:
            stop_words = f.read()
            stop_list = stop_words.splitlines(keepends=False)  # 分行,不保留分隔符
        return stop_list

    def get_cut_file(self) -> list:
        """

        Returns: 分好词的文件内容list

        """
        cut_files = []
        for name in os.listdir(self.doc_path):
            if name.endswith('cut.txt'):
                with open(os.path.join(self.doc_path, name)) as cut_f:
                    cut_f.read()
                    cut_files.append(cut_f)
        return cut_files

    def lda_train(self):
        corpus = self.get_cut_file()
        cntVector = CountVectorizer(stop_words=self.get_stopwords())
        cntTF = cntVector.fit_transform(corpus)
        lda = LatentDirichletAllocation(n_topics=2, learning_offset=50., random_state=0)
        doc_res = lda.fit_transform(cntTF)
        # 通过fit_transform函数，我们就可以得到文档的主题模型分布在docres中。
        # 而主题词 分布则在lda.components_中。我们将其打印出来：
        print(doc_res)
        print(lda.components_)
