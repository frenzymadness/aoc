width = 25
height = 6
img_len = width * height


with open("input.txt") as input_file:
    strings = [c.strip() for c in input_file.readlines()[0]]
    digits = [int(c) for c in strings if c != ""]

n_layers = len(digits) / img_len
layers = [digits[x:x+img_len] for x in range(0, len(digits), img_len)]

min_zeros = None
layer_index = 0
for i, layer in enumerate(layers):
    zeros = layer.count(0)
    if min_zeros is None or zeros < min_zeros:
        min_zeros = zeros
        layer_index = i

result = layers[layer_index].count(1) * layers[layer_index].count(2)

print(f"Minimum zeros {min_zeros} has layer number {layer_index}")
print(f"Final result is {result}")