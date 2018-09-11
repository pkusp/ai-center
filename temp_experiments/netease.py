# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: netease.py
@time: 2018/9/8 下午4:21

这一行开始写关于本文件的说明与解释
"""

def max_min_living(n,k):
    mini = 0
    maxi = k-1
    if 2*k -1 <= n :
        return mini,maxi
    else:
        while(2*k-1>n):
            k-=1
            n-=1
        return mini, k-1

def main():
    t = int(input())
    res = []
    for i in range(t):
        line = input().strip().split(" ")
        line = list(map(int,line))
        ans = max_min_living(line[0],line[1])
        res.append(ans)
    for ele in res:
        print(ele[0],ele[1])

if __name__ == '__main__':
    main()