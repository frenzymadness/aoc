from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

here = Path(__file__).parent

with open(here / "input") as input:
    content = input.read()

score = 0

for line in content.splitlines():
    l = len(line)
    half = l // 2
    c1, c2 = set(line[:half]), set(line[half:])
    intersection = (c1 & c2).pop()
    if intersection in ascii_lowercase:
        score += ascii_lowercase.index(intersection) + 1
    elif intersection in ascii_uppercase:
        score += ascii_uppercase.index(intersection) + 1 + len(ascii_lowercase)

print(score)
