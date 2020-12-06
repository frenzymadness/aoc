with open("input.txt") as input_file:
    groups = input_file.read().split("\n\n")

count = 0
for group in groups:
    count += len(set(group.replace("\n", "")))

print(count)
