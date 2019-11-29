village_list = []

for i in range(int(input())):
    village_list.append(int(input()))

village_list.sort(reverse=False)

distance = village_list[-1] - village_list[0]
for i in range(1, len(village_list) - 1):
    distance = min(distance, abs(village_list[i] - (village_list[i] + village_list[i - 1]) / 2) + abs(village_list[i] - (
                village_list[i + 1] + village_list[i]) / 2))

print(distance)
