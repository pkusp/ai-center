# encoding: utf-8
"""
@author: shipeng
@contact: peng_shi@shannonai.com

@version: 1.0
@file: tianchi_playground.py
@time: 2018/6/1 上午11:59

这一行开始写关于本文件的说明与解释
"""
import os
import sklearn
from sklearn import naive_bayes
from sklearn import svm
from sklearn import grid_search
from sklearn import linear_model
from sklearn import cross_validation
from sklearn import preprocessing

import pandas as pd
import numpy as np
from pandas import DataFrame
from experiments import config


# def ms_eda():
#     proj_path = config.PROJECT_PATH
#     cur_path = os.path.join(proj_path,'temp_experiments')
#     print(cur_path)
#     data = pd.read_csv(os.path.join(cur_path,'UserSegAmlDaily.ss.csv'))
#     # print(data.head())
#     # print(data.columns)
#     # print(data['InMarket'])
#     in_market = data['InMarket']
#     #
#     # for feat in data['InMarket']:
#     #     print(feat)
#     # onehot = preprocessing.OneHotEncoder()
#     # onehot.fit([[0,0,3],
#     #             [1,1,0],
#     #             [0,2,1]])
#     # results = onehot.transform([[0,1,3]]).toarray()
#     # print(results)
#     return in_market
#
# def alphabet_onehot():
#     from numpy import argmax
#     data = 'hello world'
#     alphabet = 'abcdefghijklmnopqrstuvwxyz '
#     char_to_int = dict((c,i) for i,c in enumerate(alphabet))
#     int_to_char = dict((i,c) for i,c in enumerate(alphabet))
#     print(char_to_int)
#     print(int_to_char)
#     int_encoded = [char_to_int[char] for char in data]
#     print(int_encoded)
#     onehot_encoded = list()
#     for val in int_encoded:
#         letter = [0 for _ in range(len(alphabet))]
#         print(letter)
#         letter[val] = 1
#         onehot_encoded.append(letter)
#     print(onehot_encoded)
#     # onehot转换为原特征值  argmax() 函数定位具有最大值的二进制向量中的索引，然后使用字符值的反向查找表中的整数进行整数。
#     inverted = int_to_char[argmax(onehot_encoded[1])]
#     print(argmax(onehot_encoded[1]))
#     print(inverted)
#
# def read_csv():
#     proj_path = config.PROJECT_PATH
#     cur_path = os.path.join(proj_path,'temp_experiments')
#     data = pd.read_csv(os.path.join(cur_path,'UserSegAmlDaily.ss.csv'))
#     return data
#
# def read_column(df,column_name)->list:
#     """
#
#     Args:
#         df:
#         column_name:
#
#     Returns: 这一列column组成的list，即所有数据的这个特征的值
#
#     """
#     column_val = df[column_name]
#     return column_val
#
# # im = ms_eda()
# # print(im[0])
# #
# #
# # for i in im[0].split(';'):
# #     print(i)
#
#
# def ms_feature_values(feature_list:list):
#     im_data = feature_list
#     feature_value = []
#     for i in range(len(im_data)):
#         # 每条数据的特征值append在一起
#         record = im_data[i]
#         feature_value.extend(record.split(';'))
#     #  去重
#     feature_value = list(set(feature_value))
#     print("all features in ImMarket:",feature_value)
#     return feature_value
#
#
# def feature_onehot(feature_values:list,data:list):
#     """
#
#     Args:
#         feature_values: 所有的特征值组成的list
#         data: 待转换为onehot的特征序列list
#
#     Returns: 将data的list转换为onehot形式的list
#
#     本函数每次转换一条数据的多个特征值为一个onehot向量
#
#     """
#     # 特征值和数字映射：
#     feat_to_int = dict((f,i) for i,f in enumerate(feature_values))
#     # int_to_feat = dict((i,f) for i,f in enumerate(feature_values))
#     # 特征值转化为数字编号：如[805685097,...] -> [3,...]
#     int_encoded = [feat_to_int[feat] for feat in data]
#
#     onehot_encoded = [0 for _ in range(len(feature_values))]
#     for val in int_encoded:
#         #  feature_values为特征字典, 有值得部分设置为1
#         onehot_encoded[val] = 1
#     return onehot_encoded
#
#
# def process_feature_onehot():
#     data = read_csv()
#     onehot_results = []
#     # col 为一列的所有特征值得list
#     for col in data.columns[-1]:
#         col_onehot = []
#         each_feature_list=read_column(data,col)
#         #  该列的所有特征值
#         feature_values = ms_feature_values(each_feature_list)
#         # record 为这一列的一条数据的特征list
#         for record in col:
#             # record_onehot 即每条转换好的onehot特征值
#             record_onehot=feature_onehot(feature_values,record)
#             col_onehot.append(record_onehot)
#         onehot_results.append(col_onehot)
#     return onehot_results
#

class MSOneHot(object):
    def __init__(self,input_file_name,output_name):
        self.file_name = input_file_name
        self.output_name = output_name
        self.proj_path = config.PROJECT_PATH
        self.file_path = os.path.join(self.proj_path,'temp_experiments')
        self.data_df = pd.read_csv(os.path.join(self.file_path,self.file_name))

    def fil_Nan(self,data,strategy=None):
        # 删除全部为none的列
        data = data.dropna(axis=1,how='all')
        if strategy == '0':
            data = data.fillna(0)
        elif strategy == '-1':
            data = data.fillna(-1)
        elif strategy =='max':
            data = data.fillna(data.max())
        elif strategy == 'mean':
            data = data.fillna(data.mean())
        else:
            data = data
        return data

    def read_column(self,df,column_name)->list:
        """

        Args:
            df:
            column_name:

        Returns: 这一列column组成的list，即所有数据的这个特征的值

        """
        column_val = df[column_name]
        return column_val

    def ms_feature_values(self,feature_list:list):
        im_data = feature_list
        feature_value = []
        print('____im data______',im_data)
        for i in range(len(im_data)):
            # 每条数据的特征值append在一起
            record = str(im_data[i])
            if record is None:
                print('____record__{}__None_____'.format(i))
                continue
            # print('______--record______',record)
            feature_value.extend(record.split(';'))
        #  去重
        feature_value = list(set(feature_value))
        print("all features in col:",feature_value)
        return feature_value

    def feature_onehot(self,feature_values:list,data:list):
        """

        Args:
            feature_values: 所有的特征值组成的list
            data: 待转换为onehot的特征序列list

        Returns: 将data的list转换为onehot形式的list

        本函数每次转换一条数据的多个特征值为一个onehot向量

        """
        # print('______data______',data)
        # print("feat::::---------",feature_values)
        # 特征值和数字映射：
        feat_to_int = dict((f,i) for i,f in enumerate(feature_values))
        # print('______dict______-',feat_to_int)
        # int_to_feat = dict((i,f) for i,f in enumerate(feature_values))
        # 特征值转化为数字编号：如[805685097,...] -> [3,...]
        int_encoded = [feat_to_int[feat] for feat in data]

        onehot_encoded = [0 for _ in range(len(feature_values))]
        for val in int_encoded:
            #  feature_values为特征字典, 有值得部分设置为1
            onehot_encoded[val] = 1
        return onehot_encoded

    def process_feature_onehot(self):
        data = self.fil_Nan(self.data_df,-1)
        column_list = ['InMarket', 'Remarketing', 'DMP']
        print(len(data['InMarket']))
        # 初始化数组
        onehot_results = np.zeros((len(data['InMarket']),1))
        print('____init___:',onehot_results)
        # col 为一列的所有特征值得list
        print(data.head())
        print(data.columns)
        # col 为待转为onehot的列
        for col in column_list:
        # for col in ['InMarket']:
            # print(data['InMarket'])
            print('_____________column:{}____________'.format(col))
            # print(data.columns)
            # print(data.head())

            col_value = data[col]
            col_onehot = []
            each_feature_list=self.read_column(data,col)
            #  该列的所有特征值
            feature_values = self.ms_feature_values(each_feature_list)
            # record 为这一列的一条数据的特征list
            for record in col_value:

                record_val_list = str(record).split(';')
                # record_onehot 即每条转换好的onehot特征值
                record_onehot=self.feature_onehot(feature_values,record_val_list)
                col_onehot.append(record_onehot)
                # print('___record onehot___',record_onehot)
            # print('______col  onehot_______',col_onehot)
            onehot_results = np.hstack((onehot_results,col_onehot))
        # 删除第一列(初始化时新增的列，全零)
        onehot_results = np.delete(onehot_results,0,axis=1)
        return onehot_results

    def save_csv(self):
        results = self.process_feature_onehot()
        for r in results:
            print("本条数据特征维数：",len(r))
        print('数据量：{}条'.format(len(results)))
        results_df = DataFrame(results)
        results_df.to_csv(os.path.join(self.file_path,self.output_name))

if __name__ == '__main__':
    input_filename = 'UserSegAmlDaily.ss.csv'
    output_name = 'onehot.csv'
    ms = MSOneHot(input_filename,output_name)
    ms.save_csv()












