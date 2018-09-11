# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: bytedance02.py
@time: 2018/9/9 上午10:34

这一行开始写关于本文件的说明与解释
"""


def bfs_matrix(m: list):
    res = 0
    state = [[0]*len(m)]*len(m)
    for i in range(len(m)-1):
        for j in range(len(m)-1):
            if m[i][j]==0 or state[i][j]==1:
                continue
            bfs(m,state,i,j)
            res += 1
    # for k in range(len(m)):
    #     last =len(m)-1
    #     if m[last][i]==1 and m[last-1][i]==0 and m[last][i-1]==0 and m[last][i+1]==0:
    #         res +=1
    #     elif m[last][i]==1 and m[last-1][i]==0 and m[last][i+1]==0:
    #         res +=1
    # for k in range(len(m)):
    #     last =len(m)-1
    #     if m[i][last]==1 and m[i][last-1]==0 and m[i-1][last]==0 and m[i+1][last]==0:
    #         res +=1
    #     elif m[i][last]==1 and m[i][last-1]==0 and m[i+1][last]==0:
    #         res +=1
    #
    return res

def bfs(m,state,i,j):
    q = []
    q.append((i,j))
    while len(q)>0 and i<len(m) and j<len(m):
        node = q[0]
        # print('node:',node)
        # print(node[0],node[1])
        state[node[0]][node[1]]=1
        del q[0]
        if m[node[0]+1][node[1]] == 1:
            q.append((node[0]+1,node[1]))
        if m[node[0]][node[1]+1] == 1:
            q.append((node[0],node[1]+1))

def main():
    num = int(input())
    # print("num:",num)
    mat=[]
    for i in range(num):
        line = input().split(' ')
        # for i in range(num):
        #     line.append(input())
        mat.append(line)
    res = bfs_matrix(mat)
    print(res)

if __name__ =='__main__':
    main()

