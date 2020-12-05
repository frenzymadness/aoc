def traverse(pass_, space, control_chars):
    queue = list(reversed(pass_))
    lower_char, upper_char = control_chars

    while queue:
        char = queue.pop()
        lower, upper = split_to_halves(space)

        if char == lower_char:
            space = lower
        elif char == upper_char:
            space = upper
        else:
            raise RuntimeError(char)
    
    return space[0]


def split_to_halves(list):
    return list[:len(list)//2], list[len(list)//2:]


def main():
    with open("input.txt") as input_file:
        boarding_passes = input_file.readlines()

    seat_ids = []

    for pass_ in boarding_passes:
        pass_ = pass_.strip()
        row_part, col_part = pass_[:7], pass_[7:]
        row_id = traverse(row_part, space=range(128), control_chars=("F", "B"))
        col_id = traverse(col_part, space=range(8), control_chars=("L", "R"))
        seat_ids.append(row_id * 8 + col_id)

    print(f"Max seat id: {max(seat_ids)}")

main()
