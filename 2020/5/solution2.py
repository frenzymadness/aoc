from itertools import product


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

    row_ids = []
    col_ids = []

    for pass_ in boarding_passes:
        pass_ = pass_.strip()
        row_part, col_part = pass_[:7], pass_[7:]
        row_id = traverse(row_part, space=range(128), control_chars=("F", "B"))
        col_id = traverse(col_part, space=range(8), control_chars=("L", "R"))

        row_ids.append(row_id)
        col_ids.append(col_id)

    print(f"Rows - minimum: {min(row_ids)}, maximum: {max(row_ids)}")
    print(f"Cols - minimum? {min(col_ids)}, maximum: {max(col_ids)}")

    all_rows = range(min(row_ids), max(row_ids))
    all_cols = range(min(col_ids), max(col_ids))

    all_seats = set(product(all_rows, all_cols))
    all_seats_found = set(zip(row_ids, col_ids))

    for missing_seat in all_seats - all_seats_found:
        print(f"Missing seat: {missing_seat}, ID:{missing_seat[0]*8+missing_seat[1]}")

main()
