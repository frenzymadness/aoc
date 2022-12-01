print(sum(sorted([sum(map(int, elf.strip().split("\n"))) for elf in open("01/input").read().split("\n\n")], reverse=True)[:3]))
