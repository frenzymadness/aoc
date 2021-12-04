from collections import defaultdict


def check_winner(cards):
    for card_index, card in cards.items():
        for index in range(5):
            complete_line = all([x[1] for x in card[index]])
            complete_column = all([card[x][index][1] for x in range(5)])
            if complete_line or complete_column:
                return card_index


with open("input.txt") as input_file:
    lines = input_file.readlines()

drawn = [int(n) for n in lines[0].strip().split(",")]
del lines[0:2]

cards = defaultdict(list)
card = 0

# Card prep
for line in lines:
    line = line.strip()
    if not line:
        card += 1
        continue
    card_line = [[int(n), False] for n in line.split()]
    cards[card].append(card_line)

winners = []

# Final game
for n in drawn:
    # Find all cells to cross
    for card in cards.values():
        for line in card:
            try:
                index = line.index([n, False])
                line[index][1] = True
            except ValueError:
                pass

    # Remove all the winners from the game
    # but save their cards and last drawn number first
    while (winner := check_winner(cards)) is not None:
        winners.append((cards[winner], n))
        del cards[winner]

sum = 0
card, last_drawn = winners[-1]
for line in card:
    for n, drawn in line:
        if not drawn:
            sum += n

print(sum * last_drawn)
