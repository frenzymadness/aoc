from collections import Counter

with open("input.txt") as input_file:
    main = ["".join(chars) for chars in zip(*input_file.readlines())]
    del main[-1]

gamma, epsilon = "", ""

for possition in range(len(main)):
    c = Counter(main[possition])
    (gamma_bit, _), (epsilon_bit, _) = c.most_common()
    gamma += gamma_bit
    epsilon += epsilon_bit

gamma_int, epsilon_int = int(gamma, 2), int(epsilon, 2)

print(gamma_int * epsilon_int)
