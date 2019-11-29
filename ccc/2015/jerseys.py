
n = int(input())
a = int(input())

arr = []
for i in range(n):
    arr.append(input())

arr2 = []

for i in range(a):
    arr2.append(input().split(" "))

counter = 0
for i in arr2:
    if arr[int(i[1]) - 1] == i[0]:
        counter += 1

print(counter)