import re

validators = {}
tickets = []
invalid_numbers = []

def validator_from_string(s):
    m = re.match(r"^(.*): (\d+)-(\d+) or (\d+)-(\d+)$", s)
    if m is None:
        print(s)
    name, min1, max1, min2, max2 = m.groups()
    
    def validator(number):
        return int(min1) <= number <= int(max1) or int(min2) <= number <= int(max2)
    
    return name, validator


with open("input.txt") as input_file:
    # Rules
    for line in input_file:
        line = line.strip()
        if line == "":
            break
        n, v = validator_from_string(line)
        validators[n] = v
    
    # My ticket
    for line in input_file:
        line = line.strip()
        if line == "your ticket:":
            continue
        if line == "":
            break
        my_ticket = line
    
    # Other tickets
    for line in input_file:
        line = line.strip()
        if line == "nearby tickets:":
            continue
        tickets.append(line)

# print(validators, my_ticket, tickets)

for ticket in tickets:
    for number in [int(n) for n in ticket.split(",")]:
        valid = False
        for validator in validators.values():
            if validator(number):
                valid = True
        
        if not valid:
            invalid_numbers.append(number)

print(sum(invalid_numbers))
