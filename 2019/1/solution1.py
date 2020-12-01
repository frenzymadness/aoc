from math import floor

result = 0

with open("input.txt") as input_file:
    for line in input_file:
        mass = int(line)
        fuel = floor(mass / 3) - 2
        result += fuel
        print(f"Fuel needed for mass {mass} is {fuel}")

print(result)
