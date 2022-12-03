from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

here = Path(__file__).parent

with open(here / "input") as input:
    content = input.read()

score = 0
iterator = iter(content.splitlines())

for line in iterator:
    rucksacks = set(line), set(next(iterator)), set(next(iterator))
    intersection = rucksacks[0].intersection(*rucksacks[1:]).pop()
    if intersection in ascii_lowercase:
        score += ascii_lowercase.index(intersection) + 1
    elif intersection in ascii_uppercase:
        score += ascii_uppercase.index(intersection) + 1 + len(ascii_lowercase)

print(score)
