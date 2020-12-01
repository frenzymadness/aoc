def get_data(filename):
    with open(filename) as input_file:
        w1, w2 = input_file.readlines()[:2]
    w1 = [(instruction[0], int(instruction[1:])) for instruction in w1.split(",")]
    w2 = [(instruction[0], int(instruction[1:])) for instruction in w2.split(",")]
    return w1, w2

def trace(wire, init=(1000,1000)):
    wire_points = [init]
    for direction, steps in wire:
        start_x, start_y = wire_points[-1]
        if direction == "R":
            points = [(x, start_y) for x in range(start_x+1, start_x+steps+1)]
        elif direction == "L":
            points = [(x, start_y) for x in range(start_x-1, start_x-steps-1, -1)]
        elif direction == "U":
            points = [(start_x, y) for y in range(start_y+1, start_y+steps+1)]
        elif direction == "D":
            points = [(start_x, y) for y in range(start_y-1, start_y-steps-1, -1)]
        
        wire_points.extend(points)
    return wire_points[1:]


def intersections(w1_points, w2_points):
    return set(w1_points).intersection(set(w2_points))


def min_manhattan(points, init=(1000,1000)):
    init_x, init_y = init
    distances = []
    for point_x, point_y in points:
        distance = abs(point_x - init_x) + abs(point_y - init_y)
        distances.append(distance)
    return min(distances)

w1, w2 = get_data("input.txt")
# print(w1)
# print(w2)
w1_points = trace(w1)
w2_points = trace(w2)
#print(w1_points)
#print(w2_points)
inter = intersections(w1_points, w2_points)
print(inter)
distance = min_manhattan(inter)
print(distance)
