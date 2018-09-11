# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: bytedance.py
@time: 2018/9/9 上午10:14

这一行开始写关于本文件的说明与解释
"""

import copy


def max_sub_str(s):
    if not s:
        return 0
    if len(s)==1:
        return 1
    sub_mp = set()
    tmp_mp =set()
    for c in s:
        # print(c)
        if c not in tmp_mp:
            tmp_mp = tmp_mp+ {c}
            # print('not in:',c)
        else:
            if len(tmp_mp) > len(sub_mp):
                # print('len max:')
                sub_mp = copy.deepcopy(tmp_mp)
                # print(sub_mp)
            tmp_mp.clear()
            # print(sub_mp)
            tmp_mp+={c}
    return len(sub_mp)


def main():
    s = input()
    res = max_sub_str(s)
    print(res)


if __name__ == '__main__':
    import time
    t1=time.time()
    main()
    t2 = time.time()
    print(t2-t1)