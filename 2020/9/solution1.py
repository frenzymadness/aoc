from itertools import combinations

with open("input.txt") as input_file:
    numbers = [int(n.strip()) for n in input_file.readlines()]

PREAMBLE = 25

for index, number in enumerate(numbers[PREAMBLE:], start=PREAMBLE):
    for combination in combinations(numbers[index-PREAMBLE:index], 2):
        if sum(combination) == number:
            break
    else:
        print(f"number {number} on index {index} is not valid")
        exit(0)
