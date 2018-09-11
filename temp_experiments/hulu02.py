# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: hulu02.py
@time: 2018/9/10 下午7:51

这一行开始写关于本文件的说明与解释
"""

def Triangle(data):
    n = len(data)
    res = 0
    i = 0
    while (i<n and data[i]<180):
        cnt = 0
        maxi = data[i]+180
        for j in range(i+1,n):
            if data[j]<maxi:
                cnt+=1
        res += int(cnt*(cnt-1)/2)
        i+=1
    while (i<n and data[i]>180):
        cnt = 0
        maxi = data[i]-180
        for j in range(i+1,n):
            if data[j]>maxi:
                cnt+=1
        res += int(cnt*(cnt-1)/2)
        i+=1
    return res

def main():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(int(int(input())/100))
    arr.sort()
    res = Triangle(arr)
    print(res)

if __name__ == '__main__':
    main()