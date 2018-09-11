# encoding: utf-8

def work_bfs(m, g):
    deep = [0]*m
    que = []
    for i in range(m):
        que.append(i)
        while (len(que)):
            front = que[0]
            del que[0]
            for j in range(m):
                if g[front][j]==1:
                    deep[j]=deep[i]+1
                    g[front][j]=0
                    que.append(j)
    max_deep = 0
    for d in deep:
        if d>max_deep:
            max_deep = d
    return max_deep


def main():
    line = str(input()).split(' ')
    print("line:::",line)
    m, n, k = int(line[0]), int(line[1]), int(line[2])
    g = [[0] * m] * m
    for i in range(k):
        edge = input()
        edge = edge.split(' ')
        # print("edge:", edge)
        row, col = int(edge[0]), int(edge[1])
        g[row][col] = 1

    res = work_bfs(m, g)
    print(res)

if __name__ == '__mian__':
    main()


