from itertools import combinations

with open("input1.txt") as input_file:
    numbers = [int(line.strip()) for line in input_file.readlines()]

for x, y in combinations(numbers, 2):
    if x + y == 2020:
        print(f"{x} + {y} == {x + y} so {x} × {y} == {x * y}")
