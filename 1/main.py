from itertools import combinations

INPUT_FILE = './input/input.txt'

data = [int(x) for x in open(INPUT_FILE).read().splitlines()]

def part1(comb_size):
    # Generamos las combinaciones de los datos de entrada
    comb = combinations(data, comb_size)

    for candidate in comb:
        candidate = list(candidate)
        if sum(candidate) == 2020:
            break

    result = 1
    for x in candidate:
        result = result * x

    return result



if __name__ == '__main__':
    print("Solution for part 1 is: " + str(part1(2)))
    print("Solution for part 2 is: " + str(part1(3)))
