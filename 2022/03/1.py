from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

alphabet = ascii_lowercase + ascii_uppercase

here = Path(__file__).parent

with open(here / "input") as input:
    content = input.read()

score = 0

for line in content.splitlines():
    l = len(line)
    half = l // 2
    c1, c2 = set(line[:half]), set(line[half:])
    intersection = (c1 & c2).pop()
    score += alphabet.index(intersection) + 1

print(score)
