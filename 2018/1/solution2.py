from itertools import cycle

with open("input.txt") as input_file:
    lines = input_file.readlines()

results = [0]
for line in cycle(lines):
    x = results[-1] + int(line.strip())
    print(x)
    if x in results:
        print("we have", x, "again")
        break
    else:
        results.append(x)
        
print(len(results))
