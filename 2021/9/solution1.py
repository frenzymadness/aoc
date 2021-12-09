with open("input.txt") as input_file:
    map = input_file.read().splitlines()

low_points = []

for x in range(len(map)):
    for y in range(len(map[0])):
        neigh = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]        
        for nx, ny in neigh:
            if nx < 0 or ny < 0 or nx >= len(map) or ny >= len(map[0]):
                continue
            if map[nx][ny] <= map[x][y]:
                break
        else:
            low_points.append(map[x][y])

print(sum([int(n)+1 for n in low_points]))
