# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: train.py
@time: 2019/12/28 10:20 PM

这一行开始写关于本文件的说明与解释
"""
import torch
from torch.autograd import Variable
import torch.nn as nn
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np

# 一、数据准备

data_file = "./doc/21380.csv"
train_full = pd.read_csv(data_file)

#####
data = train_full


def label(column_name):
    label = np.zeros(len(data))
    label[0:len(data) - 1] = data[column_name][1:]
    print(label)
    data['{}Label'.format(column_name)] = label
    return


def feature_days_ago(days, column_name):
    feature_name = column_name + str(days) + 'Days'
    feature_lst = np.zeros(len(data))
    feature_lst[days: len(data)] = data[column_name][0: len(data) - days]
    print(label)
    data[feature_name] = feature_lst


for ele in ["Impressions", "Clicks", "Conversions", "RevenueUSD"]:
    label(ele)
    feature_days_ago(1, ele)
    feature_days_ago(7, ele)
    feature_days_ago(30, ele)
    # accumulate_monthly(ele)

data.to_csv('./doc/21380_cook.csv')


#####

impression = train_full["Impressions"]
datas = impression.values

print(len(datas))

# 归一化处理，这一步必不可少，不然后面训练数据误差会很大，模型没法用

max_value = np.max(datas)
min_value = np.min(datas)
scalar = max_value - min_value
datas = list(map(lambda x: x / scalar, datas))

print(datas)


# 数据集和目标值赋值，dataset为数据，look_back为输入特征维度

def creat_dataset(dataset, look_back):
    data_x = []
    data_y = []
    for i in range(len(dataset) - look_back):
        data_x.append(dataset[i:i + look_back])
        data_y.append(dataset[i + look_back])
    return np.asarray(data_x), np.asarray(data_y)  # 转为ndarray数据


# 以14为特征维度，得到数据集，即前14天预测后一天
dataX, dataY = creat_dataset(datas, 14)

train_size = int(len(dataX) * 0.7)

x_train = dataX[:train_size]  # 训练数据
y_train = dataY[:train_size]  # 训练数据目标值

x_train = x_train.reshape(-1, 1, 14)  # 将训练数据调整成pytorch中lstm的输入维度
y_train = y_train.reshape(-1, 1, 1)  # 将目标值调整成pytorch中lstm的输出维度

# 将ndarray数据转换为张量，因为pytorch用的数据类型是张量

x_train = torch.from_numpy(x_train)
y_train = torch.from_numpy(y_train)


# 二、创建LSTM模型


class RNN(nn.Module):
    def __init__(self):
        super(RNN, self).__init__()  # 面向对象中的继承
        self.lstm = nn.LSTM(14, 6, 2)  # 输入数据14个特征维度，6个隐藏层维度，2个LSTM串联，第二个LSTM接收第一个的计算结果
        self.out = nn.Linear(6, 1)  # 线性拟合，接收数据的维度为6，输出数据的维度为1

    def forward(self, x):
        x1, _ = self.lstm(x)
        a, b, c = x1.shape
        out = self.out(x1.view(-1, c))  # 因为线性层输入的是个二维数据，所以此处应该将lstm输出的三维数据x1调整成二维数据，最后的特征维度不能变
        out1 = out.view(a, b, -1)  # 因为是循环神经网络，最后的时候要把二维的out调整成三维数据，下一次循环使用
        return out1


rnn = RNN()

# 参数寻优，计算损失函数

optimizer = torch.optim.Adam(rnn.parameters(), lr=0.02)
loss_func = nn.MSELoss()

# 三、训练模型

for i in range(100):
    var_x = Variable(x_train).type(torch.FloatTensor)
    var_y = Variable(y_train).type(torch.FloatTensor)
    out = rnn(var_x)
    loss = loss_func(out, var_y)
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
    if (i + 1) % 10 == 0:
        print('Epoch:{}, Loss:{:.5f}'.format(i + 1, loss.item()))

# 四、模型测试

# 准备测试数据
x_test = dataX[train_size:]
y_test = dataY[train_size:]



dataX1 = x_test.reshape(-1, 1, 14)
dataX2 = torch.from_numpy(dataX1)
var_dataX = Variable(dataX2).type(torch.FloatTensor)

pred = rnn(var_dataX)

pred_test = pred.view(-1).data.numpy()  # 转换成一维的ndarray数据，这是预测值

# dataY为真实值

# 五、画图检验

plt.plot(pred.view(-1).data.numpy(), 'r', label='prediction')
plt.plot(y_test, 'b', label='real')
plt.legend(loc='best')

plt.ioff()
plt.show()