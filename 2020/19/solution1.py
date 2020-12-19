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
            result += make_regex(rules[x])
    
    return result


with open("input.txt") as input_file:
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
