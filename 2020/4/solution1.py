import re

with open("input.txt") as input_file:
    input = input_file.read()

pattern = re.compile(r"(\w+):(\S+)")

required_keys = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
valid_passports = 0

for passport in input.split("\n\n"):
    keys = []
    for match in pattern.finditer(passport):
        key, value = match.groups()
        keys.append(key)
    if all([key in keys for key in required_keys]):
        valid_passports += 1

print(f"Valid passports: {valid_passports}")
