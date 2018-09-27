import sys
class Solution(object):
    def Inversion(self, tinput):
        min_count = sys.maxsize
        index = 0
        for i in range(len(tinput)):
            temp = tinput[i]
            tinput[i] = 0
            _, count = self.InversionNum(tinput)
            if count < min_count:
                index = i + 1
                min_count = count
            tinput[i] = temp
        return min_count, index

    def InversionNum(self, lst):
        if len(lst) == 1:
            return lst, 0
        else:
            n = len(lst) // 2
            lst1, count1 = self.InversionNum(lst[0:n])
            lst2, count2 = self.InversionNum(lst[n:len(lst)])
            lst, count = self.Count(lst1, lst2, 0)
            return lst, count1 + count2 + count

    def Count(self, lst1, lst2, count):
        i = 0
        j = 0
        res = []
        while i < len(lst1) and j < len(lst2):
            if lst1[i] <= lst2[j]:
                res.append(lst1[i])
                i += 1
            else:
                res.append(lst2[j])
                count += len(lst1) - i
                j += 1
        res += lst1[i:]
        res += lst2[j:]
        return res, count

def main():
    n = input().strip().split()
    tinput = input().strip().split()
    tinput = [int(ele) for ele in tinput]
    s = Solution()
    count, index = s.Inversion(tinput)
    print(count, index)

if __name__ == "__main__":
    main()