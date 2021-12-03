from collections import Counter

with open("input.txt") as input_file:
    lines = input_file.readlines()

copy_of_lines = list(lines)

for index in range(len(lines[0])):
    if len(lines) == 1:
        ox = int(lines[0], 2)
        break
    counter = Counter([s[index] for s in lines])
    if counter["1"] == counter["0"]:
        most_common = "1"
    else:
        most_common = counter.most_common()[0][0]
    lines = [l for l in lines if l[index] == most_common]

lines = list(copy_of_lines)

for index in range(len(lines[0])):
    if len(lines) == 1:
        co2 = int(lines[0], 2)
        break
    counter = Counter([s[index] for s in lines])
    if counter["1"] == counter["0"]:
        most_common = "0"
    else:
        most_common = counter.most_common()[-1][0]
    lines = [l for l in lines if l[index] == most_common]

print(ox * co2)