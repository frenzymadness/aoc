class Package:
    def __init__(self, binary_input):
        self.bin = binary_input
        self.version = int(self.bin[:3], 2)
        self.type = int(self.bin[3:6], 2)
        if self.type == 4:  # Literal value
            groups = []
            index = 6
            while True:
                groups.append(self.bin[index+1:index+5])
                if self.bin[index] == "0":
                    break
                index += 5
            self.value = int("".join(groups), 2)
            self.last_bit_index = index + 4
        else:  # Operators
            self.subpackages = []
            self.length_type = self.bin[6]
            if self.length_type == "0":
                self.subpackages_bits = int(self.bin[7:22], 2)
                while True:
                    starts_from = 22 if not self.subpackages else 22 + bits_count
                    self.subpackages.append(Package(self.bin[starts_from:]))
                    bits_count = sum(p.last_bit_index+1 for p in self.subpackages)
                    if bits_count == self.subpackages_bits:
                        break
                self.last_bit_index = 22 + bits_count - 1
            else:
                self.subpackages_count = int(self.bin[7:18], 2)
                for _ in range(self.subpackages_count):
                    starts_from = 18 if not self.subpackages else 18 + bits_count
                    self.subpackages.append(Package(self.bin[starts_from:]))
                    bits_count = sum(p.last_bit_index+1 for p in self.subpackages)
                self.last_bit_index = 18 + bits_count - 1

    def __repr__(self):
        base = f"{self.version=}, {self.type=}"
        if self.type == 4:
            return "LITERAL " + base + f", {self.value=}"
        else:
            return "OPERATOR " + base + f", {self.length_type}"
    
    def __str__(self):
        return self.__repr__()

def print_tree(package, indent=0):
    print(" " * indent, package)
    for subpackage in getattr(package, "subpackages", ""):
        print_tree(subpackage, indent+2)

def calculate_version_sum(package):
    sum = package.version
    for subpackage in getattr(package, "subpackages", ""):
        sum += calculate_version_sum(subpackage)
    return sum

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

for line in lines:
    binary_input = bin(int(line, 16))[2:].zfill(len(line)*4)
    p = Package(binary_input)
    print_tree(p)
    print(calculate_version_sum(p))
