from pathlib import Path
from collections import deque, defaultdict

here = Path(__file__).parent

with open(here / "input") as input:
    content = input.read()

stacks_txt, instructions_txt = content.split("\n\n")
stacks = defaultdict(deque)

for line in stacks_txt.splitlines():
    i = 0
    while True:
        try:
            if line[i] == "[":
                stacks[(i // 4) + 1].appendleft(line[i+1])
            i += 4
        except IndexError:
            break

for line in instructions_txt.splitlines():
    count, from_stack, to_stack = map(int, re.match(r"move (\d+) from (\d+) to (\d+)", line).groups())
    for _ in range(count):
        stacks[to_stack].append(stacks[from_stack].pop())

result = ""
for key in sorted(stacks.keys()):
    result += stacks[key][-1]

print(result)
