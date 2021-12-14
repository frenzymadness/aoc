import re
from collections import Counter, defaultdict

pairs = {}

with open("input.txt") as input_file:
    template = next(input_file).strip()
    next(input_file)
    for line in input_file:
        match = re.match(r"(\w{2}) -> (\w)", line)
        k, v = match.groups()
        pairs[k] = v

counts = defaultdict(int)

for i in range(len(template)-1):
    counts[template[i:i+2]] += 1

for step in range(40):
    new_counts = defaultdict(int)
    for pair, count in counts.items():
        first, second = pair
        new_counts[first+pairs[pair]] += count
        new_counts[pairs[pair]+second] += count

    counts = new_counts

letter_counts = Counter()

for (first, second), count in counts.items():
    letter_counts[first] += count
    letter_counts[second] += count

letter_counts[template[0]] += 1
letter_counts[template[-1]] += 1

for letter, count in letter_counts.most_common():
    letter_counts[letter] = count//2

print(sum(c//2 for c in letter_counts.values()))

most_common = letter_counts.most_common()
most, least = most_common[0][1], most_common[-1][1]
print(most - least)
