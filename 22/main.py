INPUT_FILE = './input/input.txt'

def parse_input():
    p1_deck = []
    p2_deck = []
    adding = []

    with open(INPUT_FILE) as f:
        for l in f.readlines():
            if l.strip() == '':
                continue

            if 'Player 1' in l:
                adding = p1_deck
            elif 'Player 2' in l:
                p1_deck = adding
                adding = p2_deck
            else:
                adding.append(int(l.strip()))

        p2_deck = adding

    return p1_deck, p2_deck


def solve_1(p1_deck, p2_deck):
    winner = False
    score = 0

    while not winner:
        d1_card = p1_deck.pop(0)
        d2_card = p2_deck.pop(0)

        if d1_card > d2_card:
            p1_deck.append(d1_card)
            p1_deck.append(d2_card)
        else:
            p2_deck.append(d2_card)
            p2_deck.append(d1_card)

        if p1_deck == []:
            winner = p2_deck
        elif p2_deck == []:
            winner = p1_deck

    for i, value in enumerate(winner):
        score += value * (len(winner) - i)

    print(score)


if __name__ == "__main__":
    # p1_deck = [9, 2, 6, 3, 1]
    # p2_deck = [5, 8, 4, 7, 10]

    p1_deck, p2_deck = parse_input()

    solve_1(p1_deck, p2_deck)
