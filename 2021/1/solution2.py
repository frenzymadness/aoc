with open("input.txt") as input_file:
    lines = input_file.readlines()
numbers = [int(n) for n in lines]
counter = 0
for n in range(len(numbers)-2):
    current_sum = sum(numbers[n:n+3])
    next_sum = sum(numbers[n+1:n+4])
    if next_sum > current_sum:
        counter += 1
print(counter)
