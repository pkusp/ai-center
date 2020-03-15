# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: rec_feat_gen.py
@time: 2020/1/1 9:59 PM

这一行开始写关于本文件的说明与解释
"""

from torch.utils.data import Dataset
import pickle as pkl
import torch
import pandas as pd
import numpy as np
from pandas import DataFrame as df


def raw_data_gen():
    # data_file = "./doc/Monetization_Campaign_Performance_99_20170101_20191130(1).csv"
    # df = pd.read_csv(data_file)
    # print(df.head())
    # impressions = df["Impressions"]
    # cust_id = df["CustomerId"]
    # account_id = ["AccountId"]
    # cost_1d = df["RevenueUSD"]
    #
    # impression_1 = impressions.drop([0])
    #
    # data_x = []
    # data_y = []
    test_train_data = {
        "cust_id":[1122321,1122321,1122321,1122321,1122321,1122321],
        "cust_seq1":[1,2,1,3,2,4],
        "cust_seq2": [ 2, 1, 3, 2, 4,3],
        "cust_seq3": [1, 3, 2, 4,3,5],
        "impression":[2,1,2,1,3,2],
        "account_id": [101, 101, 101, 101, 101, 101]

    }

    test_train_df = pd.DataFrame(data=test_train_data)
    print(test_train_df)
    print("test",test_train_df.iloc[1, 0])
    return test_train_df


class MovieRankDataset(Dataset):

    def __init__(self, drop_dup=False):

        # df = pd.read_csv(df_file)
        df = raw_data_gen()
        if drop_dup is True:
            df_cust_id = df.drop_duplicates(['cust_id'])
            df_impressions = df.drop_duplicates(['cust_seq'])
            self.dataFrame = pd.concat((df_cust_id, df_impressions), axis=0)
        else:
            self.dataFrame = df

    def __len__(self):
        return len(self.dataFrame)

    def __getitem__(self, idx):
        # movie data
        cust_id = self.dataFrame.iloc[idx, 0]
        cust_type = 1
        cust_seq1 = self.dataFrame.iloc[idx, 1]
        cust_seq2 = self.dataFrame.iloc[idx, 2]
        cust_seq3 = self.dataFrame.iloc[idx, 3]

        # target
        impression = torch.FloatTensor([self.dataFrame.iloc[idx, 4]])
        # user_inputs = {
        #     'uid': torch.LongTensor([uid]).view(1, -1),
        #     'gender': torch.LongTensor([gender]).view(1, -1),
        #     'age': torch.LongTensor([age]).view(1, -1),
        #     'job': torch.LongTensor([job]).view(1, -1)
        # }

        cust_inputs = {
            'cust_id': torch.LongTensor(cust_id).view(1, -1),
            'cust_type': torch.LongTensor(cust_type).view(1, -1),
            'cust_seq1': torch.LongTensor(cust_seq1).view(1, -1),
            'cust_seq2': torch.LongTensor(cust_seq2).view(1, -1),
            'cust_seq3': torch.LongTensor(cust_seq3).view(1, -1)
        }

        sample = {
            'user_inputs': "",
            'cust_inputs': cust_inputs,
            'target': impression
        }
        return sample
