from itertools import permutations
from copy import deepcopy
from collections import Counter

INPUT_FILE = './input/input.txt'


def solve_1(adapters_list):
    one_diff = 0
    three_diff = 1  # Hay una diferencia de 3 entre el ultimo adaptador y el dispositivvo

    current_jolts = 0

    while adapters_list:
        adapter = adapters_list.pop()

        if adapter == current_jolts:
            continue
        if adapter-current_jolts == 1:
            one_diff += 1
        elif adapter-current_jolts  == 3:
            three_diff += 1

        current_jolts = adapter

    return one_diff*three_diff


def solve_2(adapters_list):
    c = Counter({0:1})

    for x in sorted([0] + adapters_list):
        c[x+1] += c[x]
        c[x+2] += c[x]
        c[x+3] += c[x]

    return c[adapters_list[0] + 3]


if __name__ == '__main__':
    with open(INPUT_FILE) as f:
        adapters_list = [int(x.strip()) for x in f.readlines()]
        adapters_list.sort(reverse=True)

    sol1 = solve_1(deepcopy(adapters_list))
    print("solution to part 1 is: {}".format(sol1))
    print("Solution to part 2 is: {}".format(solve_2(adapters_list)))
