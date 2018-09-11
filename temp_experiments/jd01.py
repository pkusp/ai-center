#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def solve(s, t):
    if not s or not t:
        return 0
    if len(t)==1:
        return len(s)
    sub_cnt = 0
    mp = {}
    pm ={}
    for i in range(len(s) - len(t)+1):
        for j in range(len(t)):
            if s[i + j] not in mp:
                if j == len(t)-1:
                    if s[i+j] not in mp and t[j] not in pm:
                        sub_cnt+=1
                    mp={}
                    pm={}
                    break
                mp[s[i + j]] = t[j]
                pm[t[j]]= s[i+j]
            else:
                if t[j] == mp[s[i + j]]:
                    if j==len(t)-1:
                        sub_cnt += 1
                        mp={}
                        pm={}

                else:
                    mp={}
                    break

    return sub_cnt


# ******************************结束写代码******************************


try:
    _S = input()
except:
    _S = None

try:
    _T = input()
except:
    _T = None

res = solve(_S, _T)

print(str(res) + "\n")