with open("input.txt") as input_file:
    instructions = input_file.readlines()

directions = ["N", "E", "S", "W"]
reversed_directions = list(reversed(directions))

direction = "E"

pos_n = 0
pos_e = 0

for instruction in instructions:
    # print(instruction.strip())
    command, length = instruction[0], instruction[1:]
    length = int(length)

    if command == "F":
        command = direction

    if command == "N":
        pos_n += length
    elif command == "S":
        pos_n -= length
    elif command == "E":
        pos_e += length
    elif command == "W":
        pos_e -= length
    elif command == "L":
        steps = length // 90
        cur = reversed_directions.index(direction)
        direction = reversed_directions[(cur + steps) % len(reversed_directions)]
    elif command == "R":
        steps = length // 90
        cur = directions.index(direction)
        direction = directions[(cur + steps) % len(directions)]
    
    # print(direction, pos_n, pos_e)

print(abs(pos_n) + abs(pos_e))
