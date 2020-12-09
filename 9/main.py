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

def solve_2(code, invalid_number):
    for set_size in range(2, len(code)):

        for i in range(len(code)):
            if i+set_size > len(code):
                break
            else:
                if sum(code[i:i+set_size]) == invalid_number:
                    print(code[i:i+set_size])
                    return max(code[i:i+set_size]) + min(code[i:i+set_size])

if __name__ == '__main__':
    with open(INPUT_FILE) as f:
        input_code = [int(x.strip()) for x in f.readlines()]

    invalid_number = solve_1(input_code, 25)
    print("Solution for part 1 is: {}".format(invalid_number))

    print(solve_2(input_code, invalid_number))

