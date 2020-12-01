from int_comp import IntComputer
import os

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
        self.ball_x = None
        self.paddle_x = None
    
    def step(self):
        x = self.comp.run()
        y = self.comp.run()
        tile = self.comp.run()

        if None in [x, y, tile]:
            return False

        if x == -1 and y == 0:
            print("SCORE: ", tile)
            return True

        if x > self.max_x:
            self.max_x = x + 1

        if y > self.max_y:
            self.max_y = y + 1
        
        self.map[(x, y)] = SHAPES[tile]

        if tile == 4:
            self.ball_x = x
        
        if tile == 3:
            self.paddle_x = x

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
    #g.draw()
    # if "-" in g.map.values():
    #     g.comp.input.append(int(input("-1, 0, 1")))
    # os.system("clear")
    if g.paddle_x is not None and g.ball_x is not None:
        if g.paddle_x < g.ball_x:
            g.comp.input = [1]
        elif g.paddle_x > g.ball_x:
            g.comp.input = [-1]
        else:
            g.comp.input = [0]
        print(g.ball_x, g.paddle_x)

# print(sum([1 for v in g.map.values() if v == "@"]))
