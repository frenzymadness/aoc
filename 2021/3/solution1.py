from collections import Counter

main = None

with open("input.txt") as input_file:
    for line in input_file:
        line = line.strip()
        if not main:
            main = [[] for _ in line]
        for index, char in enumerate(line):
            main[index].append(char)

gamma = ""
epsilon = ""

for possition in range(len(main)):
    c = Counter(main[possition])
    gamma_bit, epsilon_bit = c.most_common()
    gamma += gamma_bit[0]
    epsilon += epsilon_bit[0]

gamma_int = int(gamma, 2)
epsilon_int = int(epsilon, 2)

print(gamma_int * epsilon_int)
