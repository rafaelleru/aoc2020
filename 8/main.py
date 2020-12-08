import re

INPUT_FILE = './input/input.txt'

def read_program():
    with open(INPUT_FILE) as f:
        program = [[False, line.rstrip()] for line in f.readlines()]

    return program

def get_value_from_instruction(instruction):
    pattern = "((\+|-)\d+)"
    return int(re.search(pattern, instruction).group())

def solve_1(program):
    counter = 0
    i = 0

    # import pdb; pdb.set_trace()
    while True:
        instruction = program[i]
        # Si la instruction fue ejecutada cortamos la ejecucion del programa
        if instruction[0] is True:
            break
        else:
            instr = instruction[1]  # Para no referenciar todo el tiempo el segundo elemento de la tupla
            instruction[0] = True
            if 'nop' in instr:
                i += 1
                continue
            else:
                value = get_value_from_instruction(instr)
                if 'acc' in instr:
                    counter += value
                    i += 1
                elif 'jmp' in instr:
                    i += value

    return counter


if __name__ == '__main__':
    program = read_program()
    counter = solve_1(program)
    print("Counter value was {}.".format(counter))
