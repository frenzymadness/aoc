from collections import defaultdict
from pathlib import Path

here = Path(__file__).parent

with open(here / "input") as input:
    content = input.read()

structure = defaultdict(list)
stack = []

for i, line in enumerate(content.splitlines()):
    if line.startswith("$ cd"):
        dir = line.split()[-1]
        if dir == "..":
            stack.pop()
        else:
            stack.append(dir)
    elif line.startswith("$ ls"):
        pass
    elif line.startswith("dir"):
        name = line.split()[-1]
        structure["/".join(stack)].append(name)
    else:
        size, name = line.split()
        structure["/".join(stack)].append((int(size), name))

def calculate_size(dir, structure):
    size = 0
    for x in structure[dir]:
        if isinstance(x, tuple):
            size += x[0]
        else:
            size += calculate_size("/".join((dir, x)), structure)
    return size

result = 0

for dir in structure.keys():
    size = calculate_size(dir, structure)
    if size <= 100000:
        result += size

print(result)
