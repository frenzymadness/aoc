from int_comp import IntComputer
from itertools import permutations

results = []

for permutation in permutations(range(5), 5):
    input = 0
    for phase in permutation:
        computer = IntComputer("input", [input, phase])
        input = computer.run()
    results.append(input)

print("Max is", max(results))
