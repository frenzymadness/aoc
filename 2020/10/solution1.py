from collections import Counter

with open("input.txt") as input_file:
    adapters = [int(n.strip()) for n in input_file.readlines()]

builtin = max(adapters) + 3
adapters = [0] + sorted(adapters) + [builtin]
diffs = []

for index, adapter in enumerate(adapters):
    try:
        diff = adapters[index+1] - adapter
        diffs.append(diff)
    except IndexError:
        break

c = Counter(diffs)
print(c, "result", c[1] * c[3])
