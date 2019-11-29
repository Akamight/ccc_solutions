
input()
tides = [int(i) for i in input().split(" ")]

lowtides = []
hightides = []

first_low = tides[0]
for i in tides:
    if i > first_low:
        hightides.append(i)
    else:
        lowtides.append(i)
hightides.sort()
lowtides.sort(reverse=True)

for i, p in zip(lowtides,hightides):
    print(i,p,end=" ")
