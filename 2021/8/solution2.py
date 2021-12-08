from itertools import permutations

valid_numbers = [
    [1, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 0, 0, 0, 0],
    [1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 0, 0, 1],
    [0, 1, 1, 0, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1],
    [1, 0, 1, 1, 1, 1, 1],
    [1, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 0, 1, 1],
]

def display_from_signal(permutation, signal):
    number = [0] * 7
    for char in signal:
        number[permutation.index(char)] = 1
    return number

def number_from_display(number):
    return valid_numbers.index(number)

final_result = 0

with open("input.txt") as input_file:
    lines = input_file.readlines()

for line in lines:
    signals, digits = line.split(" | ")
    lens = list(map(len, signals))

    for permutation in permutations("abcdefg"):
        for signal in signals.split():
            number = display_from_signal(permutation, signal)
            if number not in valid_numbers:
                break
        else:
            break

    result = ""

    for digit in digits.split():
        result += str(number_from_display(display_from_signal(permutation, digit)))
    final_result += int(result)

print(final_result)
