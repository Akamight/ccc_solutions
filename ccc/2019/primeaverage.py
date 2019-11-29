import time

def primeuntil(n):
    primelist = [2]

    startnumber = 2

    while primelist[-1] < n:

        isPrime = True

        for i in primelist:

            if startnumber/i == startnumber//i:
                isPrime = False
                break

        if isPrime:
            primelist.append(startnumber)

        startnumber += 1

    return primelist

def solveForNumberStupid(number):
    primelist = primeuntil(number)

    for i in primelist:
        for p in primelist:
            if (i + p) / 2 == number:
                return i, p

arr = input()
arr = arr.split(" ")
for i in arr:
    print(solveForNumberStupid(int(i)))
