from pathlib import Path

here = Path(__file__).parent

with open(here / "input") as file:
    lines = file.readlines()
    instructions = len(lines) * 2

def signal_strength(x, cycle):
    if cycle in range(20, instructions, 40):
        signal_strength = cycle * x
        return signal_strength
    return 0


x = 1
cycle = 0
signal_sum = 0

for i, line in enumerate(lines):
    if line.startswith("noop"):
        cycle += 1
        signal_sum += signal_strength(x, cycle)
    elif line.startswith("addx"):
        num = int(line.strip().split()[1])
        cycle += 1
        signal_sum += signal_strength(x, cycle)
        cycle += 1
        signal_sum += signal_strength(x, cycle)
        x += num

print(signal_sum)
