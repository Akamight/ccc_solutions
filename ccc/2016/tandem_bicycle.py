question_type = int(input())

n = int(input())

dimojistan = [int(i) for i in input().split(" ")]
pegland = [int(i) for i in input().split(" ")]

if question_type == 1:
    dimojistan.sort()
    pegland.sort()
else:
    dimojistan.sort(reverse=True)
    pegland.sort()

total_speed = sum([max(i,p) for i,p in zip(dimojistan,pegland)])

print(total_speed)