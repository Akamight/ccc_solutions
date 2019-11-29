
def locate(list1):
    coords0, coords1, coords2 = list1
    if coords0 == "X":
        return [int(coords1 - (coords2 - coords1)), coords1, coords2]
    elif coords1 == "X":
        return [coords0, int(coords0 + (coords2 - coords0)/2), coords2]
    elif coords2 == "X":
        return [coords0, coords1, int(coords1 + (coords1 - coords0))]
    else:
        return [coords0, coords1, coords2]

def outOfBounds(x, length):
    if x > length:
        return - (x - length)
    else:
        return x

def slicing(arr, dimension):
    #print(arr)
    return [i[dimension] for i in arr]

def invertSlicing(arr1, arr2, dimension):

    for i in range(len(arr1)):
        arr1[i][dimension] = arr2[i]

    return arr1

def hasX(board):
    for i in board:
        if "X" in i:
            return True
    return False

class Board():
    def __init__(self):
        self.left, self.middle, self.right = ["X", "X", "X"], [3, "X", "X"], [5, 7, 9]
        self.xList = []

        self.List = [self.left, self.middle, self.right]
        self.OriList = self.List
        self.locateX()
        #print(slicing(self.List, 0))
        self.solveX()

    def locateX(self):
        for i in range(len(self.left)):
            if self.left[i] == "X":
                self.xList.append([0, i])

            if self.middle[i] == "X":
                self.xList.append([1, i])

            if self.right[i] == "X":
                self.xList.append([2, i])

    def solveX(self):
        for i in range(9):
            for p in self.xList:
                if slicing(self.xList, 0).count(p[0]) == 1:
                    self.List[p[0]] = locate(self.List[p[0]])
                    self.xList.pop(self.xList.index(p))

            for p in self.xList:
                if slicing(self.xList, 1).count(p[1]) == 1:
                    self.List = invertSlicing(self.List, locate(slicing(self.List,p[1])),p[1])
                    self.xList.pop(self.xList.index(p))

        print(self.List)
        #
        #
        if hasX(self.List):
            for i in range(len(self.List)):
                for p in range(len(self.List[0])):
                    if self.List[i][p] != "X" and "X" in self.List[i]:
                        self.List[i] = [self.List[i][p], self.List[i][p], self.List[i][p]]

                        for i1 in self.xList:
                            if i1[0] == i:
                                self.xList.pop(self.xList.index(i1))
                        break
                else:
                    continue

                break
        else:
            return self.List
        self.solveX()





Board()