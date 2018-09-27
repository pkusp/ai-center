# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: 360.py
@time: 2018/9/17 下午8:14

这一行开始写关于本文件的说明与解释
"""


#
# def crabstick(nums):
#     state_sum=[0]*len(nums)
#     state_max=[0]*len(nums)
#     tmp_max=nums[0]
#     tmp_sum=nums[0]
#     state_sum[0]=tmp_sum
#     state_max[0] = tmp_max
#     for i in range(1,len(nums)):
#         if nums[i]>tmp_max:
#             tmp_max=nums[i]
#         tmp_sum+=nums[i]
#
#         state_sum[i]=tmp_sum
#         state_max[i]=tmp_max
#     print("max:",state_max)
#     print("sum:",state_sum)
#     for j in range(len(nums)):
#         if state_sum[j]-state_max[j]>state_max[j]:
#             return j+1
#     return -1
#

#
#
# def main():
#     n=input()
#     line=input()
#     line = list(map(int, line.split()))
#     res = crabstick(line)
#     print(res)
#
# if __name__ == '__main__':
#     main()

def bittts(nums):
    k, l, r = nums[0], nums[1], nums[2]
    range_k = k
    while range_k < r:
        range_k = range_k * k
    range_k = range_k / k
    if range_k <= l:
        range_limit = r - range_k + 1
        tmp_k = k
        while tmp_k < range_limit:
            tmp_k = tmp_k * k
        range_k = range_k + 1 + tmp_k / k

    return range_k - 1


def main():
    res_lst = []
    n = int(input())
    for i in range(n):
        line = input()
        line = list(map(int, line.split()))
        res = bittts(line)
        res_lst.append(res)

    for r in res_lst:
        print(r)


if __name__ == '__main__':
    main()
