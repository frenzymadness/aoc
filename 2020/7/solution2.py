from collections import defaultdict
import re

gold = set()
contains = defaultdict(set)


def traverse(color):  
    result = 0
    for c, inner_color in contains[color]:
        result += c * traverse(inner_color) + c
    return result


def main():
    with open("input.txt") as input_file:
        lines = input_file.readlines()

    for line in lines:
        outer_color = re.match(r"(\w+ \w+) bags contain", line.strip()).groups()[0]

        for bags in re.findall(r"(\d+ \w+ \w+) bags?", line.strip()):
            count, *inner_color = bags.split()
            if count == "no":
                contains[outer_color].add(tuple())
            else:
                count = int(count)
                inner_color = " ".join(inner_color)
                contains[outer_color].add((count, inner_color))

    print(traverse("shiny gold"))


main()
