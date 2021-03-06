from copy import deepcopy

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


def solve_2(p1_deck, p2_deck):
    winner = False
    previous_rounds = set()
    round = 0

    while not winner:
        round += 1

        if (tuple(p1_deck), tuple(p2_deck)) in previous_rounds:
            return 1
        else:

            if p1_deck == []:
                return 2
            elif p2_deck == []:
                return 1
            else:
                previous_rounds.add((tuple(p1_deck), tuple(p2_deck)))
                d1_card = p1_deck.pop(0)
                d2_card = p2_deck.pop(0)

                if len(p1_deck) >= d1_card and len(p2_deck) >= d2_card:
                    d1_copy = deepcopy(p1_deck)[:d1_card]
                    d2_copy = deepcopy(p2_deck)[:d2_card]
                    round_winner = solve_2(d1_copy, d2_copy)
                    # __import__('pdb').set_trace()
                    if round_winner == 1:
                        p1_deck.append(d1_card)
                        p1_deck.append(d2_card)
                    else:
                        p2_deck.append(d2_card)
                        p2_deck.append(d1_card)
                else:
                    round_winner = 1 if d1_card > d2_card else 0

                    if round_winner == 1:
                        p1_deck.append(d1_card)
                        p1_deck.append(d2_card)
                    else:
                        p2_deck.append(d2_card)
                        p2_deck.append(d1_card)

    return winner



if __name__ == "__main__":

    # p1_deck = [9, 2, 6, 3, 1]
    # p2_deck = [5, 8, 4, 7, 10]
    p1_deck, p2_deck = parse_input()

    solve_1(p1_deck, p2_deck)

    # p1_deck = [9, 2, 6, 3, 1]
    # p2_deck = [5, 8, 4, 7, 10]
    p1_deck, p2_deck = parse_input()
    solve_2(p1_deck, p2_deck)

    score = 0
    for i, value in enumerate(p2_deck):
        score += value * (len(p2_deck) - i)

    print(score)
