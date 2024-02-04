def selectionSort(customList):
    for i in range(len(customList)):
        minindex = i
        for j in range(i + 1, len(customList)):
            if customList[minindex] > customList[j]:
                minindex = j
        customList[i], customList[minindex] = customList[minindex], customList[i]
    print(customList)


list = [2, 5, 1, 7, 8, 3]
selectionSort(list)

# Time Complexity ---> O(n^2)

# When to use selection sort :-
# when we have insufficient memory
# easy to implement

# When not to use selection sort :-
# when time is a concern
