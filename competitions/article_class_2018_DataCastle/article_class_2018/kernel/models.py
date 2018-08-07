# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: models.py
@time: 2018/7/29 下午5:17

这一行开始写关于本文件的说明与解释
"""

import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
import pandas as pd
from pandas import Series,DataFrame
#from sklearn.model_selection import train_test_split
from sklearn import datasets
# from sklearn import cross_validation

import xgboost as xgb

from competitions import config
from competitions.article_class_2018_DataCastle.article_class_2018.kernel.eda import PreData
from competitions.article_class_2018_DataCastle.article_class_2018.kernel.eda import save_data


class BasicModel(object):
    def __init__(self):
        self.model_name = "basic_model"
        self.train_doc=None
        self.test_doc = None
        self.label_doc = None
        self.pre_data()

    def pre_data(self):
        print("__pre_data__")
        pre_data = PreData()
        self.train_doc,self.test_doc,self.label_doc = pre_data.vectorize()

    def train(self):
        pass

    def save_csv(self):
        preds = self.train()
        save_data(preds,self.model_name)


class XGBModel(BasicModel):
    def __init__(self):
        super(XGBModel,self).__init__()
        self.model_name = "XGBoost"
        # self.train_doc=None
        # self.test_doc = None
        # self.label_doc = None
        print("_____xgboost running_____")
        # self.pre_data()
    #
    # def pre_data(self):
    #     pre_data_obj = PreData()
    #     self.train_doc,self.test_doc,self.label_doc = pre_data_obj.vectorize()

    def train(self):
        param = {
            'booster': 'gbtree',
            'objective': 'binary:logistic',  # 多分类的问题
            'num_class':18, # 类别数，与 multisoftmax 并用
            'gamma': 0.1,  # 用于控制是否后剪枝的参数,越大越保守，一般0.1、0.2这样子。
            'max_depth': 12,  # 构建树的深度，越大越容易过拟合
            'lambda': 2,  # 控制模型复杂度的权重值的L2正则化项参数，参数越大，模型越不容易过拟合。
            'subsample': 0.7,  # 随机采样训练样本
            'colsample_bytree': 0.8,  # 生成树时进行的列采样
            'min_child_weight': 1,
            # 这个参数默认是 1，是每个叶子里面 h 的和至少是多少，对正负样本不均衡时的 0-1 分类而言
            # ，假设 h 在 0.01 附近，min_child_weight 为 1 意味着叶子节点中最少需要包含 100 个样本。
            # 这个参数非常影响结果，控制叶子节点中二阶导的和的最小值，该参数值越小，越容易 overfitting。
            'silent': 1,  # 设置成1则没有运行信息输出，最好是设置为0.
            'eta': 0.01,  # 如同学习率
            'seed': 1000,
            'nthread':4,# cpu 线程数
            'eval_metric': 'mlogloss'
        }

        train_final = xgb.DMatrix(self.train_doc, label=self.label_doc)  ## 数据格式转换
        test_final = xgb.DMatrix(self.test_doc)
        xgb_model = xgb.train(param, train_final, 100)  # ,watchlist)
        preds = xgb_model.predict(test_final)
        return preds
    #
    # def save_csv(self):
    #     preds = self.train()
    #     save_data(preds,self.model_name)

    def validation(self):
        pass


class LSTMModel(object):
    def __init__(self):
        self.model_name = "LSTM"

    def pre_data(self):
        pass

    def train(self):
        pass

    def save_csv(self):
        pass

    def validation(self):
        pass


class SVMModel(BasicModel):
    def __init__(self):
        super(SVMModel,self).__init__()
        self.model_name="SVM"
        # self.train_doc=None
        # self.test_doc = None
        # self.label_doc = None
        # self.pre_data()

    # def pre_data(self):
    #     print("__pre_data__")
    #     pre_data = PreData()
    #     self.train_doc,self.test_doc,self.label_doc = pre_data.vectorize()

    def train(self):
        print("----------train svm------------")
        from sklearn import svm
        lin_clf = svm.LinearSVC()
        lin_clf.fit(self.train_doc, self.label_doc)
        preds = lin_clf.predict(self.test_doc)
        return preds

    # def save_csv(self):
    #     print("__save_csv__")
    #     preds = self.train()
    #     save_data(preds,self.model_name)

    def validation(self):
        pass


class OneClassSvm(object):
    def __init__(self):
        self.model_name = "one_class_SVM"

    def train(self):
        pass


if __name__ == "__main__":
    xgb_ = XGBModel()
    xgb_.save_csv()
