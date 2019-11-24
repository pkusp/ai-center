# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: lstm.py
@time: 2018/6/16 下午8:03

这一行开始写关于本文件的说明与解释
"""
import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn.metrics import mean_absolute_error, mean_squared_error
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
#% matplotlib inline
import warnings

warnings.filterwarnings('ignore')


class LSTMModel(object):
    def __init__(self):
        self.class_name = self.__class__.__name__
        self.description = 'construct LSTM'

    def __repr__(self):
        return self.class_name


class NetConf(object):
    def __init__(self):
        self.class_name = self.__class__.__name__
        self.description = 'train LSTM'
        self.rnn_hidden_unit = 10
        self.input_size = 4
        self.outpuy_size = 1
        self.learning_rate = 0.0006
        #  input output weights:
        self.weights = {
            'in':tf.Variable(tf.random_normal([self.input_size,self.rnn_hidden_unit])),
            'out':tf.Variable(tf.random_normal([self.rnn_hidden_unit,1])),
        }
        #  input output biases:
        self.biases = {
            'in':tf.Variable(tf.constant(0.1,shape=[self.rnn_hidden_unit,])),
            'out':tf.Variable(tf.constant(0.1,shape=[1,])),
        }
        # init weights:
        tf.reset_default_graph()


class LSTMTrain(object):
    def __init__(self):
        self.class_name = self.__class__.__name__
        self.ref_url_1 = 'https://blog.csdn.net/Flying_sfeng/article/details/78852816'
        self.data_style = "pd.read_csv(path,names=['年','月','日','当日最高气温','当日最低气温','当日平均气温','当日平均湿度','输出'])  "
        self.net_conf = NetConf()

    def __repr__(self):
        return self.class_name

    def data_process(self):
        pass

    def get_data(self,batch_size=60,time_step=20,train_begin=0,train_end=500):
        # 分割数据集，将数据分为训练集和验证集(最后90天做验证，其他做训练)
        pass

    def lstm(self,x):
        batch_size = tf.shape(x)[0]
        time_step = tf.shape(x)[1]
        w_in = self.net_conf.weights['in']
        b_in = self.net_conf.biases['in']
        # 将tensor转成2维进行计算，计算后的结果作为隐藏层的输入
        in_put = tf.reshape(x,[-1,self.net_conf.input_size])
        input_rnn = tf.matmul(in_put,w_in) + b_in
        # 将tensor转成3维，作为lstm cell的输入
        in_put = tf.reshape(input_rnn,[-1,time_step,self.net_conf.rnn_hidden_unit])

        cell = tf.contrib.rnn.BasicLSTMCell(self.net_conf.rnn_hidden_unit)
        # cell=tf.contrib.rnn.core_rnn_cell.BasicLSTMCell(rnn_unit)
        init_state = cell.zero_state(batch_size,dtype=tf.float32)

        # output_rnn是记录lstm每个输出节点的结果，final_states是最后一个cell的结果
        output_rnn, final_states = tf.nn.dynamic_rnn(cell,input_rnn,initial_state=init_state,dtype=tf.float32)
        # output =
        output = tf.reshape(output_rnn, [-1, self.net_conf.rnn_hidden_unit])  # 作为输出层的输入
        w_out = self.net_conf.weights['out']
        b_out = self.net_conf.biases['out']
        pred = tf.matmul(output, w_out) + b_out
        return pred, final_states

    def train_lstm(self):
        pass
