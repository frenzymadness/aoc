import re

with open("input.txt") as input_file:
    lines = input_file.readlines()

original_instructions = []
to_modify = []

for index, line in enumerate(lines):
    match = re.match(r"(\w{3}) ([+-]\d+)", line.strip())
    instruction, number = match.groups()
    original_instructions.append((instruction, int(number)))
    if instruction in ("nop", "jmp"):
        to_modify.append(index)

while True:
    acumulator = 0

    instructions = list(original_instructions)
    index_to_modify = to_modify.pop()
    instruction_to_modify = instructions[index_to_modify]

    if instructions[index_to_modify][0] == "nop":
        instructions[index_to_modify] = ("jmp", instruction_to_modify[1])
    elif instructions[index_to_modify][0] == "jmp":
        instructions[index_to_modify] = ("nop", instruction_to_modify[1])

    executed_instructions = []

    next_instruction = 0

    while True:
        if next_instruction in executed_instructions:
            break
        else:
            executed_instructions.append(next_instruction)

        try:
            instruction, number = instructions[next_instruction]
        except IndexError:
            print("End reached, acumulator", acumulator)
            exit(0)

        if instruction == "acc":
            # print("Acc")
            acumulator += number
            next_instruction += 1
        elif instruction == "jmp":
            # print("Jmp")
            next_instruction += number
        elif instruction == "nop":
            # print("nop")
            next_instruction += 1
        else:
            raise RuntimeError("Unknown instruction")
