with open("input.txt") as input_file:
    numbers = [int(n) for n in input_file.read().strip().split(",")]

memory = {}
turn = 0

for n in numbers:
    turn += 1
    memory[n] = (turn,)
    last = n

while True:
    turn += 1
    if len(memory[last]) == 1:
        last = 0
    else:
        last = memory[last][-1] - memory[last][-2]

    try:
        memory[last] = (memory[last][-1], turn)
    except KeyError:
        memory[last] = (turn,)

    if turn == 30000000:
        print(last)
        break
