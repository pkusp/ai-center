# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: sensetime.py
@time: 2018/10/15 下午8:29

这一行开始写关于本文件的说明与解释
"""
import sys
import numpy as np
from numpy import random


def Distance(x):
    def Dis(y):
        return np.sqrt(sum((x - y) ** 2))  # 欧式距离
    return Dis


def init_k_means(k):
    k_means = {}
    for i in range(k):
        k_means[i] = []
    return k_means


def cal_seed(k_mean):
    k_mean = np.array(k_mean)
    new_seed = np.mean(k_mean, axis=0)
    return new_seed


def K_means(data, seed_k, k_means):
    for i in data:
        f = Distance(i)
        dis = list(map(f, seed_k))
        index = dis.index(min(dis))
        k_means[index].append(i)

    new_seed = []
    for i in range(len(seed_k)):
        new_seed.append(cal_seed(k_means[i]))
    new_seed = np.array(new_seed)
    return k_means, new_seed


def run_K_means(data, k):
    seed_k =data[random.randint(len(data), size=k)]
    k_means = init_k_means(k)
    result = K_means(data, seed_k, k_means)
    count = 0
    # while not (result[1] == seed_k).all():
    count += 1
    seed_k = result[1]
    k_means = init_k_means(k=2)
    result = K_means(data, seed_k, k_means)
    for i in range(k):
        mydata = np.array(result[0][i])
    return result[0]


if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    pos = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        values = list(map(int, line.split()))
        values = np.array(values)
        pos.append(values)
    pos = np.array(pos)
    res = run_K_means(pos, k=2)
    mp={}
    for k,v in res.items():
        for val in list(v):
            key=(val[0],val[1])
            mp[key]=k
    cnt=0
    sizen=len(pos)
    for p in pos:
        kk=(p[0],p[1])
        if(kk==1):
            cnt+=1
            if(cnt>sizen*0.3):
                print(0)
        print(mp[kk])






