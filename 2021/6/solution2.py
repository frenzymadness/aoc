from collections import Counter, defaultdict

with open("input.txt") as input_file:
    lines = input_file.readlines()

fish = [int(n) for n in lines[0].split(",")]
fish = defaultdict(int, Counter(fish))

for _ in range(256):
    new_fish = defaultdict(int)
    for k, v in fish.items():
        new_fish[k-1] = fish[k]
    fish = new_fish

    if -1 in fish:
        fish[6] += fish[-1]
        fish[8] = fish[-1]
        del fish[-1]

print(sum(fish.values()))
