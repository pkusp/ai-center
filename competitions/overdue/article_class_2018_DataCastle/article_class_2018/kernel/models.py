# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: models.py
@time: 2018/7/29 下午5:17

这一行开始写关于本文件的说明与解释
"""
# import fasttext
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
from pandas import Series,DataFrame
#from sklearn.model_selection import train_test_split
from sklearn import datasets
# from sklearn import cross_validation
import tensorflow as tf
import logging
import xgboost as xgb
from sklearn.decomposition import PCA
from competitions import config
from competitions.article_class_2018_DataCastle.article_class_2018.kernel.eda import PreData
from competitions.article_class_2018_DataCastle.article_class_2018.kernel.eda import save_data
logger = logging.getLogger(__name__)


class BasicModel(object):
    def __init__(self):
        self.model_name = "basic_model"
        self.train_doc=None
        self.test_doc = None
        self.label_doc = None
        self.pre_data()

    def pre_data(self):
        print('___data vectorize___')
        pre_data = PreData()
        self.train_doc,self.test_doc,self.label_doc = pre_data.read_pickle()  # DataFrame格式
        self.label_doc = np.array(self.label_doc).reshape(-1)
        # self.test_doc = np.array(self.test_doc)
        # self.train_doc = np.array(self.train_doc)
        print("_______tran label test shape：:",self.train_doc.shape,self.label_doc.shape,self.test_doc.shape)
        # _______tran label test len: (102244, 2819876) (102244,) (102277, 2819876)
        print(type(self.train_doc))

    def train(self):
        pass

    def save_csv(self):
        preds = self.train()
        save_data(preds,self.model_name)


class XGBModel(BasicModel):
    def __init__(self):
        super(XGBModel,self).__init__()
        self.model_name = "XGBoost"
        print('[xgboost launching]...')
        # import matplotlib.pyplot as plt
        from xgboost.sklearn import XGBClassifier
        from xgboost import plot_importance
        from sklearn.preprocessing import Imputer

    def train(self):
        param = {
            'booster': 'gbtree',
            'objective': 'multi:softmax',  # 多分类的问题
            'num_class':19, # 类别数，与 multisoftmax 并用
            'gamma': 0.1,  # 用于控制是否后剪枝的参数,越大越保守，一般0.1、0.2这样子。
            'max_depth': 5,  # 构建树的深度，越大越容易过拟合
            'lambda': 2,  # 控制模型复杂度的权重值的L2正则化项参数，参数越大，模型越不容易过拟合。
            'subsample': 0.8,  # 随机采样训练样本
            'colsample_bytree': 0.8,  # 生成树时进行的列采样
            # 'min_child_weight': 1,
            # 这个参数默认是 1，是每个叶子里面 h 的和至少是多少，对正负样本不均衡时的 0-1 分类而言
            # ，假设 h 在 0.01 附近，min_child_weight 为 1 意味着叶子节点中最少需要包含 100 个样本。
            # 这个参数非常影响结果，控制叶子节点中二阶导的和的最小值，该参数值越小，越容易 overfitting。
            'silent': 0,  # 设置成1则没有运行信息输出，最好是设置为0.
            'eta': 0.1,  # 如同学习率
            'seed': 1000,
            'nthread':4,# cpu 线程数
            'eval_metric': 'mlogloss'
        }

        train_final = xgb.DMatrix(data=self.train_doc, label=self.label_doc)  ## 数据格式转换
        test_final = xgb.DMatrix(self.test_doc)
        xgb_model = xgb.train(params=param, dtrain=train_final, num_boost_round=100,evals=[(train_final,'train')])

        preds = xgb_model.predict(test_final)
        return preds

    def validation(self):
        pass


class SVMModel(BasicModel):
    def __init__(self):
        super(SVMModel,self).__init__()
        self.model_name="SVM"
        print('[SVM launching]...')

    def train(self):
        from sklearn import svm
        lin_clf = svm.LinearSVC()
        lin_clf.fit(self.train_doc, self.label_doc)
        preds = lin_clf.predict(self.test_doc)
        return preds

    def validation(self):
        pass


class OneClassSvm(object):
    def __init__(self):
        self.model_name = "one_class_SVM"

    def train(self):
        pass


class LSTMModel(BasicModel):
    def __init__(self):
        super(LSTMModel,self).__init__()
        self.model_name = "LSTM"
        logger.info('LSTM launching...')

    def pre_data(self):
        pass

    def train(self):
        pass

    def save_csv(self):
        pass

    def validation(self):
        pass


class PCAMethod(object):
    def __init__(self,data_raw):
        self.model_name = "PCA"
        logger.info("PCA lauching...")
        self.data_raw = data_raw
        self.x_raw,self.xt_raw,self.y_raw = self.load_raw_data()
        self.x_pca=None
        self.y_pca = self.y_raw

    def load_raw_data(self):
        pre_data = PreData()
        return pre_data.vectorize()

    def pca_process(self):
        pca_obj = PCA(n_components='mle',copy=True,svd_solver='auto')
        self.x_pca = pca_obj.fit_transform(self.x_raw)


if __name__ == "__main__":
    # import time
    # t1 = time.time()
    # xgb_ = XGBModel()
    # xgb_.save_csv()
    # # svm_obj = SVMModel()
    # # svm_obj.save_csv()
    # t2 = time.time()
    # print("run {}s".format(round(t2-t1,4)))
    a = tf.constant([1.0,2.0],name='a')
    b = tf.constant([2.0,3.0],name='b')
    result = tf.add(a,b,name='add')
    print(result)
