file_name = "input"
input = 5

with open(file_name + ".txt") as input_file:
    program = input_file.readlines()[0].split(",")
    program = [int(c) for c in program]

def process_opcode(opcode):
    zero_string = str(opcode).zfill(5)
    m3, m2, m1, *instruction = zero_string
    return int(m3), int(m2), int(m1), int("".join(instruction))

def load_param(program, position, mode):
    if mode == 0:
        return program[program[position]]
    elif mode == 1:
        return program[position]
    return None

def store_result(program, position, mode, result):
    if mode == 0:
        program[program[position]] = result
    elif mode == 1:
        program[position] = result
    return program

pointer = 0

while True:
    opcode = program[pointer]
    m3, m2, m1, instruction = process_opcode(opcode)
    # print(program, "\n", pointer, instruction, (m1, m2, m3))
    if instruction == 99:
        #print(",".join([str(c) for c in program]))
        print("HALT")
        break
    
    if instruction in (1, 2):
        # addition and multiplication
        a = load_param(program, pointer+1, m1)
        b = load_param(program, pointer+2, m2)
        if instruction == 1:
            c = a + b
        elif instruction == 2:
            c = a * b
        program = store_result(program, pointer+3, m3, c)

        pointer += 4
        continue
    
    if instruction == 3:
        # input
        a = input
        program = store_result(program, pointer+1, m1, a)
        pointer += 2
        continue

    if instruction == 4:
        # output
        a = load_param(program, pointer+1, m1)
        print(a)
        pointer += 2
        continue

    if instruction == 5:
        # jump-if-true
        a = load_param(program, pointer+1, m1)
        if a != 0:
            pointer = load_param(program, pointer+2, m2)
        else:
            pointer += 3
        continue
    if instruction == 6:
        # jump-if-false
        a = load_param(program, pointer+1, m1)
        if a == 0:
            pointer = load_param(program, pointer+2, m2)
        else:
            pointer += 3
        continue
        
    if instruction == 7:
        # less than
        a = load_param(program, pointer+1, m1)
        b = load_param(program, pointer+2, m2)
        if a < b:
            program = store_result(program, pointer+3, m3, 1)
        else:
            program = store_result(program, pointer+3, m3, 0)
        
        pointer += 4
        continue
    if instruction == 8:
        # equals
        a = load_param(program, pointer+1, m1)
        b = load_param(program, pointer+2, m2)
        if a == b:
            program = store_result(program, pointer+3, m3, 1)
        else:
            program = store_result(program, pointer+3, m3, 0)
    
        pointer += 4
        continue
