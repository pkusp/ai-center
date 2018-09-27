# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: bytedance05.py
@time: 2018/9/9 上午11:42

求抖音红人数量
"""

import sys


def judge_lucky(num):
        num = str(num)
        level = len(num)
        for i in range(level//2):
            # print(nums[i],nums[level-1-i])
            if num[i] == num[level-i-1]:
                return False,i==level//2,i
        return True,0,0


def lucky_number(a,b):
    count = 0
    # for i in range(b,a-1,-1):
    while(a<=b):
        is_lucky, pos_judge,pos = judge_lucky(b)
        if is_lucky:
            count += 1
            if pos_judge:
                break
            if pos:
                valve = b//pow(10,pos)
                b=valve
        b-=1

    return count


def main():
    line = sys.stdin.readline().strip()
    line = list(map(int, line.split()))
    # print("line:",line)
    res = lucky_number(line[0],line[1])
    print(res)

if __name__ == '__main__':
    main()