import re
from dataclasses import dataclass
from collections import defaultdict
from itertools import cycle

@dataclass
class Line:
    x1: int
    y1: int
    x2: int
    y2: int

    def all_points(self):
        stepx = 1 if self.x1 < self.x2 else -1
        stepy = 1 if self.y1 < self.y2 else -1

        if self.x1 == self.x2:
            x = cycle((self.x1,))
        else:
            x = range(self.x1, self.x2+stepx, stepx)
        
        if self.y1 == self.y2:
            y = cycle((self.y1,))
        else:
            y = range(self.y1, self.y2+stepy, stepy)
        yield from zip(x, y)

    def __repr__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"

lines = []

with open("input.txt") as input_file:
    for line in input_file:
        match = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line)
        coords = [int(n) for n in match.groups()]
        lines.append(Line(*coords))

points = defaultdict(int)
for line in lines:
    for point in line.all_points():
        points[point] += 1

print(len(list(filter(lambda x: x > 1, points.values()))))
