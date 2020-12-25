import re
import numpy
from itertools import product
from collections import defaultdict


def get_all_borders(image):
    result = []
    result.append(image[0, :])   # first row
    result.append(image[-1, :])  # last row
    result.append(image[:, 0])   # first col
    result.append(image[:, -1])  # last col
    # All of the above flipped
    for i in range(len(result)):
        result.append(numpy.flip(result[i]))

    return result


def count_possible_fits(borders1, borders2):
    result = 0
    for r1, r2 in product(borders1, borders2):
        if list(r1) == list(r2):
            result += 1
    return result


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

borders = {}

for k, v in images.items():
    borders[k] = get_all_borders(v)

fits = defaultdict(int)

for k1 in images:
    for k2 in images:
        if k1 == k2:
            continue
        count = count_possible_fits(borders[k1], borders[k2])
        fits[k1] += count
        fits[k2] += count

result = 1

for k, v in fits.items():
    if v == 8:
        result *= k

print(result)
