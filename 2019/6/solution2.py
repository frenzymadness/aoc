import networkx as nx
from networkx.algorithms.shortest_paths import shortest_path

with open("input.txt") as input_file:
    lines = input_file.readlines()

g = nx.Graph()

for line in lines:
    if ")" not in line:
        continue
    t, f = line.strip().split(")")
    g.add_edge(f, t)

orbits = 0

path = shortest_path(g, "YOU", "SAN")
steps = len(path)-3

print(path)
print(steps)