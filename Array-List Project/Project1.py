# Calculate average of temperature.

user = int(input("How many days temperature you want? : "))
temperatures = []

for i in range(1, user + 1):
    temperature = int(input(f"Temperature of Day {i} : "))
    temperatures.append(temperature)

print("Temperatures for each day:", temperatures)


def average(temp):
    return sum(temp) / len(temp)


avg = print(f"Average of {user} days :- ", average(temperatures))
