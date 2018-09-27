# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: aqiyi.py
@time: 2018/9/15 上午11:50

这一行开始写关于本文件的说明与解释
"""

def noodles(n,lines):
    lines=sorted(lines,key=lambda x:x[0])
    i=1
    res=1
    tmp=lines[1]
    while i < len(lines):
        while(lines[i][0]<tmp[1] and i<len(lines)):
            i+=1
        if i<len(lines):
            res+=1
    return res



def main():
    n=int(input())
    lines=[]
    for i in range(n):
        line=str(input()).split()
        line=sorted(line)
        lines.append(line)
    res=noodles(n,lines)
    print(res)

if __name__ =='__main__':
    main()