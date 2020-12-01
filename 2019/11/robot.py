from int_comp import IntComputer

DIRECTIONS = {
    "up": (0, 1),
    "left": (-1, 0),
    "down": (0, -1),
    "right": (1, 0)
}

CHANGE_LEFT = ["up", "left", "down", "right", "up"]
CHANGE_RIGHT = ["up", "right", "down", "left", "up"]

class Robot:
    def __init__(self, pos=(50, 50), dir="up"):
        self.position = pos
        self.direction = dir
        self.comp = IntComputer("input", [])
        self.whites = []
        self.painted = set()
    
    def step(self):
        print(self.position)
        if self.position in self.whites:
            print("reading white")
            self.comp.input = [1]
        else:
            print("reading black")
            self.comp.input = [0]
        
        color = self.comp.run()
        if color is None:
            print("STOP", len(self.painted))
            return False
        if color == 0:
            # black
            print("painting black")
            self.painted.add(self.position)
            if self.position in self.whites:
                self.whites.remove(self.position)
        elif color == 1:
            # white
            print("painting white")
            self.whites.append(self.position)
            self.painted.add(self.position)
        
        turn = self.comp.run()
        if turn == 0:
            # left
            print("turning left")
            self.direction = CHANGE_LEFT[CHANGE_LEFT.index(self.direction) + 1]
        elif turn == 1:
            # right
            print("turning right")
            self.direction = CHANGE_RIGHT[CHANGE_RIGHT.index(self.direction) + 1]
        
        move_x, move_y = DIRECTIONS[self.direction]
        self.position = self.position[0] + move_x, self.position[1] + move_y

        return True

    def draw(self):
        size = 100
        for y in range(size, 0, -1):
            for x in range(size):
                if (x, y) in self.whites:
                    print("#", end="")
                elif (x, y) == self.position:
                    print("X", end="")
                else:
                    print(".", end="")
            print()
        print("="*20)

if __name__ == "__main__":
    r = Robot()
    end = True
    while end:
    #for _ in range(10):
        r.draw()
        end = r.step()
