import sys


def path_rear(s):
    pos = 0
    # while s[-1] == '/':
    #     s = s[:-1]
    for i in range(len(s)):
        if s[-i] != '/':
            s=s[:-i+1]
            break
    for i in range(1,len(s)):
        if s[-i]=='/':
            pos = -i
            break
    return s[pos:]


def main():
    line = sys.stdin.readline().strip()

    res = path_rear(line)
    print(res)


if __name__ == '__main__':
    main()