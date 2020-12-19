import math

INPUT_FILE = './input/input.txt'

def apply_operation(op1, op2, operator):
    if operator == "*":
        return op1*op2
    else:
        return op1+op2

def solve_1(input_line):
    ops = []
    i = 0
    while i < len(input_line):
        value = input_line[i]
        if value == '(':
            # find matching parenthesis pos
            opening_parenthesis = 1
            closing_parenthesis = 0
            pos = i+1

            while opening_parenthesis != closing_parenthesis:
                if input_line[pos] == '(':
                    opening_parenthesis += 1
                elif input_line[pos] == ')':
                    closing_parenthesis += 1

                pos += 1

            ops.append(solve_1(input_line[i+1:pos-1]))
            i = pos
            if len(ops) == 2:
                res = apply_operation(ops[0], ops[1], operator)
                ops = [res]
            continue
        else:
            try:
                ops.append(int(value))
            except ValueError:
                operator = value

        if len(ops) == 2:
            res = apply_operation(ops[0], ops[1], operator)
            ops = [res]

        i += 1

    return res

def solve_2(input_line):
    p_res = []
    res = 0
    i = 0
    operator = '+'
    while i < len(input_line):
        value = input_line[i]

        if value.isdigit():
            res = apply_operation(res, int(value), operator)
        elif value == '+':
            operator = '+'
        elif value == '*':
            p_res.append(res)
            res = 0
        elif value == '(':
            opening_parenthesis = 1
            closing_parenthesis = 0
            pos = i+1

            while opening_parenthesis != closing_parenthesis:
                if input_line[pos] == '(':
                    opening_parenthesis += 1
                elif input_line[pos] == ')':
                    closing_parenthesis += 1

                pos += 1

            res = apply_operation(res, solve_2(input_line[i+1:pos-1]), operator)
            i = pos
            continue

        i += 1
    p_res.append(res)
    res = math.prod(p_res)

    return res

if __name__ == '__main__':
    # input_line = open(INPUT_FILE).readline()
    # input_line = '1 + 2 * 3 + 4 * 5 + 6'
    # print(solve_2(input_line.strip().replace(' ', '')))
    # input_line = '2 * 3 + (4 * 5)'
    # print(solve_2(input_line.strip().replace(' ', '')))
    # input_line = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
    # print(solve_2(input_line.strip().replace(' ', '')))
    # input_line = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
    # print(solve_2(input_line.strip().replace(' ', '')))
    # # input_line = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'
    # # print(solve_1(input_line.strip().replace(' ', '')))
    # print(solve_2(input_line.strip().replace(' ', '')))
    res = []
    for line in open(INPUT_FILE).readlines():
        res.append(solve_1(line.strip().replace(' ', '')))
    print(sum(res))

    res = []
    for line in open(INPUT_FILE).readlines():
        res.append(solve_2(line.strip().replace(' ', '')))
    print(sum(res))
