
with open("input.txt") as input_file:
# with open("test_input.txt") as input_file:
# with open("test_input2.txt") as input_file:
    adapters = [int(n.strip()) for n in input_file.readlines()]

builtin = max(adapters) + 3
adapters = [0] + sorted(adapters) + [builtin]


def is_valid_combination(adapters):
    for index, adapter in enumerate(adapters):
        try:
            diff = adapters[index+1] - adapter
            if diff > 3:
                return False
        except IndexError:
            break
    return True


def combinations(iterable, r):
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    result = []
    for i in indices:
        result.append(pool[i])
        s = set(result)
        if s in forbidden_combos:
            break
        for fc in forbidden_combos:
            if s.issuperset(fc):
                break
        else:
            continue
        break
    else:
        yield result
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        result = []
        for i in indices:
            result.append(pool[i])
            s = set(result)
            if s in forbidden_combos:
               break
            for fc in forbidden_combos:
                if s.issuperset(fc):
                    break
            else:
                continue
            break
        else:
            yield result


valid_combinations = 0

if is_valid_combination(adapters):
    valid_combinations += 1

removable_indexes = []
forbidden_combos = []

for index in range(1, len(adapters)-1):
    new = list(adapters)
    del new[index]
    if is_valid_combination(new):
        removable_indexes.append(index)

print(adapters)
print(removable_indexes)

for l in range(1, len(removable_indexes)+1):
    print("will be deleting combinations with length", l)
    diff = max(adapters) - min(adapters)
    if diff / (len(adapters) - l) > 3:
        print("reached max len", l)
        break

    for c in combinations(removable_indexes, l):
        new_list = list(adapters)
        for i in sorted(c, reverse=True):
            del new_list[i]
        if is_valid_combination(new_list):
            valid_combinations += 1
        else:
            forbidden_combos.append(set(c))

print(valid_combinations)
