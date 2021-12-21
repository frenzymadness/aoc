from itertools import cycle

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

pos = [int(lines[0].split(" ")[-1]), int(lines[1].split(" ")[-1])]

def deterministic_dice():
    used = 0
    dice = cycle(range(1, 101))
    while True:
        used += 3
        yield used, next(dice) + next(dice) + next(dice)

scores = [0, 0]
dice = deterministic_dice()

while max(scores) < 1000:
    for p in 0, 1:
        used, move = next(dice)

        pos[p] += move
        pos[p] = ((pos[p] - 1) % 10) + 1
        
        scores[p] += pos[p]

        if max(scores) >= 1000:
            break

print(used*min(scores))
