import re
from itertools import product

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

on = set()

for line in lines:
    match = re.match(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line)
    instruction, *numbers = match.groups()
    numbers = list(map(int, numbers))
    for index, number in enumerate(numbers):
        if number < -50:
            numbers[index] = -50
        if number > 50:
            numbers[index] = 50
        
        skip = any([abs(numbers[i]) == abs(numbers[i+1]) == 50 for i in range(0, 6, 2)])
    
    if skip:
        continue

    xmin, xmax, ymin, ymax, zmin, zmax = numbers

    all_combinations = product(range(xmin, xmax+1), range(ymin, ymax+1), range(zmin, zmax+1))

    for x, y, z in all_combinations:
        if any((x>50, x<-50, y>50, y<-50, z>50, z<-50)):
            continue
        if instruction == "on":
            on.add((x, y, z))
        else:
            try:
                on.remove((x, y, z))
            except KeyError:
                pass

print(len(on))
