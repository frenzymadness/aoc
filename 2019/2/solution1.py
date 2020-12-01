file_name = "input"

with open(file_name + ".txt") as input_file:
    program = input_file.readlines()[0].split(",")
    program = [int(c) for c in program]

if file_name == "input":
    program[1] = 12
    program[2] = 2

for base in range(0, len(program), 4):
    opcode = program[base]
    if opcode == 99:
        print(",".join([str(c) for c in program]))
        break
    a = program[program[base + 1]]
    b = program[program[base + 2]]
    if opcode == 1:
        c = a + b
    elif opcode == 2:
        c = a * b
    program[program[base + 3]] = c
