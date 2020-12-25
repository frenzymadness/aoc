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

black_tiles = set()
white_tiles = set()

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
        black_tiles.add((x, y))

print(len(black_tiles))

for x in range(100):
    new_black_tiles = set(black_tiles)
    new_white_tiles = set(white_tiles)
    for tile in black_tiles:
        adjacent = 0
        for move in MOVES.values():
            if (tile[0]+move[0], tile[1]+move[1]) in black_tiles:
                adjacent += 1
            else:
                white_tiles.add((tile[0]+move[0], tile[1]+move[1]))
                new_white_tiles.add((tile[0]+move[0], tile[1]+move[1]))
        
        if adjacent == 0 or adjacent > 2:
            new_black_tiles.remove(tile)
            new_white_tiles.add(tile)

    for tile in white_tiles:
        adjacent = 0
        for move in MOVES.values():
            if (tile[0]+move[0], tile[1]+move[1]) in black_tiles:
                adjacent += 1
        
        if adjacent == 2:
            new_black_tiles.add(tile)
            new_white_tiles.remove(tile)
    
    black_tiles = new_black_tiles
    white_tiles = new_white_tiles

print(len(new_black_tiles))
