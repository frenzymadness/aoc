width = 25
height = 6
img_len = width * height

with open("input.txt") as input_file:
    strings = [c.strip() for c in input_file.readlines()[0]]
    digits = [int(c) for c in strings if c != ""]

n_layers = len(digits) / img_len
layers = [digits[x:x+img_len] for x in range(0, len(digits), img_len)]

for i in range(0, img_len):
    for layer in layers:
        if layer[i] == 2:
            continue
        else:
            print(layer[i], end="")
            break
    if (i+1) % width == 0:
        print()
    #print("-- ", i+1, width, i+1%width)
