input()

riceballs = [int(i) for i in input().split(" ")]

def checkAdjacent(riceballs):
    for i in range(len(riceballs) - 1):
        if riceballs[i] == riceballs[i + 1]:
            riceballs = riceballs[:i] + [(riceballs[i] + riceballs[i+1])]+ riceballs[i+2:]
            return riceballs, True
    else:
        return riceballs, False

def checkSpace(riceballs):
    for i in range(len(riceballs) - 2):
        if riceballs[i] == riceballs[i + 2]:
            riceballs = riceballs[:i] + [sum(riceballs[i:i+3])] + riceballs[i+3:]
            return riceballs, True
    else:
        return riceballs, False

def recursiveSolve(riceballs):

    riceballs, keep = checkSpace(riceballs)

    riceballsadj, keepadj = checkAdjacent(riceballs)

    print(riceballs, riceballsadj)
    if not keep and not keepadj:
        return max(max(riceballs), max(riceballsadj))
    elif keep:
        return max(recursiveSolve(riceballs), max(riceballsadj))
    elif keepadj:
        return max(recursiveSolve(riceballsadj), max(riceballs))
    else:
        return max(recursiveSolve(riceballsadj), recursiveSolve(riceballs))

keep = True

print(recursiveSolve(riceballs))

#print(checkAdjacent(riceballs))