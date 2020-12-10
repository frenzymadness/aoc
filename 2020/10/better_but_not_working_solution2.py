from networkx import DiGraph
from networkx.algorithms.simple_paths import all_simple_paths                        

with open("input.txt") as input_file:
# with open("test_input.txt") as input_file:
# with open("test_input2.txt") as input_file:
    adapters = [int(n.strip()) for n in input_file.readlines()]

builtin = max(adapters) + 3
adapters = [0] + sorted(adapters) + [builtin]

g = DiGraph()

for index, adapter in enumerate(adapters): 
    for next in adapters[index+1:index+4]:
        try: 
            if next - adapter <= 3: 
                g.add_edge(adapter, next)
            else: 
                break 
        except IndexError: 
            break

sum = 0
for _ in all_simple_paths(g, min(adapters), max(adapters)):
    sum += 1

print(sum)
