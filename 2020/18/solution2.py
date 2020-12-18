import re
from operator import add, mul

operators = {"+": add, "*": mul}

with open("input.txt") as input_file:
    expressions = input_file.readlines()

def parse_par(exp):
    result = []
    stack = [] 
    for i, c in enumerate(exp): 
        if c == '(': 
            stack.append(i) 
        elif c == ')' and stack: 
            start = stack.pop() 
            result.append((len(stack), exp[start + 1: i]))
    return result

def eval_exp(exp):
    while m := re.search(r"(\d+) \+ (\d+)", exp):
        a, b = m.groups()
        res = int(a) + int(b)
        exp = exp[:m.start()] + str(res) + exp[m.end():]

    while m := re.search(r"(\d+) \* (\d+)", exp):
        a, b = m.groups()
        res = int(a) * int(b)
        exp = exp[:m.start()] + str(res) + exp[m.end():]

    return exp

sum = 0

for exp in expressions:
    while pars := sorted(parse_par(exp)):
        depth, subexp = pars.pop()
        subres = eval_exp(subexp)
        exp = exp.replace(f"({subexp})", str(subres))

    sum += int(eval_exp(exp))

print(sum)
