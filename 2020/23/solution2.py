from copy import copy

with open("input.txt") as input_file:
    cups = [int(n) for n in input_file.read().strip()]

for x in range(max(cups), 1_000_000):
    cups.append(x+1)

maximum = max(cups)
minimum = min(cups)

selected = cups[0]
circle = {}
for i in range(len(cups)):
    if i == len(cups) - 1:
        circle[cups[i]] = cups[0]
    else:
        circle[cups[i]] = cups[i+1]

def play(circle, selected):
    following = circle[selected]
    picks = []
    for x in range(3):
        picks.append(following)
        following = circle[following]
    circle[selected] = following
    destination = selected - 1
    while destination in picks or destination <= 0:
        destination -= 1
        if destination <= 0:
            destination = maximum
    stitch = circle[destination]
    circle[destination] = picks[0]
    circle[picks[2]] = stitch
    return circle, following

for x in range(10_000_000):
    circle, selected = play(circle, selected)

print(circle[1]*circle[circle[1]])
