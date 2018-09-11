//# encoding: utf-8
//"""
//@author: pkusp
//@contact: pkusp@outlook.com
//
//@version: 1.0
//@file: hulu03.py
//@time: 2018/9/10 下午8:06
//
//这一行开始写关于本文件的说明与解释
"""

//
//def dfs(i,m,g,n,days):
//    if n==0:
//        days+=1
//        return days
//    for j in range(m):
//        if g[i][j] == 1:
//            break
//    for j in range(m):
//        if g[i][j] == 1:
//            g[i][j]=0
//            dfs(j,m,g,n-1,days)
//    days += 1
//    return days
//
//int dfs(int i,int m,const vector<vector<int>> &g,int n,int days){
//    if(n==0) return ++days;
//    for(int j=0;j<m;++j){
//        if(g[i][j]==1) break;
//    }
//    for(int j=0;j<m;++j){
//        if(g[i][j]==1){
//            g[i][j]=0;
//            days = dfs(j,m,g,n-1,days);
//        }
//    return days;
//    }
//
//
//}
//
//


def work_bfs(m,n,g):
    res = 0
    deep = [0]*len(m)
    que = []
    for i in range(m):
        for j in range(m):
            if g[i][j]==1:
                que.append()




def main():
    line = str(input()).split(' ')
    m,n,k = int(line[0]),int(line[1]),int(line[2])
    g = [[0]*m]*m
    for i in range(k):
        edge = input().split(' ')
        print("edge:",edge)
        row,col = int(edge[0]),int(edge[1])
        g[row][col]=1

    res = work_arrange(m,n,g)
    print(res)







