# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: onehot_process.py
@time: 2018/6/26 下午5:39

这一行开始写关于本文件的说明与解释
"""

import os

import numpy as np
import pandas as pd
from pandas import DataFrame


class OneHot(object):
    """
    input_file_name：输入的文件名.csv 在当前脚本的目录
    output_name：输出文件名.csv 将会以改名字保存csv，在当前目录
    返回处理好的one-hot形式的csv文件,但标题暂时没有加上

    """
    def __init__(self, input_file_name, output_name):
        self.file_name = input_file_name
        self.output_name = output_name
        self.proj_path = os.path.dirname(os.path.abspath(__file__))
        print('___path___',self.proj_path)
        self.file_path = self.proj_path
        self.data_df = pd.read_csv(os.path.join(self.file_path, self.file_name))

    def fil_Nan(self, data, strategy=None):
        # 删除全部为none的列
        data = data.dropna(axis=1, how='all')
        if strategy == '0':
            data = data.fillna(0)
        elif strategy == '-1':
            data = data.fillna(-1)
        elif strategy == 'max':
            data = data.fillna(data.max())
        elif strategy == 'mean':
            data = data.fillna(data.mean())
        else:
            data = data
        return data

    def read_column(self, df, column_name) -> list:
        """

        Args:
            df:
            column_name:

        Returns: 这一列column组成的list，即所有数据的这个特征的值

        """
        column_val = df[column_name]
        return column_val

    def ms_feature_values(self, feature_list: list):
        im_data = feature_list
        feature_value = []
        for i in range(len(im_data)):
            # 每条数据的特征值append在一起
            record = str(im_data[i])
            if record is None:
                print('____record__{}__None_____'.format(i))
                continue
            feature_value.extend(record.split(';'))
        #  去重
        feature_value = list(set(feature_value))
        print("all features in col:", feature_value)
        return feature_value

    def feature_onehot(self, feature_values: list, data: list):
        """

        Args:
            feature_values: 所有的特征值组成的list
            data: 待转换为onehot的特征序列list

        Returns: 将data的list转换为onehot形式的list

        本函数每次转换一条数据的多个特征值为一个onehot向量

        """
        # 特征值和数字映射：
        feat_to_int = dict((f, i) for i, f in enumerate(feature_values))
        # 特征值转化为数字编号：如[805685097,...] -> [3,...]
        int_encoded = [feat_to_int[feat] for feat in data]
        onehot_encoded = [0 for _ in range(len(feature_values))]
        for val in int_encoded:
            #  feature_values为特征字典, 有值得部分设置为1
            onehot_encoded[val] = 1
        return onehot_encoded

    def process_feature_onehot(self):
        data = self.fil_Nan(self.data_df, -1)
        process_column_list = ['InMarket', 'Remarketing', 'DMP']  # TODO: 这里是待转为one-hot的列
        save_column_list = list(set(data.columns)-set(process_column_list))
        # 初始化数组
        onehot_results = np.zeros((len(data['InMarket']), 1))
        # col 为待转为onehot的列
        for col in process_column_list:
            col_value = data[col]
            col_onehot = []
            each_feature_list = self.read_column(data, col)
            #  该列的所有特征值
            feature_values = self.ms_feature_values(each_feature_list)
            # record 为这一列的一条数据的特征list
            for record in col_value:
                record_val_list = str(record).split(';')
                # record_onehot 即每条转换好的onehot特征值
                record_onehot = self.feature_onehot(feature_values, record_val_list)
                col_onehot.append(record_onehot)
            onehot_results = np.hstack((onehot_results, col_onehot))
        # 删除第一列(初始化时新增的列，全零)
        onehot_results = np.delete(onehot_results, 0, axis=1)
        onehot_results = np.hstack((np.array(data[save_column_list]),onehot_results))
        return onehot_results

    def save_csv(self):
        results = self.process_feature_onehot()
        for r in results:
            print("本条数据特征维数：", len(r))
        print('数据量：{}条'.format(len(results)))
        results_df = DataFrame(results)
        results_df.to_csv(os.path.join(self.file_path, self.output_name))


if __name__ == '__main__':
    input_filename = 'UserSegAmlDaily.ss.csv'
    output_name = 'onehot.csv'
    ms = OneHot(input_filename, output_name)
    ms.save_csv()
