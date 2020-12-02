with open("input1.txt") as input_file:
    valid_passwords = 0

    for line in input_file:
        policy, password = line.split(":")
        password = password.strip()
        indexes, char = policy.split()
        id1, id2 = indexes.split("-")
        two_chars = password[int(id1)-1] + password[int(id2)-1]
        if two_chars.count(char) == 1:
            valid_passwords += 1
    
    print(f"Valid passwords: {valid_passwords}")
