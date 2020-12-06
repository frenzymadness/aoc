with open("input.txt") as input_file:
    groups = input_file.read().split("\n\n")

count = 0
for group in groups:
    people = [set(g) for g in group.split("\n") if len(g) > 0]
    intersection = people[0].intersection(*people[1:])
    count += len(intersection)

print(count)
