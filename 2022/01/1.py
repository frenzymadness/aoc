from pathlib import Path

here = Path(__file__).parent

inp = Path(here / "input").read_text()
elves = inp.split("\n\n")

maximum = 0

for elf in elves:
    elf_sum = sum(map(int, elf.strip().split("\n")))
    if elf_sum > maximum:
        maximum = elf_sum

print(maximum)
