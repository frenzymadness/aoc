from dataclasses import dataclass


@dataclass
class Submarine:
    horizontal = 0
    depth = 0

    def forward(self, x):
        self.horizontal += x
    
    def down(self, x):
        self.depth += x
    
    def up(self, x):
        self.depth -= x

sub = Submarine()

with open("input.txt") as input_file:
    for line in input_file:
        command, x = line.split()
        x = int(x)
        getattr(sub, command)(x)
    
print(sub.horizontal * sub.depth)
