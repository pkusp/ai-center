# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: algorithm_playground.py
@time: 2018/6/1 上午11:48

这一行开始写关于本文件的说明与解释
"""


def longest_increasing_subsequence(input_seq:list):
    pass


def climb_stairs(num:int):
    if num == 1:
        return 1
    elif num == 2:
        return 2
    else:
        stairs_num = [-1]*num
        stairs_num[0] = 1
        stairs_num[1] = 2
        for i in range(2,num):
            stairs_num[i] = stairs_num[i-1] + stairs_num[i-2]
        return stairs_num[num-1]


def longest_common_sequence(seq_1,seq_2):
    pass


def _2_1_1_remove_duplicates(input_nums:list):
    """
    Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
    Args:
        input_nums:

    Returns:

    """
    after_len = len(input_nums)
    for i in range(after_len-1,0,-1):
        if input_nums[i-1]==input_nums[i]:
            del input_nums[i]
            after_len-=after_len
    return






if __name__ == '__main__':
    print('hello eos')












































