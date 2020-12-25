import re
import numpy
from math import sqrt


def get_all_transformations(image):
    result = []
    for x in range(0, 4):
        result.append(numpy.rot90(image, k=x))

    for i in range(len(result)):
        result.append(numpy.flip(result[i], 0))

    return result


def assemble_tiles(image_transformations, image_size):
    image = [[(0, 0)] * image_size for _ in range(image_size)]
    remaining = set(image_transformations.keys())

    def _assemble_tiles(rowcolumn):
        if rowcolumn == image_size ** 2:
            return True
        r, c = rowcolumn // image_size, rowcolumn % image_size
        for tileid in list(remaining):
            for i, transformation in enumerate(image_transformations[tileid]):
                up_ok = left_ok = True
                if r > 0:
                    up_tileid, up_transformation = image[r - 1][c]
                    up_tile = image_transformations[up_tileid][up_transformation]
                    up_ok = (transformation[0] == up_tile[9]).all()
                if c > 0:
                    left_tileid, left_transformation = image[r][c - 1]
                    left_tile = image_transformations[left_tileid][left_transformation]
                    left_ok = (transformation[:, 0] == left_tile[:, 9]).all()
                if up_ok and left_ok:
                    image[r][c] = (tileid, i)
                    remaining.remove(tileid)
                    if _assemble_tiles(rowcolumn + 1):
                        return True
                    remaining.add(tileid)
        return False
    _assemble_tiles(0)

    return image


def get_monster_indexes():
    monster_pattern = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]
    indexes = []
    for r in range(len(monster_pattern)):
        for c in range(len(monster_pattern[r])):
            if monster_pattern[r][c] == '#':
                indexes.append((r, c))

    return indexes


with open("input.txt") as input_file:
    inp = input_file.read()

images = {}

it = iter(inp.splitlines())

for line in it:
    if line.startswith("Tile"):
        number = re.match(r"Tile (\d+):", line).groups()[0]
        number = int(number)
        images[int(number)] = []
        for line in it:
            if line.strip() == "":
                break
            images[number].append([c for c in line])
        images[number] = numpy.array(images[number])

image_transformations = {id: get_all_transformations(image) for id, image in images.items()}
image_size = int(sqrt(len(image_transformations)))
image_matrix = assemble_tiles(image_transformations, image_size)

print(image_matrix)

image = [['.'] * (image_size * 8) for _ in range(image_size * 8)]

for r in range(image_size):
    for c in range(image_size):
        tileid, transformation = image_matrix[r][c]
        tile = image_transformations[tileid][transformation]
        for i in range(1, 9):
            for j in range(1, 9):
                image[8 * r + i - 1][8 * c + j - 1] = tile[i, j]

for image in get_all_transformations(image):
    monster = 0
    for r in range(len(image) - 3):
        for c in range(len(image) - 20):
            if all(image[r + dr, c + dc] == '#' for dr, dc in get_monster_indexes()):
                monster += 1
    if monster > 0:
        total = numpy.sum(image == "#")
        print(total - monster * len(get_monster_indexes()))
