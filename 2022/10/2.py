from pathlib import Path

here = Path(__file__).parent

with open(here / "input") as file:
    lines = file.readlines()
    instructions = len(lines) * 2

def pixel(cycle, x):
    col = cycle % 40
    if col in (x-1, x, x+1):
        return "#"
    return "."

x = 1
cycle = 0
crt = [[] for x in range(6)]

for i, line in enumerate(lines):
    if cycle % 40 == 0:
        crt.append([])
    #print("before", cycle, crt, x)
    if line.startswith("noop"):
        p = pixel(cycle, x)
        crt[cycle // 40].append(p)
        cycle += 1
    elif line.startswith("addx"):
        num = int(line.strip().split()[1])
        p = pixel(cycle, x)
        crt[cycle // 40].append(p)
        cycle += 1
        p = pixel(cycle, x)
        crt[cycle // 40].append(p)
        cycle += 1
        x += num

    #print("after", cycle, crt, x)

for row in crt:
    print("".join(row))
