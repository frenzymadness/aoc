import networkx as nx
from networkx.algorithms.shortest_paths import shortest_path

with open("input.txt") as input_file:
    lines = input_file.readlines()

g = nx.DiGraph()

for line in lines:
    if ")" not in line:
        continue
    t, f = line.strip().split(")")
    g.add_edge(f, t)

orbits = 0

for node in g.nodes:
    if node == "COM":
        continue
    path = shortest_path(g, node, "COM")
    orbits += len(path)-1

print(orbits)