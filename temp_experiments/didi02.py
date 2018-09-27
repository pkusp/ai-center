class Solution(object):
    def FindWord(self, word_list, matrix):
        numr = len(matrix)
        numc = len(matrix[0])
        visited = list()
        res = []
        for word in word_list:
            cur = word[0]
            for i in range(numr):
                for j in range(numc):
                    if matrix[i][j] == cur:
                        visited.append([i,j])
                        if self.FindNextWordInMatrix(visited, matrix, word[1:], i, j):
                            res.append(word)
                        else:
                            visited.remove([i,j])
                            continue
        return res


    def FindNextWordInMatrix(self, visited, matrix, word, i, j):
        if not word:
            return True
        numr = len(matrix)
        numc = len(matrix[0])
        directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        curchar = word[0]
        for direc in directions:
            if i + direc[0] >= 0 and i + direc[0] <= numr - 1 and j + direc[1] >= 0 and j + direc[1] <= numc - 1:
                if matrix[i + direc[0]][j + direc[1]] == curchar:
                    visited.append([i + direc[0], j + direc[1]])
                    flag = self.FindNextWordInMatrix(visited, matrix, word[1:], i + direc[0], j + direc[1])
                    if flag:
                        return True
                    else:
                        visited.remove([i + direc[0], j + direc[1]])
            else:
                continue
        return False

def main():
    num_list = input().strip().split()
    # m = int(num_list[0])
    n = int(num_list[1])
    # k = int(num_list[2])
    word_list = input().strip().split()
    matrix = []
    for i in range(n):
        row = input().strip().split()
        matrix.append(row)
    s = Solution()
    result = s.FindWord(word_list, matrix)
    for answer in result:
        print(answer)

if __name__ == "__main__":
    main()