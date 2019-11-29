

import math

def explorePath(maxDays, K, a, score, solutionList = []):
    #print(maxDays, len(a))
    if maxDays == 0 and len(a) == 0:
        return score
    elif (maxDays == 0 and len(a) != 0) or maxDays * K < len(a):
        return 0



    startScore = score
    globalScore = score

    for i in range(1, min(K+1, len(a)) + 1):
        #print(score, a[0:i], a[i:])
        score += max(a[0:i])
        #b = explorePath(maxDays-1, K, a[i:], score)
        score = explorePath(maxDays-1, K, a[i:], score)
       # print(score, a[0:i], a[i:])
        globalScore = max(score, globalScore)
        score = startScore


    return globalScore

def Solution(N, K, a):
    maxDays = math.ceil(N/K)
    #print(maxDays)
    print(explorePath(maxDays, K, a, 0))

input1 = input().split(" ")
N, K = int(input1[0]), int(input1[1])
a = [int(i) for i in input().split(" ")]

Solution(N, K, a)