import re
from collections import Counter

pairs = {}

with open("input.txt") as input_file:
    template = next(input_file).strip()
    next(input_file)
    for line in input_file:
        match = re.match(r"(\w{2}) -> (\w)", line)
        k, v = match.groups()
        pairs[k] = v

for step in range(10):
    print(step)
    new_template = ""
    for i in range(len(template)):
        new_template += template[i]
        if template[i:i+2] in pairs:
             new_template += pairs[template[i:i+2]]

    template = new_template

most_common = Counter(template).most_common()
most, least = most_common[0][1], most_common[-1][1]
print(most - least)
