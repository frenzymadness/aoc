def main():
    with open("input.txt") as input_file:
        boarding_passes = input_file.readlines()

    seat_ids = []

    for pass_ in boarding_passes:
        pass_ = pass_.strip()
        row_id = int("0b" + pass_[:7].replace("F", "0").replace("B", "1"), 2)
        col_id = int("0b" + pass_[7:].replace("L", "0").replace("R", "1"), 2)
        seat_ids.append(row_id * 8 + col_id)

    print(f"Max seat id: {max(seat_ids)}")

main()
