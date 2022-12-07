from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

alphabet = ascii_lowercase + ascii_uppercase

here = Path(__file__).parent

with open(here / "input") as input:
    content = input.read()

score = 0
iterator = iter(content.splitlines())

for line in iterator:
    rucksacks = set(line), set(next(iterator)), set(next(iterator))
    intersection = rucksacks[0].intersection(*rucksacks[1:]).pop()
    score += alphabet.index(intersection) + 1

print(score)
