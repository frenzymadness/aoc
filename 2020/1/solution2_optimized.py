from itertools import combinations
from functools import reduce
from operator import mul

with open("input1.txt") as input_file:
    numbers = [int(line.strip()) for line in input_file.readlines()]

for combination in combinations(numbers, 3):
    if sum(combination) == 2020:
        result = reduce(mul, combination)
        print(f"Sum of {combination} == {sum(combination)} so {combination} multiplied == {result}")
