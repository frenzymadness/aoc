import re

with open("input.txt") as input_file:
    lines = input_file.readlines()

acumulator = 0
instructions = []
executed_instructions = []

for line in lines:
    match = re.match(r"(\w{3}) ([+-]\d+)", line.strip())
    instruction, number = match.groups()
    instructions.append((instruction, int(number)))

next_instruction = 0

while True:
    if next_instruction in executed_instructions:
        break
    else:
        executed_instructions.append(next_instruction)

    instruction, number = instructions[next_instruction]

    if instruction == "acc":
        acumulator += number
        next_instruction += 1
    elif instruction == "jmp":
        next_instruction += number
    elif instruction == "nop":
        next_instruction += 1
    else:
        raise RuntimeError("Unknown instruction")

print(acumulator)
