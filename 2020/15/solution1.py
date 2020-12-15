with open("input.txt") as input_file:
    numbers = [int(n) for n in input_file.read().strip().split(",")]

while True:
    last = numbers[-1]
    if last not in numbers[:-1]:
        numbers.append(0)
    else:
        last_turn = len(numbers)
        before_last_turn = len(numbers) - list(reversed(numbers[:-1])).index(last) - 1
        diff = last_turn - before_last_turn
        numbers.append(diff)

    try:
        print(numbers[2019])
        break
    except IndexError:
        pass
