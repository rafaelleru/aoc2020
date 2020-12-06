#!/bin/bash

INPUT_FILE = './input/input.txt'

class GroupAnswers():
    def __init__(self, raw_data):
        self.unique_answers = {x for x in raw_data}

    @property
    def yes_count(self):
        return len(self.unique_answers)


def solve_1():
    with open(INPUT_FILE) as f:
        raw_data = f.read()
        groups = [GroupAnswers(x.rstrip().replace('\n', '')) for x in raw_data.split('\n\n')]

    return sum([g.yes_count for g in groups])


if __name__ == '__main__':
    sol_1 = solve_1()
    print("Total sum of yes answers is: {}".format(sol_1))
