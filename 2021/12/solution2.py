from collections import defaultdict, deque

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

g = defaultdict(set)

for line in lines:
    n1, n2 = line.split("-")
    g[n1].add(n2)
    g[n2].add(n1)

def walk(node, path, return_here):
    if node == "end":
        yield path
    
    for next_node in g[node]:
        if next_node not in path or next_node.isupper():
            yield from walk(next_node, path + [next_node], return_here)
        elif next_node.islower() and return_here and next_node not in ("start", "end"):
            yield from walk(next_node, path + [next_node], False)

print(sum(1 for _ in walk("start", ["start"], True)))
