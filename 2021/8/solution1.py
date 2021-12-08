with open("input.txt") as input_file:
    lens = []
    for line in input_file:
        signals, digits = line.split(" | ")
        digits = digits.split()
        lens.extend([len(d) for d in digits])

print(sum((lens.count(7), lens.count(3), lens.count(4), lens.count(2))))
