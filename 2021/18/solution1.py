from collections import deque
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

while len(data) > 1:
    line1 = data.popleft()
    line2 = data.popleft()

    merged = line1 + line2

    new_line = deque()
    while len(merged):
        number = merged.pop()
        new_line.appendleft([number[0], number[1] + 1])
    
    data.appendleft(new_line)

    while True:
        number = data[0]
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

print(number[0][0])
