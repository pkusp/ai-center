# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: didi01.py
@time: 2018/9/18 下午7:40

这一行开始写关于本文件的说明与解释
"""


def ball(p,q,r):
    res=0
    total_nums=p+q+r
    state=[0]*(total_nums)

    for i in range(total_nums):

    return res


def main():
    line=input()
    line = list(map(int, line.split()))
    p,q,r=line[0],line[1],line[2]
    res = ball(p,q,r)
    print(res)


if __name__ == '__main__':
    main()
