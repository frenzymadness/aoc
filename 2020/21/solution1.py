from collections import defaultdict

recipes = []
allergen_in_recipes = defaultdict(set)
possible_allergens = defaultdict(set)
safe_ingredients = []


def is_safe(ingredient):
    for allergen in possible_allergens[ingredient]:
        if len(allergen_in_recipes[allergen]) == 1:
            return False

        for recipe in allergen_in_recipes[allergen]:
            if ingredient not in recipes[recipe]:
                break
        else:
            return False

    return True


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
    if is_safe(ingredient):
        safe_ingredients.append(ingredient)

final_count = 0

for ingredient in safe_ingredients:
    for recipe in recipes:
        final_count += ingredient in recipe

print(final_count)
