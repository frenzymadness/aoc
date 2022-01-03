from collections import Counter, deque
from itertools import starmap

all_rotations = [
    lambda x, y, z: (x, y, z),
    lambda x, y, z: (z, y, -x),
    lambda x, y, z: (-x, y, -z),
    lambda x, y, z: (-z, y, x),
    lambda x, y, z: (-x, -y, z),
    lambda x, y, z: (-z, -y, -x),
    lambda x, y, z: (x, -y, -z),
    lambda x, y, z: (z, -y, x),
    lambda x, y, z: (x, -z, y),
    lambda x, y, z: (y, -z, -x),
    lambda x, y, z: (-x, -z, -y),
    lambda x, y, z: (-y, -z, x),
    lambda x, y, z: (x, z, -y),
    lambda x, y, z: (-y, z, -x),
    lambda x, y, z: (-x, z, y),
    lambda x, y, z: (y, z, x),
    lambda x, y, z: (z, x, y),
    lambda x, y, z: (y, x, -z),
    lambda x, y, z: (-z, x, -y),
    lambda x, y, z: (-y, x, z),
    lambda x, y, z: (-z, -x, y),
    lambda x, y, z: (y, -x, z),
    lambda x, y, z: (z, -x, -y),
    lambda x, y, z: (-y, -x, -z),
]

def generate_all_rotations(scan):
    for rotation in all_rotations:
        yield list(starmap(rotation, scan))

def move_scanner(scan, dx, dy, dz):
    return [(x + dx, y + dy, z + dz) for x, y, z in scan]

def find_scanner(base, rotated_scans):
    for scan in rotated_scans:
        diff, count = Counter((x2 - x1, y2 - y1, z2 - z1)
                                  for x1, y1, z1 in scan
                                  for x2, y2, z2 in base).most_common(1)[0]
        if count >= 12:
            return diff, move_scanner(scan, *diff)
    return None, None

def solve(all_scans):
    solved = set(all_scans[0])
    del all_scans[0]
    remaining = deque(list(generate_all_rotations(scan)) for scan in all_scans)
    scanners = [(0, 0, 0)]

    while remaining:
        rotated_scans = remaining.popleft()
        scanner, moved = find_scanner(solved, rotated_scans)
        if scanner:
            solved |= set(moved)
            scanners.append(scanner)
        else:
            remaining.append(rotated_scans)

    return solved, scanners

all_scans = []

with open("input.txt") as input_file:
    lines = input_file.readlines()

for line in lines:
    if line.startswith("---"):
        all_scans.append([])
    elif "," in line:
        all_scans[-1].append(tuple(map(int, line.split(","))))

solved, scanners = solve(all_scans)
print(len(solved))
