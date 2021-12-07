with open("input.txt") as input_file:
    numbers = [int(n) for n in input_file.read().split(",")]

avg = sum(numbers) // len(numbers)

fuel = 0
for n in numbers:
    src = min(n, avg)
    dest = max(n, avg)
    fuel += sum(range(1, (dest-src)+1))

print(fuel)
