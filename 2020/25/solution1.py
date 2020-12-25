with open("input.txt") as input_file:
    card = int(input_file.readline().strip())
    door = int(input_file.readline().strip())

x = 1
y = 1

loop_size_card = 0
loop_size_door = 0

while(x != card):
    x *= 7
    x %= 20201227
    loop_size_card += 1

while(y != door):
    y *= 7
    y %= 20201227
    loop_size_door += 1

answer = 1
for i in range(0, loop_size_door):
    answer *= card
    answer %= 20201227

print(answer)

answer = 1
for i in range(0, loop_size_card):
    answer *= door
    answer %= 20201227

print(answer)
