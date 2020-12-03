from copy import deepcopy


INPUT_FILE = './input/input.txt'
trees = [list(x.rstrip()) for x in open(INPUT_FILE).readlines()]

def generate_map(trees_map, from_line):
    for i in range(from_line, len(trees_map)):
        trees_map[i] = trees_map[i] + trees[i]



def solve(x_inc, y_inc=1):
    trees_map = deepcopy(trees)
    trees_found = 0
    x = 0

    for i in range(0, len(trees_map), y_inc):
        # Comprobamos si tenemos que ampliar la linea en la que nos encontramos
        if x >= len(trees_map[i]):
            generate_map(trees_map, i)

        # Comprobamos si hay un arbol en la posicion futura
        if trees_map[i][x] == '#':
            trees_found += 1

        x = x+x_inc

    return trees_found

def solve_1():
    return solve(x_inc=3, y_inc=1)


def solve_2():
    a = solve(1,1)
    b = solve(3,1)
    c = solve(5,1)
    d = solve(7,1)
    e = solve(1,2)

    return a*b*c*d*e


if __name__ == '__main__':
    print("Solution to part 1: {} trees".format(solve_1()))
    print("Solution to part 2: {} trees".format(solve_2()))
