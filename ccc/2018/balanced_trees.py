n = 1000

def counttrees(n):
    numtrees = 0
   # print(n)
    for i in range(2, n+1):
        print(n%i)
        if n % i < i:
            subtrees = 0
            if n // i > 1:
                subtrees += counttrees(n//i)
                print(subtrees)
            else:
                subtrees += 1
            numtrees += subtrees
    return numtrees

print(counttrees(n))