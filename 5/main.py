#!/bin/bash

INPUT_FILE = './input/input.txt'

class BoardPass(object):
    def __init__(self, seat_spec):
        # TODO: Esto seguro que se puede simplificar
        start, end = 0, 127

        for mov in seat_spec[:-3]:
            pivot = start + (end-start)//2
            if mov == 'B':
                start = pivot + 1
            else:
                end = pivot

        self.row = start

        start, end = 0, 7
        for mov in seat_spec[-3:]:
            pivot = start + (end-start)//2
            if mov == 'L':
                end = pivot
            else:
                start = pivot + 1

        self.colum = start

    @property
    def id(self):
        return self.row*8 + self.colum


if __name__ == '__main__':
    f = open(INPUT_FILE)
    passes = [BoardPass(x.rstrip()) for x in f.readlines()]
    ids = [p.id for p in passes]
    print("Higest pass id is: {}".format(max(ids)))

    ids.sort()
    sit_id = None
    for i in range(ids[0], ids[-1]):
        if i not in ids and i+1 in ids and i-1 in ids:
            sit_id = i
            break

    print("Your sit has id: {}".format(sit_id))
