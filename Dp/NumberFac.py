# Top-Down Approach


def numberFactor(n, tempDict):
    if n in (0, 1, 2):
        return 1
    if n == 3:
        return 2
    else:
        if n not in tempDict:
            subp1 = numberFactor(n - 1, tempDict)
            subp2 = numberFactor(n - 3, tempDict)
            subp3 = numberFactor(n - 4, tempDict)
            tempDict[n] = subp1 + subp2 + subp3

        return tempDict[n]


# Time Complexity: O(3^n)
print(numberFactor(7, {}))

# Bottom-up Approach


def numberFactorBU(n):
    temp = [1, 1, 1, 2]
    for i in range(4, n + 1):
        temp.append(temp[i - 1] + temp[i - 3] + temp[i - 4])
    return temp[n]


print(numberFactorBU(7))

# Time Complexity: O(n)
