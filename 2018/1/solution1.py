with open("input.txt") as input_file:
    lines = input_file.readlines()

result = 0
for line in lines:
    print(line.strip(), result)
    result += int(line.strip())
print(result)
