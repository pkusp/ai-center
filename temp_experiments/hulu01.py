def sum_arr(a):
    if not a:
        return []
    res = []
    for ele in a:
        cur=0
        for less in a:
            if less<ele:
                cur+=less
        res.append(cur)
    return res

def sum_a(a):
    if not a:
        return []
    res = [0]*len(a)
    for i in range(len(a)):
        for j in range(i):
            if a[i]>a[j]:
                res[i]+=res[j]


    return res


def main():
    n = int(input())
    arr = []
    if n==0:
        print(0)
    else:
        for i in range(n):
            arr.append(int(input()))
    res = sum_a(arr)
    for r in res:
        print(r)


if __name__ == '__main__':
    main()

