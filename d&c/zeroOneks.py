class Items:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight


def zeroOneKs(items, capacity, currentindex):
    if capacity <= 0 or currentindex < 0 or currentindex >= (len(items)):
        return 0
    elif items[currentindex].weight <= capacity:
        profit1 = items[currentindex].profit + zeroOneKs(
            items, capacity - items[currentindex].weight, currentindex + 1
        )
        profit2 = zeroOneKs(items, capacity, currentindex + 1)
        return max(profit1, profit2)
    else:
        return 0


mango = Items(31, 3)
apple = Items(26, 1)
orange = Items(17, 2)
banana = Items(72, 5)

items = [mango, apple, orange, banana]
print(zeroOneKs(items, 7, 0))
