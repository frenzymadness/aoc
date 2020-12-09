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
        invalid_number = number
        invalid_number_index = index
        break


for start_index in range(invalid_number_index):
    for end_index in range(start_index, invalid_number_index):
        part = numbers[start_index:end_index]
        if sum(part) == invalid_number:
            print("Found: ", min(part) + max(part))
            exit(0)
        elif sum(part) > invalid_number:
            break
