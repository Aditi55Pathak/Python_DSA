def findMinOperation(s1, s2, index1, index2, tempDict):
    if index1 == len(s1):
        return len(s2) - index2
    if index2 == len(s2):
        return len(s1) - index1
    if s1[index1] == s2[index2]:
        return findMinOperation(s1, s2, index1 + 1, index2 + 1, tempDict) 
    else:
        dictkey = str(index1) + str(index2)
        if dictkey not in tempDict:
            deleteOp = 1 + findMinOperation(s1, s2, index1, index2 + 1, tempDict)
            insertOp = 1 + findMinOperation(s1, s2, index1 + 1, index2, tempDict)
            replaceOp = 1 + findMinOperation(s1, s2, index1 + 1, index2 + 1, tempDict)
            tempDict[dictkey] = min(deleteOp, insertOp, replaceOp)
        return tempDict[dictkey]

print(findMinOperation("table", "tbrltt", 0, 0, {}))
