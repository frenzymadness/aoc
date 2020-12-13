from functools import reduce
from math import gcd


def lcm(a, b):
    return a * b // gcd(a, b)


def sync(buses):
    # highest bus number and its index in line
    period, maxi = max((bus, i) for i, bus in enumerate(buses))
    # time differences for all  non zero busses (negative)
    diffs = [(i - maxi, bus) for i, bus in enumerate(buses) if bus]
    # Biggest negative difference from the highest bus id
    mindiff = min(diffs)[0]
    t = 0
    while diffs:
        # Jump to the future by given period
        t += period
        # Get all busses synced in the t
        synced = [bus for diff, bus in diffs if (t + diff) % bus == 0]
        # If we have some synced busses here, calculate next jump and remove them from diffs
        if synced:
            period = reduce(lcm, [period] + synced)
            diffs = [(diff, bus) for diff, bus in diffs if bus not in synced]
    return t + mindiff


with open("input.txt") as input_file:
    _ = int(input_file.readline().strip())
    busses = [int(bus.replace("x", "0")) for bus in input_file.readline().strip().split(",")]

print(sync(busses))
