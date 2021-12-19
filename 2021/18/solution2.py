from collections import deque
from itertools import product
from math import ceil, floor

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

data = deque()

for line in lines:
    level = 0
    new_line = deque()
    for char in line:
        if char == "[":
            level += 1
        elif char == "]":
            level -= 1
        elif char.isdigit():
            new_line.append([int(char), level])
    data.append(new_line)

def magnitude(line1, line2):
    merged = line1 + line2

    number = deque()
    while len(merged):
        part = merged.pop()
        number.appendleft([part[0], part[1] + 1])

    while True:
        # Explosion
        explosion = False
        for index, (n, level) in enumerate(number):
            if level > 4:
                if index > 0:
                    number[index-1][0] += n
                if index < len(number) - 2:
                    number[index+2][0] += number[index+1][0]
                del number[index]
                number[index] = [0, level-1]
                explosion = True
                break
        
        if explosion:
            continue

        # Split
        split = False
        for index, (n, level) in enumerate(number):
            if n >= 10:
                left = floor(n / 2)
                right = ceil(n / 2)
                number[index] = [right, level+1]
                number.insert(index, [left, level+1])
                split = True
                break


        if explosion or split:
            continue
        break

    for level in range(4, 0, -1):
        index = 0
        while True:
            try:
                if number[index][1] == number[index+1][1]:
                    number[index][1] -= 1
                    number[index][0] = number[index][0] * 3 + number[index+1][0] * 2
                    del number[index+1]
                index += 1
            except IndexError:
                break

    return number[0][0]

max_mag = None

for line1, line2 in product(data, data):
    if line1 == line2:
        continue
    mag = magnitude(line1, line2)
    if max_mag is None or mag > max_mag:
        max_mag = mag

print(max_mag)
