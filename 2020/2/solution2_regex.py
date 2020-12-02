import re

with open("input1.txt") as input_file:
    valid_passwords = 0

    for line in input_file:
        m = re.match(r"^(\d+)-(\d+) (\w): (\w+)$", line.strip())
        id1, id2, char, password = m.groups()

        if (password[int(id1)-1] + password[int(id2)-1]).count(char) == 1:
            valid_passwords += 1
    
    print(f"Valid passwords: {valid_passwords}")
