# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: feature_gen.py
@time: 2020/1/1 8:57 PM

这一行开始写关于本文件的说明与解释
"""
import torch
from torch.autograd import Variable
import torch.nn as nn
import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plt
import numpy as np


data_file = "./doc/Monetization_Campaign_Performance_99_20170101_20191130(1).csv"

raw_data = pd.read_csv(data_file)

print(raw_data.head())











