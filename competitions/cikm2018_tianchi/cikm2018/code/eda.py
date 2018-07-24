#
# import numpy as np # linear algebra
# import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
# import os
# import gc
# import matplotlib.pyplot as plt
# import seaborn as sns
# # %matplotlib inline
#
# pal = sns.color_palette()
#
# print('# File sizes')
# for f in os.listdir('../input'):
#     if 'zip' not in f:
#         print(f.ljust(30) + str(round(os.path.getsize('../input/' + f) / 1000000, 2)) + 'MB')

from competitions import config
import os
print(config.PROJECT_PATH)


def vec_eda():
    vec = 'cikm2018_tianchi/data_raw/wiki.es.vec'
    vec_file = os.path.join(config.PROJECT_PATH,vec)
    print(vec_file)
    with open(vec_file,mode='r') as f:
        for i in range(1000):
            line = f.readline()
            print(line.split(' ')[0])


def train_eda():
    en_train = 'cikm2018_tianchi/data_raw/cikm_english_train_20180516.txt'
    es_train_file = os.path.join(config.PROJECT_PATH,en_train)
    with open(es_train_file,mode='r') as f:
        for i in range(10):
            line = f.readline()
            print(line)


if __name__ == '__main__':
    train_eda()


