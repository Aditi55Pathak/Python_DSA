def insertionSort(customList):
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j + 1] = customList[j]
            j -= 1
        customList[j + 1] = key
    print(customList)


list = [-2, 5, 1, 7, 8, 3]
insertionSort(list)

# Time Complexity ---> O(n^2)

# When to use insertion sort :-
# when we have insufficient memory
# easy to implement
# When we have continous inflow of number and we want to keep them sorted

# When not to use insertion sort :-
# when time is a concern
