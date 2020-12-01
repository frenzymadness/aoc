from itertools import combinations

with open("input.txt") as input_file:
    codes = [l.strip() for l in input_file.readlines()]

for c1, c2 in combinations(codes, 2):
    diff = 0
    result = ""
    for a, b in zip(c1, c2):
        if a != b:
            diff += 1
        else:
            result += a
    if diff == 1:
        print("Only one diff between", c1, "and", c2, result)

        break
