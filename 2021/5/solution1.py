import re
from collections import defaultdict


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = min(x1, x2)
        self.x2 = max(x1, x2)
        self.y1 = min(y1, y2)
        self.y2 = max(y1, y2)

    def all_points(self):
        for x in range(self.x1, self.x2+1):
            for y in range(self.y1, self.y2+1):
                yield (x, y)

    def __repr__(self):
        return f"{self.x1},{self.y1} -> {self.x2},{self.y2}"

lines = []

with open("input.txt") as input_file:
    for line in input_file:
        match = re.match(r"(\d+),(\d+) -> (\d+),(\d+)", line)
        coords = [int(n) for n in match.groups()]
        x1, y1, x2, y2 = coords
        if x1 == x2 or y1 == y2:
            lines.append(Line(*coords))
        else:
            print("Not horizontal or vertical", match.groups())

points = defaultdict(int)
for line in lines:
    for point in line.all_points():
        points[point] += 1

print(len(list(filter(lambda x: x > 1, points.values()))))
