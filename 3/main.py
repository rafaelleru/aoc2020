from copy import deepcopy


INPUT_FILE = './input/input.txt'
trees = [list(x.rstrip()) for x in open(INPUT_FILE).readlines()]

def generate_map(trees_map, from_line):
    for i in range(from_line, len(trees_map)):
        trees_map[i] = trees_map[i] + trees[i]



def solve_1():
    trees_map = deepcopy(trees)
    trees_found = 0
    x = 0

    for i in range(len(trees_map)):
        # Comprobamos si tenemos que ampliar la linea en la que nos encontramos
        if x >= len(trees_map[i]):
            generate_map(trees_map, i)

        # Comprobamos si hay un arbol en la posicion futura
        if trees_map[i][x] == '#':
            trees_found += 1

        x = x+3

    return trees_found


if __name__ == '__main__':
    print("Solution to part 1: {} trees".format(solve_1()))
