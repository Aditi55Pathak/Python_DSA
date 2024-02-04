def bubbleSort(list):
    for i in range(len(list) - 1):
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
        print(
            "After pass", i + 1, ":", list, "Number of iterations in the  pass:", j + 1
        )
    print("Number of passes:", i + 1, "Number of iterations in the last pass:", j + 1)


list = [2, 5, 1, 7, 8, 3]
bubbleSort(list)

# Time Complexity ---> O(n^2)
# When to use bubble sort :-

# when Input is already sorted
# When Space is concern
# Easy to Implement

# When not to use bubble sort :-

# Average time complexity is poor
