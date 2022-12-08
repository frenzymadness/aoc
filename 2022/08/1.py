from pathlib import Path

here = Path(__file__).parent

trees = []

with open(here / "input") as file:
    for line in file:
        trees.append(list(map(int, line.strip())))

coords = [(r, c) for r in range(1, len(trees)-1) for c in range(1, len(trees[0])-1)]

visible_count = 0

for r, c in coords:
    height = trees[r][c]
    for x in range(r+1, len(trees)):
        if trees[x][c] >= height:
            break
    else:
        visible_count += 1
        continue

    for x in range(r-1, -1, -1):
        if trees[x][c] >= height:
            break
    else:
        visible_count += 1
        continue

    for x in range(c+1, len(trees[0])):
        if trees[r][x] >= height:
            break
    else:
        visible_count += 1
        continue

    for x in range(c-1, -1, -1):
        if trees[r][x] >= height:
            break
    else:
        visible_count += 1
        continue

visible_count += (len(trees) * 2 + len(trees[0]) * 2) - 4

print(visible_count)
