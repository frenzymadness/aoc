with open("input.txt") as input_file:
    numbers = [int(n) for n in input_file.read().split(",")]

med = sorted(numbers)[len(numbers)//2]

fuel = 0
for n in numbers:
    src = min(n, med)
    dest = max(n, med)
    fuel += dest - src

print(fuel)
