from pathlib import Path
import re

here = Path(__file__).parent

pairs = 0

with open(here / "input") as input:
    for line in input:
        l1, u1, l2, u2 = re.match(r"(\d+)-(\d+),(\d+)-(\d+)", line.strip()).groups()
        elf1 = set(range(int(l1), int(u1) + 1))
        elf2 = set(range(int(l2), int(u2) + 1))

        if elf1.intersection(elf2):
            pairs += 1

print(pairs)
