import random

list_here = ["London", "Paris", "New York", "India", "UAE"]

new_dict = {city: random.randint(20, 30) for city in list_here}
print(new_dict)

above_25 = {city: temp for (city, temp) in new_dict.items() if temp < 25}
print(above_25)
