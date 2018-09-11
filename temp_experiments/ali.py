# encoding: utf-8
"""
@author: pkusp
@contact: pkusp@outlook.com

@version: 1.0
@file: ali.py
@time: 2018/9/7 下午7:51

这一行开始写关于本文件的说明与解释
"""
'''
输入范例:
singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪
请播放周杰伦的七里香给我听
输出范例:
请播放 周杰伦/actor,singer 的 七里香/song 给我听
'''
# import re
# from collections import defaultdict
#
#
# def extracted_answer(s1, s2):
#     enty_lst = s1.split(';')
#     enty_mp = {}
#     name_mp = defaultdict(list)
#     name_lst = []
#     res_s = s2
#     for enty in enty_lst:
#         k = enty.split('_')[0]
#         v = enty.split('_')[1]
#         enty_mp[k] = v.split('|')
#     for k, v in enty_mp.items():
#         for val in v:
#             name_mp[val].append(k)
#             name_lst.append(val)
#     name_lst = sorted(name_lst, key=lambda x: len(x), reverse=True)
#     pattern = '|'.join(name_lst)
#     pattern = re.compile(pattern)
#     res_lst = re.findall(pattern, s2)
#     for n in res_lst:
#         start = res_s.find(n)
#         end = start + len(n)
#         print(start, start + len(n) - 1)
#         tag = ','.join(name_mp[n])
#         res_s = res_s[:start] + ' ' + res_s[start:end] + '/' + tag + ' ' + res_s[end:]
#         print(res_s)
#
#     # print(res_lst)
#
#
# if __name__ == '__main__':
#     s = 'singer_周杰|周杰伦|刘德华|王力宏;song_冰雨|北京欢迎你|七里香;actor_周杰伦|孙俪'
#     s2 = '请播放周杰伦的七里香给我听'
#     extracted_answer(s, s2)
#     # s1 = '<[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>'
#     # s2 = '来几首@{singer}的流行歌曲'
#     # res = match_pattern(s1,s2)
#     # print(res)
#
#

'''
输入范例:
<[播]放|来>[一|几]<首|曲|个>@{singer}的<歌[曲]|[流行]音乐>
来几首@{singer}的流行歌曲
输出范例:
0
'''


# def match_pattern(s1: str, s2: str):
#     s1 = s1.replace('<', '(?:')
#     s1 = s1.replace('>', ')')
#     s1 = s1.replace('@{singer}', '\w+?')
#     res = re.findall(s1, s2)
#     if len(res) == 0:
#         return 0
#     else:
#         return 1

def find_max_length(tinput):
    if not tinput:
        return 0
    res = 0
    color = tinput[0]
    cur = 1
    for i in range(1, len(tinput)):
        if color == tinput[i]:
            cur += 1
        else:
            cur = 1
        if cur > res:
            res = cur
        color = tinput[i]
    return res


def find_max_len(s):
    if not s:
        return 0
    res = 0
    res_tmp = 1
    lst = list(s)
    clr = lst[0]
    for i in range(1,len(lst)):
        if lst[i] == clr:
            res_tmp = 1
        else:
            clr = lst[i]
            res_tmp+=1
            if res_tmp>res:
                res = res_tmp
    return res


def main():
    tinput = str(input())
    res = find_max_length(tinput)
    print(res)


if __name__ == '__main__':
    main()

    """
    def turn(tinput):
        colour = tinput[0]
        for i in range(1,len(tinput)):
            if tinput[i] == colour:
                continue
            else:
                break
            last = i -1
            t1 = tinput[:last+1]
            t1 = t1[::-1]
            out = t1+t3
            return output


    def find_max_length(tinput):
        if not tinput:
            return 0
        if len(tinput) == 1:
            return 1
        if len(tinput) == 2:
            if tinput[0] == tinput[1]:
                return 2
            else:
                return 1
        if(tinput[0] == tinput[-1]):
            tinput = turn(tinput)
        res = 0
        color = tinput[0]
        cur = 1
        for i in range(1,len(tinput)):
            if color == tinput[i]:
                cur += 1
            else:
                cur = 1
            if cur > res:
                res = cur
            color = tinput[i]
        return res


    def main():
        tinput = str(input())
        res = find_max_length(tinput)
        print(res)

    if __name__ == '__main__':
        main()
    """
