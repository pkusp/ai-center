# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: eda.py
@time: 2019/12/28 10:21 PM

这一行开始写关于本文件的说明与解释
"""
import numpy as np
import pandas as pd


data_file = "./doc/21380.csv"


def get_train():
    train_full = pd.read_csv(data_file)
    print(train_full.head())

    print(train_full.count())

    impression = train_full["Impressions"]

    impression = impression.T
    # aa_row = pd.concat([a1,a2], axis = 1) #将两个DataFrame连接在一起（横向），如果axis=0则是（纵向）连接在一起
    impression = np.array(impression)

    print(impression)

    train = []

    for i in range(len(impression)-15):
        train.append(impression[i:i+15])

    train = pd.DataFrame(train)
    print(train.head())
    return train

