from copy import copy

with open("input.txt") as input_file:
    cups = [int(n) for n in input_file.read().strip()]

length = len(cups)
maximum = max(cups)
selected = 0

for x in range(100):
    selected_cup = cups[selected]
    # Get the three cups and remove them from the list
    picks = []
    cups_copy = copy(cups)
    for i in range(1, 4):
        pick = (selected + i) % length
        picks.append(cups_copy[pick])
        del cups[cups.index(cups_copy[pick])]
    # Calculate destination
    destination = selected_cup - 1
    while destination in picks or destination <= 0:
        destination -= 1
        if destination <= 0:
            destination = maximum
    dest_index = cups.index(destination)
    # Insert picks back
    cups = cups[:dest_index+1] + picks + cups[dest_index+1:]
    # Rearange cups to the circle
    while cups[selected] != selected_cup:
        cups = cups[1:] + [cups[0]]
    selected = (selected + 1) % length

one = cups.index(1)
result = ""
for i in range(length - 1):
    result += str(cups[(one + 1 + i) % length])

print(result)