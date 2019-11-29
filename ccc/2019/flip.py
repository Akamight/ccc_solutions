import numpy as np

def horzflip(grid):
    return grid[:, ::-1]

def vertflip(grid):
    return grid[::-1]

grid = np.array([[1,2], [3,4]])

arr = input()
for i in arr:
    print(i)
    if i == "H":
        grid = horzflip(grid)
    elif i == "V":
        grid = vertflip(grid)

print(grid)