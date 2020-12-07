import re
from pathlib import Path
from collections import defaultdict, namedtuple
from math import ceil
from queue import Queue

Ingredience = namedtuple("Ingredience", ["name", "amount"])
Recipe = namedtuple("Recipe", ["batch", "ingrediens"])

with open(Path(__file__).parent / "input.txt") as input_file:
    lines = input_file.readlines()

recipes = {}

for line in lines:
    input, output = line.split(" => ")
    ingredients = []
    for input in re.findall(r"\d+ \w+", input.strip()):
        amount, name = input.split()
        ingredients.append(Ingredience(name, int(amount)))
    amount, name = output.split()
    recipes[name] = Recipe(int(amount), ingredients)

supply = defaultdict(int)
orders = Queue()
orders.put(Ingredience("FUEL", 1))

ore = 0

while not orders.empty():
    order = orders.get()

    if order.name == "ORE":
        ore += order.amount
    elif order.amount <= supply[order.name]:
        supply[order.name] -= order.amount
    else:
        amount_needed = order.amount - supply[order.name]
        recipe = recipes[order.name]
        batches = ceil(amount_needed / recipe.batch)
        for ingredient in recipe.ingrediens:
            orders.put(Ingredience(ingredient.name, ingredient.amount * batches))
        leftover_amount = batches * recipe.batch - amount_needed
        supply[order.name] = leftover_amount

print(ore)
