from itertools import combinations

with open("input1.txt") as input_file:
    numbers = [int(line.strip()) for line in input_file.readlines()]

for x, y, z in combinations(numbers, 3):
    if x + y + z == 2020:
        print(f"{x} + {y} + {z} == {x + y + z} so {x} × {y} × {z} == {x * y * z}")
