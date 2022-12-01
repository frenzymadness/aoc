from pathlib import Path

here = Path(__file__).parent

inp = Path(here / "input").read_text()
elves = inp.split("\n\n")

sums = []

for elf in elves:
    elf_sum = sum(map(int, elf.strip().split("\n")))
    sums.append(elf_sum)

print(sum(sorted(sums, reverse=True)[:3]))
