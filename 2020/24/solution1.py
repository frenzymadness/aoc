with open("input.txt") as input_file:
    lines = input_file.readlines()

MOVES = {
    "ne": (0.5, 0.5),
    "e":  (1.0, 0.0),
    "se": (0.5, -0.5),
    "sw": (-0.5, -0.5),
    "w":  (-1.0, 0.0),
    "nw": (-0.5, 0.5),
}

black_tiles = []

for line in lines:
    line = line.strip()
    index = 0
    x, y = 0, 0
    while index < len(line):
        if line[index:index+2] in ("se", "sw", "nw", "ne"):
            instruction = line[index:index+2]
            index += 2
        else:
            instruction = line[index]
            index += 1
    
        mx, my = MOVES[instruction]
        x += mx
        y += my
    
    if (x, y) in black_tiles:
        black_tiles.remove((x, y))
    else:
        black_tiles.append((x, y))

print(len(black_tiles))
