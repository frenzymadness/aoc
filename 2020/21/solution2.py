from collections import defaultdict

recipes = []
allergen_in_recipes = defaultdict(set)
possible_allergens = defaultdict(set)
dangerous_ingredients = []


def contains_allergen(ingredient):
    only_one = ""
    for allergen in possible_allergens[ingredient]:
        for recipe in allergen_in_recipes[allergen]:
            if len(allergen_in_recipes[allergen]) == 1:
                only_one = allergen
                break
            if ingredient not in recipes[recipe]:
                break
        else:
            return allergen

    return only_one if only_one else None


with open("input.txt") as input_file:
    for index, line in enumerate(input_file):
        parts = line.strip().rstrip(")").replace(",", "").split("(contains")
        ingredients = set(parts[0].strip().split())
        recipes.append(ingredients)
        allergens = set(parts[1].strip().split())
        for allergen in allergens:
            allergen_in_recipes[allergen].add(index)
            for ingredient in ingredients:
                possible_allergens[ingredient].add(allergen)

for ingredient in possible_allergens:
    allergen = contains_allergen(ingredient)
    if allergen is not None:
        dangerous_ingredients.append((allergen, ingredient))

print(",".join(i for a, i in sorted(dangerous_ingredients)))
