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
    loop = False

    # import pdb; pdb.set_trace()
    while i < len(program):
        instruction = program[i]
        # Si la instruction fue ejecutada cortamos la ejecucion del programa
        if instruction[0] is True:
            loop = True
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

    return counter, loop


def update_instruction(instruction):
    if 'nop' in instruction:
        new_instruction = instruction.replace('nop', 'jmp')
    else:
        new_instruction = instruction.replace('jmp', 'nop')
    instruction = new_instruction
    return instruction




def solve_2(program):
    counter = 0

    # Esta solucion es un poco bestia pero funciona.
    for i in range(len(program)):
        copy = program[i][1]
        program[i][1] = update_instruction(program[i][1])
        program = [[False, instr[1]] for instr in program]

        counter, looped = solve_1(program)
        if looped:
            program[i][1] = copy
        else:
            break

    return counter


if __name__ == '__main__':
    program = read_program()
    counter = solve_1(program)
    print("Counter value was {}.".format(counter))

    program = read_program()
    counter = solve_2(program)
    print("Counter value was for second part was {}.".format(counter))
