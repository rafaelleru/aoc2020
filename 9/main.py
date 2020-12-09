from itertools import permutations
from itertools import combinations_with_replacement

INPUT_FILE = './input/input.txt'

def solve_1(code, preamble):
    start, end = 0, preamble
    i = preamble  # Empezamos en el primer numero despues del preambulo

    posibles = [c[0]+c[1] for c in permutations(code[start:end], 2)]

    while i < len(code):
        if code[i] in posibles:
            start += 1
            end += 1
            i += 1
            posibles = [c[0]+c[1] for c in permutations(code[start:end], 2)]
        else:
            return code[i]

    return None


if __name__ == '__main__':
    with open(INPUT_FILE) as f:
        input_code = [int(x.strip()) for x in f.readlines()]

    print(solve_1(input_code, 25))
