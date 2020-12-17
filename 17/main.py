from copy import deepcopy
from collections import defaultdict
from itertools import combinations_with_replacement
from itertools import product

INPUT_FILE = './input/input.txt'

ACTIVE = '#'
INACTIVE = '.'

grid = defaultdict(lambda: '.')
x_boundary = [0, 7]
y_boundary = [0, 7]
z_boundary = [0, 0]

def parse_input():
    state = []
    with open(INPUT_FILE) as f:
        for i, line in enumerate(f.readlines()):
            for j, value in enumerate(line[:-1]):
                grid[i, j, 0] = value

    return grid

def check_neighbors(grid, coord):
    n_enabled = 0
    for x in range(coord[0]-1, coord[0]+2):
        for y in range(coord[1]-1, coord[1]+2):
            for z in range(coord[2]-1, coord[2]+2):
                if (x, y, z) == coord:
                    continue
                else:
                    n_enabled += grid[x, y, z] == ACTIVE
    return n_enabled


def iterate_state(grid):
    coords = []

    # Seguro que hay una forma mas pythonic para hacer esto
    for x in range(x_boundary[0]-1, x_boundary[1]+2):
        for y in range(y_boundary[0] - 1, y_boundary[1]+2):
            for z in range(z_boundary[0] - 1, z_boundary[1]+2):
                coords.append((x, y, z))

    x_boundary[0] = x_boundary[0] - 1; x_boundary[1] = x_boundary[1] + 2
    y_boundary[0] = y_boundary[0] - 1; y_boundary[1] = y_boundary[1] + 2
    z_boundary[0] = z_boundary[0] - 1; z_boundary[1] = z_boundary[1] + 1

    grid_copy = deepcopy(grid)
    for coord in coords:
        n = check_neighbors(grid_copy, coord)
        if grid[coord] == '#':
            if n ==2 or n ==3:
                continue
            else:
                grid[coord] = '.'
        else:
            if n == 3:
                grid[coord] = '#'

    new = defaultdict(lambda: '.',{k:v for k, v in grid.items() if v == '#'})
    return new

def iterate_state_2(grid):
    coords = []

    # Seguro que hay una forma mas pythonic para hacer esto
    for x in range(x_boundary[0]-1, x_boundary[1]+2):
        for y in range(y_boundary[0] - 1, y_boundary[1]+2):
            for z in range(z_boundary[0] - 1, z_boundary[1]+2):
                coords.append((x, y, z))

    x_boundary[0] = x_boundary[0] - 1; x_boundary[1] = x_boundary[1] + 2
    y_boundary[0] = y_boundary[0] - 1; y_boundary[1] = y_boundary[1] + 2
    z_boundary[0] = z_boundary[0] - 1; z_boundary[1] = z_boundary[1] + 1

    grid_copy = deepcopy(grid)
    for coord in coords:
        n = check_neighbors(grid_copy, coord)
        if grid[coord] == '#':
            if n ==2 or n ==3:
                continue
            else:
                grid[coord] = '.'
        else:
            if n == 3:
                grid[coord] = '#'

    new = defaultdict(lambda: '.',{k:v for k, v in grid.items() if v == '#'})
    return new


if __name__ == '__main__':
    grid = parse_input()
    for _ in range(6):
        grid = iterate_state(grid)
    print(list(grid.values()).count('#'))
