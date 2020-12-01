with open("input.txt") as input_file:
    codes = [l.strip() for l in input_file.readlines()]

two_count = 0
three_count = 0

for code in codes:
    print(code)
    two = False
    three = False
    for char in code:
        if code.count(char) == 2:
            two = True
        if code.count(char) == 3:
            three = True
        
    if two:
        two_count += 1
    if three:
        three_count += 1

print(two_count * three_count)
