# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: sina.py
@time: 2018/9/15 下午10:00

这一行开始写关于本文件的说明与解释
"""


def LCS(s1,s2):
    m=len(s1)
    n=len(s2)
    res=0
    if m==0 or n==0:
        return 0
    state=[[0]*m]*n
    for i in range(m):
        for j in range(n):
            if s1[i]==s2[j]:
                # if (i!=0 and j!=0):
                    state[i][j]=state[i-1][j-1]+1
                # else:
                #     state[i][j]=1
            else:
                # if (i!=0 and j!=0):
                    state[i][j]=max(state[i-1][j],state[i][j-1])
                # else:
                #     state[i][j]=0
    # for i in range(m):
    #     for j in range(n):
    #         if state[i][j]>res:
    #             res=state[i][j]
    return res

def main():
    s1=input()
    s2=input()
    res = LCS(s1,s2)
    print(res)

if __name__=='__main__':
    main()