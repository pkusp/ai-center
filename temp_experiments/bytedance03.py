import sys
def countWays(p, q, r, last):

    if (p < 0 or q < 0 or r < 0):
        return 0

    if (p == 1 and q == 0 and
            r == 0 and last == 0):
        return 1

    if (p == 0 and q == 1 and
            r == 0 and last == 1):
        return 1

    if (p == 0 and q == 0 and
            r == 1 and last == 2):
        return 1

    if (last == 0):
        return (countWays(p - 1, q, r, 1) +
                countWays(p - 1, q, r, 2))

    if (last == 1):
        return (countWays(p, q - 1, r, 0) +
                countWays(p, q - 1, r, 2))
    if (last == 2):
        return (countWays(p, q, r - 1, 0) +
                countWays(p, q, r - 1, 1))

def countUtil(p, q, r):

    return (countWays(p, q, r, 0) +
            countWays(p, q, r, 1) +
            countWays(p, q, r, 2))


if __name__ == '__main__':
    line = sys.stdin.readline()
    # line = list(map(int, line.split()))
    line = str(line).split()
    p,q,r=int(line[0]),int(line[1]),int(line[2])
    print(p,q,r)
    print(countUtil(p, q, r))

# This code is contributed by mits