# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: neteasehuyu02.py
@time: 2018/9/16 下午7:31

这一行开始写关于本文件的说明与解释
"""
import sys

dp = [0] * 1001
w=[0]*1001

def back_pack_dp(sum, n):
    if (n<1 or sum<0 or w[0]>sum):
        return
    dp[0]=1
    for i in range(n+1):
        for j in range(sum+1,-1,-1):
            if j>=w[j]:
                dp[j]=dp[j]+dp[j-w[i]]
    return dp[sum]


if __name__ == "__main__":
    # 读取第一行的n
    line1 = sys.stdin.readline().strip()
    line1 = list(map(int, line1.split()))
    n, m = line1[0], line1[1]
    line2 = sys.stdin.readline().strip()
    values = list(map(int, line2.split()))
    for i in values:
        w.append(i)
    res = back_pack_dp(m, n)
    print('\n',res)
