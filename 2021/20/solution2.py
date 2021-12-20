from itertools import product

algo = ""
image = []
pixels = {".": "0", "#": "1"}


with open("input.txt") as input_file:
    for line in input_file:
        line = line.strip()
        if not line:
            break
        algo += line
    
    for line in input_file:
        line = line.strip()
        image.append(list(line))

def get_area_index(image, x, y, default_value):
    binary = ""
    moves = (-1, 0, 1)
    for mx, my in product(moves, moves):
        nx = x + mx
        ny = y + my
        if nx < 0 or ny < 0 or nx >= len(image) or ny >= len(image[0]):
            binary += pixels[default_value]
        else:
            binary += pixels[image[nx][ny]]

    return int(binary, 2)

def evolve_image(image, default_value):
    for index in range(len(image)):
        image[index].append(default_value)
        image[index].insert(0, default_value)
    empty_line = [default_value] * len(image[0])
    image.insert(0, list(empty_line))
    image.insert(len(image), list(empty_line))

    new_image = []
    for x in range(len(image)):
        new_image.append([])
        for y in range(len(image[0])):
            index = get_area_index(image, x, y, default_value)
            final_pixel = algo[index]
            new_image[-1].append(final_pixel)
    
    return new_image

for iteration in range(50):
    if algo[0] == ".":
        default_value = "."
    else:
        default_value = ".#"[iteration % 2]
    image = evolve_image(image, default_value)

s = 0
for line in image:
    s += line.count("#")

print(s)
