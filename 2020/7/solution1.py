from collections import defaultdict
import re

gold = set()
contained_in = defaultdict(set)


def traverse(color):
    for outer_color in contained_in[color]:
        gold.add(outer_color)
        traverse(outer_color)


def main():
    with open("input.txt") as input_file:
        lines = input_file.readlines()

    for line in lines:
        outer_color = re.match(r"(\w+ \w+) bags contain", line.strip()).groups()[0]

        for contains in re.findall(r"(\d+ \w+ \w+) bags?", line.strip()):
            _, *inner_color = contains.split()
            inner_color = " ".join(inner_color)
            contained_in[inner_color].add(outer_color)

    traverse("shiny gold")
    print(len(gold))


main()
