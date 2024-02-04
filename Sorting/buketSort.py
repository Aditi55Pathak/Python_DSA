import math


def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    return customList


def bucketSort(customList):
    numberofbuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for i in range(numberofbuckets):
        arr.append([])
    for j in customList:
        index_b = math.ceil(j * numberofbuckets / maxValue)
        arr[index_b - 1].append(j)

    for i in range(numberofbuckets):
        arr[i] = insertionSort(
            arr[i]
        )  # we used here insertion sort which have O(n^2), which is large if we use merge sort it will take O(log(n))

    k = 0

    for i in range(numberofbuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


list = [2, 5, 1, 7, 8, 3]
print(bucketSort(list))

# Time Complexity ---> O(n^2)

# When to use bukket sort :-
# When input is uniformaly distributed over range

# When not to use bukket sort :-
# when space is a concern
