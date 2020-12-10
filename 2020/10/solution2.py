from functools import lru_cache

with open("input.txt") as input_file:
    adapters = [int(n.strip()) for n in input_file.readlines()]

builtin = max(adapters) + 3
adapters = [0] + sorted(adapters) + [builtin]

@lru_cache
def traverse(start):
    count = 0
    if start == len(adapters) - 1:
        return 1
    else:
        for x in range(start+1, start+4):
            try: 
                if adapters[x] - adapters[start] <= 3:
                    count += traverse(x)
                else: 
                    break 
            except IndexError: 
                break
    
    return count

print(traverse(0))
