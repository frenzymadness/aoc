with open("input1.txt") as input_file:
    valid_passwords = 0

    for line in input_file:
        policy, password = line.split(":")
        limits, char = policy.split()
        min, max = limits.split("-")
        count = password.strip().count(char)
        if int(min) <= count <= int(max):
            valid_passwords += 1
    
    print(f"Valid passwords: {valid_passwords}")
