import re

rules = {}
messages = []

def make_regex(rule):
    if rule.startswith('"'):
        return rule.replace('"', '')
    
    result = ""

    if "|" in rule:
        result += "("
        result += "|".join([make_regex(x) for x in rule.split(" | ")])
        result += ")"
    else:
        for x in rule.split():
            if x == "8":
                result += f"({make_regex('42')})+"
            elif x == "11":
                # Very ugly hack with recursion limit
                subres = []
                r42 = make_regex('42')
                r31 = make_regex('31')
                for i in range(1, 6):
                    subres.append(r42*i+r31*i)
                result += "(" + "|".join(subres)  + ")"
            else:
                result += make_regex(rules[x])

    return result


with open("input2.txt") as input_file:
    for line in input_file:
        if line.strip() == "":
            break
        n, rule = re.match(r"(\d+): (.*)$", line.strip()).groups()
        rules[n] = rule.strip()
    
    for line in input_file:
        messages.append(line.strip())
    
regex = make_regex(rules["0"])

count = 0
for message in messages:
    m = re.match(regex+"$", message)
    if m is not None:
        count += 1

print(count)
