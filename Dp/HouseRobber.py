# Top Down Approach


def houseRobber(houses, currentIndex, tempdict):
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in tempdict:
            stealFirstHouse = houses[currentIndex] + houseRobber(
                houses, currentIndex + 2, tempdict
            )
            skipFirstHouse = houseRobber(houses, currentIndex + 1, tempdict)
            tempdict[currentIndex] = max(stealFirstHouse, skipFirstHouse)
        return tempdict[currentIndex]


houses = [6, 7, 1, 30, 8, 2, 4]
print(houseRobber(houses, 0, {}))

# TC: O(2^n)


# Bottom up


def houseRobberBU(houses, currentIndex):
    temparr = [0] * (len(houses) + 2)
    for i in range(len(houses) - 1, -1, -1):
        temparr[i] = max(houses[i] + temparr[i + 2], temparr[i + 1])
    return temparr[0]


print(houseRobberBU(houses, 0))
