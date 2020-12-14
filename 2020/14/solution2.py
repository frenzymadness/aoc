import re
from collections import defaultdict


def apply_mask(binary, mask):
    result = ""
    for b, mb in zip(binary, mask):
        if mb == "0":
            result += b
        elif mb in ("1", "X"):
            result += mb
    return result


def expand_address(address): 
    count = address.count("X")
    # Generates binary numbers to get all
    # possible combinations of 0, 1 for a given length
    for x in range(2**count):
        result = address
        binary = bin(x)[2:].zfill(count)
        for i in range(count):
            result = result.replace("X", binary[i], 1)
        yield result


mem = defaultdict(int)
mask = ""

with open("input.txt") as input_file:
    inp = input_file.read()

for line in inp.splitlines():
    if line.startswith("mask"):
        mask = re.match(r"^mask = (\w+)$", line).groups()[0]
    elif line.startswith("mem"):
        addr, value = re.match(r"^mem\[(\d+)\] = (\d+)$", line).groups()
        addr = bin(int(addr))[2:].zfill(36)
        for addr in expand_address(apply_mask(addr, mask)):
            mem[int(addr, 2)] = value

print(sum(int(v) for v in mem.values()))
