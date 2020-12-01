pass_range = 387638, 919123 + 1

pass_list = list(range(*pass_range))

def check_password(password):
    digits = [int(c) for c in str(password)]
    same_adjacent = False
    for index, digit in enumerate(digits[:-1]):
        if digit == digits[index + 1]:
            same_adjacent = True
        if digit > digits[index + 1]:
            return False
    return same_adjacent

correct_pass = list(filter(check_password, pass_list))

print(correct_pass)
print(len(correct_pass))
