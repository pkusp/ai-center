# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: rec_model.py
@time: 2020/1/1 9:29 PM

这一行开始写关于本文件的说明与解释
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim


# --------------- hyper-parameters------------------
lstm_param = {
    "input_dim": 3,
    "hidden_dim_cell_out_dim": 6,
    "feature_out_dim": 1,
    "cell_num": 2
}

cust_max_dict = {
    'cust_id': 2000,  # 2000 custs
    'cust_type': 1
}

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")

class rec_model(nn.Module):

    def __init__(self, embed_dim=32, fc_size=200):
        '''
        Args:
            cust_max_dict: the max value of each cust attribute. {'cust_id': xx, 'cust_type': xx}
            lstm_param: lstm params.
            fc_sizes: fully connect layer sizes. normally 2
        '''

        super(rec_model, self).__init__()
        # --------------------------------- cust channel ---------------------------------------------------------
        #  ---------------- cust id embeddings
        self.embedding_cust_id = nn.Embedding(cust_max_dict['cust_id'], embed_dim)  # normally 32
        self.embedding_cust_type = nn.EmbeddingBag(cust_max_dict['cust_type'], embed_dim, mode='sum')

        self.fc_cust_id = nn.Linear(embed_dim, embed_dim)
        self.fc_cust_type = nn.Linear(embed_dim, embed_dim)

        # ---------------- cust lstm part
        # 输入数据14个特征维度，6个隐藏层维度，2个LSTM串联，第二个LSTM接收第一个的计算结果
        self.lstm_cell = nn.LSTM(lstm_param['input_dim'], lstm_param['hidden_dim_cell_out_dim'], lstm_param['cell_num'])

        # 线性拟合，接收数据的维度为6，输出数据的维度为1
        self.lstm_out = nn.Linear(lstm_param['hidden_dim_cell_out_dim'], lstm_param['feature_out_dim'])

        # cust channel concat
        self.fc_cust_combine = nn.Linear(embed_dim * 2 + lstm_param['feature_out_dim'], fc_size)  # tanh

        # BatchNorm layer
        self.BN = nn.BatchNorm2d(1)
        # --------------------------------- other channel --------------------------------------------------------
        # TODO: ADD OTHER channel FEATURE

    def forward(self, cust_input):
        # # pack train_data
        cust_id = cust_input['cust_id']
        cust_type = cust_input['cust_type']
        cust_seq1 = cust_input['cust_seq1']
        cust_seq2 = cust_input['cust_seq2']
        cust_seq3 = cust_input['cust_seq3']
        print("cust_seq1 shape:\n",cust_seq1.shape)
        print("cust_seq2 shape:\n",cust_seq2.shape)
        print("cust_seq3 shape:\n",cust_seq3.shape)

        cust_seq = torch.cat((cust_seq1,cust_seq2,cust_seq3),1)
        print("cust_seq shape:\n",cust_seq.shape)
        if torch.cuda.is_available():
            cust_id, cust_type, cust_seq = cust_id.to(device), cust_type.to(device), cust_seq.to(device)

        # cust channel
        feature_cust_id = self.BN(F.relu(self.fc_cust_id(self.embedding_cust_id(cust_id))))
        feature_cust_type = self.BN(F.relu(self.fc_cust_type(self.embedding_cust_type(cust_type)).view(-1, 1, 1, 32)))

        feature_cust_seq = self.BN(F.relu(self.lstm_out(self.lstm_cell(cust_seq))))

        # feature_cust
        feature_cust = F.tanh(self.fc_cust_combine(
            torch.cat([feature_cust_id.view(-1, 1, 32), feature_cust_type.view(-1, 1, 32), feature_cust_seq], 2)
        ))

        output = torch.sum(feature_cust, 2)  # B x rank
        return output, feature_cust
