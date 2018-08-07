# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: eda.py
@time: 2018/7/29 下午2:18

这一行开始写关于本文件的说明与解释
"""
from datetime import datetime
import os
import csv
import logging
from competitions import config
import numpy as np

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

logger = logging.getLogger(__name__)

proj_path = os.path.join(config.PROJECT_PATH, 'article_class_2018_DataCastle')
art_doc = os.path.join(config.PROJECT_PATH, 'article_class_2018_DataCastle/article_class_2018/doc')
article_path = os.path.join(config.PROJECT_PATH, 'article_class_2018_DataCastle')
data_path = os.path.join(article_path, 'data_raw')
train_csv = os.path.join(data_path, 'train_set.csv')
test_csv = os.path.join(data_path, 'test_set.csv')

print('___project path____: ', article_path)


class EDA(object):
    def __init__(self):
        self.classs_name = self.__class__.__name__

    def csv_file(self):
        train_data = csv.reader(open(train_csv, encoding='utf-8'))
        test_data = csv.reader(open(test_csv, encoding='utf-8'))
        for d in test_data:
            print(d)

    def eda(self):
        """
        :return:
        train--> Index(['id', 'article', 'word_seg', 'class'], dtype='object')
        test--> Index(['id', 'article', 'word_seg'], dtype='object')
        train lines:  102245
        test lines:  102277
        article size:  4785
        word_seg size:  3062

        """
        columns = ['id', 'article', 'word_seg', 'class']
        train_df = pd.read_csv(train_csv)
        train_df = train_df[train_df['class']>-1]
        test_df = pd.read_csv(test_csv)
        # print(test_df.head())
        train_lines = train_df.iloc[:, 0].size
        test_lines = test_df.iloc[:, 0].size

        article_tmp = len(train_df.iloc[1, 1].split())
        word_seg_tmp = len(train_df.iloc[1,2].split())

        y = (train_df["class"] - 1).astype(int)
        # for cls in range(train_lines):
        #     if np.isnan(train_df.iloc[cls,3]):
        #         # print(cls.astype(int))
        #         print('None')
        print(y)
        print('train keys: ',train_df.keys())
        print('test keys: ',test_df.keys())
        print('train lines: ',train_lines)
        print('test lines: ',test_lines)
        print('article size: ',article_tmp)
        print('word_seg size: ',word_seg_tmp)
        # print('word_seg example: ',train_df.iloc[1,2])

    def open_as_txt(self):
        cls_set = set()
        print(cls_set)
        with open(train_csv,mode='r',encoding='utf-8') as f:
            for i in range(100000):
                line = f.readline()
                cls = line.strip().split(',')[3]
                cls_set.add(cls)
        cls_list = list(cls_set-{'class'})
        cls_list = sorted(cls_list,key=lambda x:int(x))
        print(cls_list)


class PreData(object):
    def __init__(self):
        print("____pre data______")
        self.model_name="pre-data"
        self.seg_column = "word_seg"
        self.label_column = "class"
        self.train_doc = None
        self.label_doc =None
        self.test_doc = None

    def data_clean(self):
        # seg_column = "word_seg"
        # label_colum = "class"
        train_input = pd.read_csv(os.path.join(proj_path, 'data_raw/train_set.csv'))
        train_input = train_input[train_input['class'] > -1]  # 去掉类别为空的数据
        test_input = pd.read_csv(os.path.join(proj_path, 'data_raw/test_set.csv'))
        train_doc = train_input[self.seg_column]
        label_doc = (train_input[self.label_column]-1).astype(int)
        test_doc = test_input#[self.seg_column]
        # test_id = test["id"].copy()
        # vec = TfidfVectorizer(ngram_range=(1, 2), min_df=3, max_df=0.9, use_idf=1, smooth_idf=1, sublinear_tf=1)
        # trn_term_doc = vec.fit_transform(train[column])
        # test_term_doc = vec.transform(test[column])
        print(train_input.head())
        return train_input,test_doc#,label_doc

    def vectorize(self):
        train,test = self.data_clean()
        vec = TfidfVectorizer(ngram_range=(1, 2), min_df=3, max_df=0.9, use_idf=1, smooth_idf=1, sublinear_tf=1)
        train_term_doc = vec.fit_transform(train[self.seg_column])
        test_term_doc = vec.transform(test[self.seg_column])
        label = (train[self.label_column]-1).astype(int)
        return train_term_doc,test_term_doc,label


def save_data(preds,model_name):
    save_file = open(os.path.join(art_doc, model_name+str(datetime.now().date())+'.csv'), mode='w')
    save_file.write("id,class" + "\n")
    for i,item in enumerate(preds):
        save_file.write(str(i) + "," + str(item + 1) + "\n")
        # i = i + 1
    save_file.close()


if __name__ == '__main__':
    import time
    t1 = time.time()
    eda = EDA()
    eda.eda()
    t2 = time.time()
    print('run {}s'.format(round(t2-t1,4)))











