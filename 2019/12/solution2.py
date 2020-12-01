from itertools import combinations, cycle

four_zeros = [(0,0,0) for _ in range(4)]

# Load from file
with open("test.txt") as input_file:
    lines = input_file.readlines()

moons = []

# Parse moons coordinates
for line in lines:
    line = line.strip()
    line = line.rstrip(">").lstrip("<")
    coords = [int(part.split("=")[1]) for part in line.split(",")]
    moons.append(tuple(coords))

moons_init = list(moons)

print("moons init\n", moons)

velocity_update = {}
for moon in moons:
    velocity_update[moon] = [0,0,0]

velocity_update_records = []

step = -1
for _ in range(5000):
    step += 1
    if step % 1000 == 0:
        print(step)
    # print("="*10, step)

    for moon1, moon2 in combinations(moons, 2):
        for i, (coord1, coord2) in enumerate(zip(moon1, moon2)):
            if coord1 < coord2:
                velocity_update[moon1][i] += 1
                velocity_update[moon2][i] -= 1
            elif coord2 < coord1:
                velocity_update[moon1][i] -= 1
                velocity_update[moon2][i] += 1


    if step > 1 and velocity_update_records[-1] == four_zeros:
        print("same velocity update", step)
        print(velocity_update_records[-1])
        print(moons)
        break


    # print("velocity updates\n", velocity_update)
    velocity_update_new = {}
    for im, moon in enumerate(moons):
        new_coords = []
        for i in range(3):
            new_coords.append(moon[i] + velocity_update[moon][i])
        moons[im] = tuple(new_coords)
        velocity_update_new[tuple(new_coords)] = velocity_update[moon]
    velocity_update = velocity_update_new
    velocity_update_records.append([tuple(v) for k, v in velocity_update_new.items()])
    # print(velocity_update_records)
    # print(f"total {total}")

# for x in range(1384, 1388):
#     print(velocity_update_records[x])

for velocity_update in cycle(velocity_update_records):
    step += 1
    if step % 1000 == 0:
        print(step)
    if step == 10000:
        print("FAIL")
        break

    for im, moon in enumerate(moons):
        new_coords = []
        for i in range(3):
            new_coords.append(moon[i] + velocity_update[im][i])
        moons[im] = tuple(new_coords)
    
    # print(moons)

    if velocity_update == four_zeros or moons == moons_init:
        print(velocity_update == four_zeros, moons == moons_init)
        print(moons, moons_init)
        print(step)
        break
