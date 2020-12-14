import re
from collections import defaultdict


def apply_mask(binary, mask):
    result = ""
    for b, mb in zip(binary, mask):
        if mb in ("0", "1"):
            result += mb
        elif mb == "X":
            result += b
    return result


mem = defaultdict(int)
mask = ""

with open("input.txt") as input_file:
    inp = input_file.read()

for line in inp.splitlines():
    if line.startswith("mask"):
        mask = re.match(r"^mask = (\w+)$", line).groups()[0]
    elif line.startswith("mem"):
        addr, value = re.match(r"^mem\[(\d+)\] = (\d+)$", line).groups()
        binary = bin(int(value))[2:].zfill(36)
        mem[addr] = apply_mask(binary, mask)

print(sum(int(v, 2) for v in mem.values()))
