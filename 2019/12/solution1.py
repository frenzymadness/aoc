from itertools import combinations

# Load from file
with open("input.txt") as input_file:
    lines = input_file.readlines()

moons = []

# Parse moons coordinates
for line in lines:
    line = line.strip()
    line = line.rstrip(">").lstrip("<")
    coords = [int(part.split("=")[1]) for part in line.split(",")]
    moons.append(tuple(coords))

print("moons init\n", moons)

velocity_update = {}
for moon in moons:
    velocity_update[moon] = [0,0,0]

for step in range(1,1001):
    print("="*10, step)

    for moon1, moon2 in combinations(moons, 2):
        for i, (coord1, coord2) in enumerate(zip(moon1, moon2)):
            if coord1 < coord2:
                velocity_update[moon1][i] += 1
                velocity_update[moon2][i] -= 1
            elif coord2 < coord1:
                velocity_update[moon1][i] -= 1
                velocity_update[moon2][i] += 1

    print("velocity updates\n", velocity_update)

    for im, moon in enumerate(moons):
        new_coords = []
        for i in range(3):
            new_coords.append(moon[i] + velocity_update[moon][i])
        moons[im] = tuple(new_coords)
        velocity_update[tuple(new_coords)] = velocity_update[moon]

    print("new position\n", moons)

    total = 0
    for moon in moons:
        pot = sum([abs(coord) for coord in moon])
        kin = sum([abs(coord) for coord in velocity_update[moon]])
        moon_total = pot * kin
        total += moon_total
        print(f"moon {moon}, pot {pot}, kin {kin}, moon total {moon_total}")
    
    print(f"total {total}")
