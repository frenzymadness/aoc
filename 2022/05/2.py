import re
from pathlib import Path
from collections import defaultdict

here = Path(__file__).parent

with open(here / "input") as input:
    content = input.read()

stacks_txt, instructions_txt = content.split("\n\n")
stacks = defaultdict(list)

for line in stacks_txt.splitlines():
    for i, match in enumerate(re.finditer(r"(    |\[.\] ?)", line)):
        group = match.group()
        if group.startswith("["):
            stacks[i+1].insert(0, group[1])

for line in instructions_txt.splitlines():
    count, from_stack, to_stack = map(int, re.match(r"move (\d+) from (\d+) to (\d+)", line).groups())
    stacks[to_stack].extend(stacks[from_stack][-count:])
    del stacks[from_stack][-count:]

result = ""
for key in sorted(stacks.keys()):
    result += stacks[key][-1]

print(result)
