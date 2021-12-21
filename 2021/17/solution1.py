import re

with open("input.txt") as input_file:
    numbers = re.findall(r"-?\d+", input_file.read())

area = dict()
area["minx"], area["maxx"], area["miny"], area["maxy"] = map(int, numbers)
highest = area["miny"]

for x in range(1, area["maxx"] * 3):
    for y in range(-(area["maxy"] - area["miny"]) * 3, (area["maxy"] - area["miny"]) * 3):
        top = area["miny"]
        position = [0, 0]
        velocity = [x, y]
        while position[0] < area["maxx"] and position[1] > area["miny"]:
            position[0] += velocity[0]
            position[1] += velocity[1]
            velocity[0] += -1 if velocity[0] > 0 else 0  #-(velocity[0] > 0)
            velocity[1] -= 1
            top = max(top, position[1])
            if area["minx"] <= position[0] <= area["maxx"] and area["miny"] <= position[1] <= area["maxy"]:
                highest = max(highest, top)
                break

print(highest)
