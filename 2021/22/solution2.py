import re
from itertools import product
from dataclasses import dataclass
from collections import Counter

@dataclass
class Cuboid:
    xmin: int
    xmax: int
    ymin: int
    ymax: int
    zmin: int
    zmax: int

    def size(self):
        return (self.xmax-self.xmin+1) * (self.ymax-self.ymin+1) * (self.zmax-self.zmin+1)
    
    def intersection(self, other):
        xmin = max(self.xmin, other.xmin)
        xmax = min(self.xmax, other.xmax)
        ymin = max(self.ymin, other.ymin)
        ymax = min(self.ymax, other.ymax)
        zmin = max(self.zmin, other.zmin)
        zmax = min(self.zmax, other.zmax)

        if xmin <= xmax and ymin <= ymax and zmin <= zmax:
            return Cuboid(xmin, xmax, ymin, ymax, zmin, zmax)

    def __hash__(self):
        return hash((self.xmin, self.xmax, self.ymin, self.ymax, self.zmin, self.zmax))

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

cuboids = Counter()

for line in lines:
    match = re.match(r"(on|off) x=(-?\d+)\.\.(-?\d+),y=(-?\d+)\.\.(-?\d+),z=(-?\d+)\.\.(-?\d+)", line)
    instruction, *numbers = match.groups()
    numbers = list(map(int, numbers))

    new_cuboid = Cuboid(*numbers)
    update = Counter()
    for old_cuboid, count in cuboids.items():
        intersection_cuboid = new_cuboid.intersection(old_cuboid)
        if intersection_cuboid is not None:
            update[intersection_cuboid] -= count
        
    if instruction == "on":
        update[new_cuboid] = 1
    
    cuboids.update(update)

total_size = 0
for cuboid, count in cuboids.items():
    total_size += cuboid.size() * count

print(total_size)
