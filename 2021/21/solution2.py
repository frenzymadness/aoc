from itertools import product
from collections import Counter
from dataclasses import dataclass

@dataclass
class Game:
    p1: int
    p2: int
    s1: int
    s2: int
    next_plays: int

    def __hash__(self):
        return hash((self.p1, self.p2, self.s1, self.s2, self.next_plays))


with open("input.txt") as input_file:
    lines = input_file.read().splitlines()

pos = [int(lines[0].split(" ")[-1]), int(lines[1].split(" ")[-1])]

rolls = [sum(c) for c in product((1,2,3), (1,2,3), (1,2,3))]

games = Counter()
finished = Counter()

games[Game(pos[0], pos[1], 0, 0, 1)] = 1

while len(games) > 0:
    next_games = Counter()

    for game, count in games.items():
        if game.next_plays == 1:
            for value in rolls:
                new_pos = game.p1 + value
                new_pos = ((new_pos - 1) % 10) + 1
                new_score = game.s1 + new_pos
                new_game = Game(new_pos, game.p2, new_score, game.s2, 2)
                if new_score >= 21:
                    finished[new_game] += count
                else:
                    next_games[new_game] += count
        else:
            for value in rolls:
                new_pos = game.p2 + value
                new_pos = ((new_pos - 1) % 10) + 1
                new_score = game.s2 + new_pos
                new_game = Game(game.p1, new_pos, game.s1, new_score, 1)
                if new_score >= 21:
                    finished[new_game] += count
                else:
                    next_games[new_game] += count

    games = next_games.copy()

p1, p2 = 0, 0

for game, count in finished.items():
    if game.s1 >= 21:
        p1 += count
    else:
        p2 += count

print(p1, p2)
