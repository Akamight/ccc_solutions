
input()
swifts = input().split(" ")
semap = input().split(" ")

sumSwifts = 0
sumSemap = 0
index = 0
for i in range(len(swifts)):
    sumSwifts += int(swifts[i])
    sumSemap += int(semap[i])
    if sumSwifts == sumSemap:
        index = i

print(index + 1)
