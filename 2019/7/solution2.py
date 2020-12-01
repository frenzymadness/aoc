from int_comp import IntComputer
from itertools import permutations
from itertools import cycle

results = []

for permutation in permutations(range(5, 10), 5):
    print(permutation)
    input = 0
    computers = {}
    for phase in cycle(permutation):
        if phase not in computers:
            print("new computer")
            computers[phase] = IntComputer("input", [input, phase])
            input = computers[phase].run()
        else:
            computers[phase].input = [input]
            input = computers[phase].run()
        print("computer phase", phase, "returned", input)
        if phase == permutation[-1]:
            if input is None:
                print("FINAL")
                break
            else:
                results.append(input)
print("Max is", max(results))
