#!/bin/bash

INPUT_FILE = './input/input.txt'

def solve_1(raw_data):
    groups = [{x for x in raw_ansers.rstrip().replace('\n', '')} for raw_ansers in raw_data.split('\n\n')]
    return sum([len(g) for g in groups])


if __name__ == '__main__':
    with open(INPUT_FILE) as f:
        raw_data = f.read()

    sol_1 = solve_1(raw_data)
    print("Total sum of yes answers is: {}".format(sol_1))
