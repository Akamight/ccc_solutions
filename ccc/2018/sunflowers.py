
def rot90(arr):
    arr1 = []
    for i in reversed(range(len(arr))):
        arr2 = []
        for p in range(len(arr)):
            arr2.append(arr[p][i])
        arr1.append(arr2)
    return arr1

def checkSmallFlower(arr):
    for i in range(1, len(arr)):
        if not (arr[i][0] >= arr[i-1][0]):
            return False

    return True

def checkConsistency(arr):
    for i in arr:
        for p in range(1, len(i)):
            if not i[p] >= i[p-1]:
                return False
    return True

arr = [[3,7,9],[2,5,6],[1,3,4]]

while not (checkConsistency(arr) and checkSmallFlower(arr)):
    arr = rot90(arr)

    print(arr)