import re

def get_input():
    with open("input.txt") as input_file:
        return input_file.read()


def hgt_validate(value):
    if value.endswith("cm"):
        return 150 <= int(value[:-2]) <= 193
    elif value.endswith("in"):
        return 59 <= int(value[:-2]) <= 76
    return False


def hcl_validate(value):
    return re.match(r"^#[0-9a-f]{6}$", value) is not None


keys_validation = {
    "byr": lambda x: 1920 <= int(x) <= 2002,
    "iyr": lambda x: 2010 <= int(x) <= 2020,
    "eyr": lambda x: 2020 <= int(x) <= 2030,
    "hgt": hgt_validate,
    "hcl": hcl_validate,
    "ecl": lambda x: x in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth"),
    "pid": lambda x: len(x) == 9 and x.isdigit()
}


def main():
    pattern = re.compile(r"(\w+):(\S+)")

    valid_passports = 0

    for passport in get_input().split("\n\n"):
        keys = []
        valid = True
        for match in pattern.finditer(passport):
            key, value = match.groups()
            keys.append(key)
            validation = keys_validation.get(key, lambda x: True)
            if not validation(value):
                valid = False
        if valid and all([key in keys for key in keys_validation.keys()]):
            valid_passports += 1

    print(f"Valid passports: {valid_passports}")


if __name__ == "__main__":
    main()
