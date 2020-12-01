from math import floor

result = 0
with open("input.txt") as input_file:
    for line in input_file:
        fuel = int(line)
        while True:
            fuel = floor(fuel / 3) - 2
            if fuel <= 0:
                break
            result += fuel

print(result)
