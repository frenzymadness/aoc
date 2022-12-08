from pathlib import Path

here = Path(__file__).parent

trees = []

with open(here / "input") as file:
    for line in file:
        trees.append(list(map(int, line.strip())))

coords = [(r, c) for r in range(1, len(trees)-1) for c in range(1, len(trees[0])-1)]

best_score = 0

for r, c in coords:
    height = trees[r][c]
    score_up, score_down, score_left, score_right = 0, 0, 0, 0
    for x in range(r+1, len(trees)):
        score_up += 1
        if trees[x][c] >= height:
            break

    for x in range(r-1, -1, -1):
        score_down += 1
        if trees[x][c] >= height:
            break

    for x in range(c+1, len(trees[0])):
        score_right += 1
        if trees[r][x] >= height:
            break

    for x in range(c-1, -1, -1):
        score_left += 1
        if trees[r][x] >= height:
            break

    score = score_up * score_down * score_left * score_right
    if score > best_score:
        best_score = score

print(best_score)
