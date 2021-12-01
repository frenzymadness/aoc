with open("input.txt") as input_file:
    lines = input_file.readlines()

counter = 0
for n in range(1, len(lines)):
    if int(lines[n]) > int(lines[n-1]):
        counter += 1
print(counter)
