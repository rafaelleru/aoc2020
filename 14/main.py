import itertools


INPUT_FILE = './input/input.txt'


def solve_1(program):
    mem = {}
    mask = ''

    for instr in program:
        if 'mask' in instr:
            mask = instr.split('=')[1].strip()
        else:
            pos, value = instr.split('=')
            mem_pos = int(pos.replace('mem[', '').replace(']', '').strip())
            value = int(value.strip())
            bin_value = list(format(value, 'b').zfill(36))

            for i, mask_value in enumerate(mask):
                if mask_value != 'X':
                    bin_value[i] = mask_value

            mem[pos] = int(''.join(bin_value), 2)

    print(sum(mem.values()))

def solve_2(program):
    mem = {}
    mask = ''

    for instr in program:
        if 'mask' in instr:
            mask = instr.split('=')[1].strip()
        else:
            pos, value = instr.split('=')
            mem_pos = int(pos.replace('mem[', '').replace(']', '').strip())
            value = int(value.strip())
            bin_value = list(format(mem_pos, 'b').zfill(36))

            possible_mem_positions = []

            for i, mask_value in enumerate(mask):
                if mask_value == '0':
                    continue
                elif mask_value == '1':
                    bin_value[i] = mask_value
                elif mask_value == 'X':
                    bin_value[i] = '{}'


            possible_mem_positions = [''.join(bin_value).format(*i) for i in itertools.product([1,0], repeat=mask.count('X'))]

            for pmem in possible_mem_positions:
                mem[int(''.join(pmem), 2)] = value

    print(sum(mem.values()))


if __name__ == '__main__':
    with open(INPUT_FILE) as f:
        program = f.readlines()

    solve_1(program)
    solve_2(program)

