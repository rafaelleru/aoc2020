#!/bin/bash
from collections import defaultdict

INPUT_FILE = './input/input.txt'

def solve_1(raw_data):
    groups = [{x for x in raw_ansers.rstrip().replace('\n', '')} for raw_ansers in raw_data.split('\n\n')]
    return sum([len(g) for g in groups])

def solve_2(raw_data):
    count = 0
    for group_answers in raw_data.split('\n\n'):
        common_answers = defaultdict(int)
        for indv in group_answers.rstrip().split('\n'):
            # Iteramos cada pregunta (caracter) de cada lista de respuestas (linea en el input)
            for answer in indv:
                # Si el individuo ha respondido yes a la pregunta 'answer' sumamos uno a su contador
                common_answers[answer] = common_answers[answer] + 1

        # Nos quedamos con las respuestas cuyo contador coincida con el tamanio del grupo
        for k, v in common_answers.items():
            if v == len(group_answers.rstrip().split('\n')):
                count += 1

    return count


if __name__ == '__main__':
    with open(INPUT_FILE) as f:
        raw_data = f.read()

    sol_1 = solve_1(raw_data)
    print("Total sum of yes answers is: {}".format(sol_1))
    sol_2 = solve_2(raw_data)
    print("Total of yes answers common per group is: {}".format(sol_2))
