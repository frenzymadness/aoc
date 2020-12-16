from collections import defaultdict
import re

validators = {}
tickets = []
valid_tickets = []

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

# Filter only valid tickets
for ticket in tickets:
    valid = True
    for n in [int(n) for n in ticket.split(",")]:
        for v in validators.values():
            if v(n):
                break
        else:
            valid = False

        
    if valid:
        valid_tickets.append(ticket)


# Get all possible validators for each column
fields_count = len(valid_tickets[0].split(","))
validators_for_field = defaultdict(list)

for i in range(fields_count):
    for n, v in validators.items():
        for field in [int(t.split(",")[i]) for t in valid_tickets]:
            if not v(field):
                break
        else:
            validators_for_field[i].append(n)


# If a column has only one possible validator
# remove that validator from other columns.
# Do it as long as any column has more than one
# validator.
while True:
    for f, v in validators_for_field.items():
        if len(v) == 1:
            for f2, v2 in validators_for_field.items():
                if f == f2:
                    continue
                if v[0] in v2:
                    del v2[v2.index(v[0])]
    
    if sum(len(v) for v in validators_for_field.values()) == len(validators_for_field):
        break


# Get the final result
my_ticket = [int(n) for n in my_ticket.split(",")]
result = 1

for n, v in validators_for_field.items():
    if v[0].startswith("departure"):
        result *= my_ticket[n]

print(result)
