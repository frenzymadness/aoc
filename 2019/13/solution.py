from int_comp import IntComputer

SHAPES = {
    0: ".",
    1: "#",
    2: "@",
    3: "-",
    4: "o"
}

class Game:
    def __init__(self):
        self.comp = IntComputer("input", [])
        self.map = {}
        self.max_x = 0
        self.max_y = 0
    
    def step(self):
        x = self.comp.run()
        y = self.comp.run()
        tile = self.comp.run()

        if None in [x, y, tile]:
            return False

        if x > self.max_x:
            self.max_x = x + 1

        if y > self.max_y:
            self.max_y = y + 1
        
        self.map[(x, y)] = SHAPES[tile]

        return True

    def draw(self):
        for y in range(self.max_y):
            for x in range(self.max_x):
                if (x, y) in self.map:
                    print(self.map[(x, y)], end="")
                else:
                    print(" ", end="")
            print()

g = Game()
while g.step():
    g.draw()

print(sum([1 for v in g.map.values() if v == "@"]))
