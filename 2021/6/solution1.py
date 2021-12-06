with open("input.txt") as input_file:
    lines = input_file.readlines()
fish = [int(n) for n in lines[0].split(",")]

print(fish)

for _ in range(80):
    fish = [f-1 for f in fish]
    zeroes = fish.count(-1)
    for i, f in enumerate(fish):
        if f == -1:
            fish[i] = 6
    fish.extend([8]*zeroes)

print(len(fish))
