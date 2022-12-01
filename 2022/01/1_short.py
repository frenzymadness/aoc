print(max([sum(map(int, elf.strip().split("\n"))) for elf in open("01/input").read().split("\n\n")]))
