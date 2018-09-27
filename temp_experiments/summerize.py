# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: summerize.py
@time: 2018/9/21 下午4:05

这一行开始写关于本文件的说明与解释
"""


def coins_min(price, coins):
    state = [0] * (price + 1)
    for i in range(price + 1):
        for j in range(i):
            if i - j in coins:
                state[i] = state[j] + 1
                break
    res = state[price]

    return res


if __name__ == '__main__':
    coinss = [1, 3, 5]
    for prices in range(1000):
        ress = coins_min(prices, coinss)
        print(ress)
