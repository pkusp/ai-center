import math

def least_round(s1,s2):
    ssum= 2*(s1+s2)
    index=0
    for i in range(int(math.sqrt(ssum))+1):
        if i *(i+1) ==ssum:
            index=i
            break
    if index*(index+1) !=ssum:
        return -1
    round = 1
    ss1=s1
    while(ss1>i):
        ss1=ss1-1
        i-=1
        round+=1
    return round

def main():
    score = (input().strip().split())
    s1 = int(score[0])
    s2 = int(score[1])
    res=least_round(s1,s2)
    print(res)


if __name__ =='__main__':
    main()