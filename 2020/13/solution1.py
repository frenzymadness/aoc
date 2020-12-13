with open("input.txt") as input_file:
    time = int(input_file.readline().strip())
    busses = input_file.readline().strip().split(",")

def departures(bus):
    multiplier = 0
    while True:
        multiplier += 1
        yield multiplier * bus

def next_after(bus, time):
    for departure in departures(bus):
        if departure >= time:
            return departure

future_departures = []

for bus in busses:
    if bus == "x":
        continue
    bus = int(bus)
    future_departures.append((next_after(bus, time), bus))

departure, bus = min(future_departures)
print((departure - time) * bus)
