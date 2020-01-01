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



data = train_full
def label(column_name):
    label = np.zeros(len(data))
    label[0:len(data)-1] = data[column_name][1:]
    print(label)
    data['{}Label'.format(column_name)] = label
    return

def feature_days_ago(days, column_name):
    feature_name = column_name + str(days) + 'Days'
    feature_lst = np.zeros(len(data))
    feature_lst[days : len(data)] = data[column_name][0 : len(data) - days]
    print(label)
    data[feature_name] = feature_lst

for ele in ["Impressions", "Clicks", "Conversions", "RevenueUSD"]:
    label(ele)
    feature_days_ago(1, ele)
    feature_days_ago(7, ele)
    feature_days_ago(30, ele)
    # accumulate_monthly(ele)

data.to_csv(r'D:\Feature\21380_cook.csv')