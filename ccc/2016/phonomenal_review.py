def slice_lists(list1, dimension):
    return [i[dimension] for i in list1]


def explore_path(start_point, arr_paths, left_restaurants, distance, max_distance):
    if len(left_restaurants) == 0:
        return 0

    elif distance > max_distance:
        return 10000

    distances = []

    total_distance = 0
    for p in range(len(arr_paths)):
        i = arr_paths[p]
        distance2 = []
        if i[0] == start_point:
            if i[1] in left_restaurants:
                # print(left_restaurants[i+1:],left_restaurants[:i])
                distance1 = explore_path(i[1], arr_paths,
                                         left_restaurants[left_restaurants.index(i[1]) + 1:] + left_restaurants[
                                                                                               :left_restaurants.index(
                                                                                                   i[1])], distance + 1,
                                         max_distance) + 1
            else:
                distance1 = explore_path(i[1], arr_paths, left_restaurants, distance + 1, max_distance) + 1

        elif i[1] == start_point:
            if i[0] in left_restaurants:
                # print(left_restaurants[i + 1:], left_restaurants[:i])
                distance1 = explore_path(i[0], arr_paths,
                                         left_restaurants[left_restaurants.index(i[0]) + 1:] + left_restaurants[
                                                                                               :left_restaurants.index(
                                                                                                   i[0])], distance + 1,
                                         max_distance) + 1
            else:
                distance1 = explore_path(i[0], arr_paths, left_restaurants, distance + 1, max_distance) + 1

        else:
            continue

        distances.append(min(distance2) if len(distance2) > 0 else 0 + distance1)

        max_distance = min(min(distances), max_distance)
    # print(distances)
    return min(distances)


n, m = [int(i) for i in input().split(" ")]

arr_m = [int(i) for i in input().split(" ")]

arr_paths = []
for i in range(n - 1):
    arr_paths.append([int(i) for i in input().split(" ")])

distances = []
best_solution = n
for i in range(len(arr_m)):
    print(arr_m[i + 1:] + arr_m[:i])
    distances.append(explore_path(arr_m[i], arr_paths, arr_m[i + 1:] + arr_m[:i], 0, best_solution))
    best_solution = min(min(distances), best_solution)

print(distances)

# print(arr_m[i+1:] + arr_m[:i])
# if distance != 0:
#     print(distance)
