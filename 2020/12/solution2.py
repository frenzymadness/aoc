from math import sin, cos, radians

with open("input.txt") as input_file:
    instructions = input_file.readlines()

directions = ["N", "E", "S", "W"]
reversed_directions = list(reversed(directions))

direction = "E"

wp_pos_n = 1
wp_pos_e = 10

pos_n = 0
pos_e = 0

for instruction in instructions:
    # print(instruction.strip())
    command, length = instruction[0], instruction[1:]
    length = int(length)

    if command == "F":
        pos_n += length * wp_pos_n
        pos_e += length * wp_pos_e

    if command == "N":
        wp_pos_n += length
    elif command == "S":
        wp_pos_n -= length
    elif command == "E":
        wp_pos_e += length
    elif command == "W":
        wp_pos_e -= length
    elif command == "L":
        new_pos_n = int(round(wp_pos_n * cos(radians(length)) + wp_pos_e * sin(radians(length))))
        new_pos_e = int(round(wp_pos_e * cos(radians(length)) - wp_pos_n * sin(radians(length))))
        wp_pos_n = new_pos_n
        wp_pos_e = new_pos_e
    elif command == "R":
        new_pos_n = int(round(wp_pos_n * cos(radians(-length)) + wp_pos_e * sin(radians(-length))))
        new_pos_e = int(round(wp_pos_e * cos(radians(-length)) - wp_pos_n * sin(radians(-length))))
        wp_pos_n = new_pos_n
        wp_pos_e = new_pos_e
    
    # print(direction, pos_n, pos_e, wp_pos_n, wp_pos_e)

print(abs(pos_n) + abs(pos_e))
