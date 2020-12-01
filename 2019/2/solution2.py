def get_data(file_name):
    with open(file_name + ".txt") as input_file:
        program = input_file.readlines()[0].split(",")
        program = [int(c) for c in program]
    return program

def part1(data, noun=None, verb=None):
    program = data[:]

    if noun is not None:
        program[1] = noun
    if verb is not None:
        program[2] = verb

    for base in range(0, len(program), 4):
        opcode = program[base]
        if opcode == 99:
            return program[0]
        a = program[program[base + 1]]
        b = program[program[base + 2]]
        if opcode == 1:
            c = a + b
        elif opcode == 2:
            c = a * b
        program[program[base + 3]] = c

def part2(data):
    for noun in range(100):
        for verb in range(100):
            if part1(data, noun, verb) == 19690720:
                return 100 * noun + verb

print("Second part", part2(get_data("input")))
