# import sys
#
#
#
#
#
# def str_label(lines):
#     res = []
#     pos = 0
#     for i in range(len(lines)-1):
#
#         for j in range(100):
#             if lines[i][j] != lines[i+1][j]:
#                 res.append(line[i][:j+1])
#                 pos = j
#                 break
#     res.append(lines[])
#
#
#     return res
#
# if __name__ == "__main__":
#     # 读取第一行的n
#     n = int(sys.stdin.readline().strip())
#     ans = 0
#     lines = []
#     for i in range(n):
#         # 读取每一行
#         line = sys.stdin.readline().strip()
#         lines.append(line)
#     res = str_label(lines)
#     for r in res:
#         print(r)

class Solution(object):
    def Prefix(self, tinput):
        if not tinput:
            return []
        n = len(tinput)
        res = []
        for outer in range(n):
            s = tinput[outer]
            tag = ""
            for i in range(len(s)):
                tag += s[i]
                if self.kernel(tag, outer, n, tinput):
                    continue
                else:
                    res.append(tag)
                    break
        return res

    def kernel(self, tag, i, n, tinput):
        for j in range(n):
            if j != i:
                if tinput[j].startswith(tag):
                    return True
                else:
                    continue
            else:
                continue
        return False


def main():
    n = int(input().strip())
    tinput = []
    for i in range(n):
        line = str(input().strip())
        tinput.append(line)
    s = Solution()
    res = s.Prefix(tinput)
    for ele in res:
        print(ele)


if __name__ == "__main__":
    main()