# Recursive Approach


def openrussiandoll(doll):
    if doll == 1:
        print("All dolls done")
    else:
        openrussiandoll(doll - 1)


openrussiandoll(10)

# itrative Approach


def firstmethod():
    secondmethod()
    print("I am the first method")


def secondmethod():
    thirdmethod()
    print("I am the second method")


def thirdmethod():
    forthmethod()
    print("I am the third method")


def forthmethod():
    print("I am the forth method")


firstmethod()
