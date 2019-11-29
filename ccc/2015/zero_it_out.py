number = int(input())

arr = []
last_num = 0
for i in range(number):
    num = int(input())
    if num != 0:
        arr.append(num)
    else:
        arr.pop(-1)
print(sum(arr))
