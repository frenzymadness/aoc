import re

with open("input1.txt") as input_file:
    valid_passwords = 0

    for line in input_file:
        m = re.match(r"^(\d+)-(\d+) (\w): (\w+)$", line.strip())
        min, max, char, password = m.groups()

        if int(min) <= password.count(char) <= int(max):
            valid_passwords += 1
    
    print(f"Valid passwords: {valid_passwords}")
