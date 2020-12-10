from copy import deepcopy
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



if __name__ == '__main__':
    with open(INPUT_FILE) as f:
        adapters_list = [int(x.strip()) for x in f.readlines()]
        adapters_list.sort(reverse=True)

    sol1 = solve_1(deepcopy(adapters_list))
    print("solution to part 1 is: {}".format(sol1))
