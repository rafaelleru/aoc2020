import re
f = open('./input/input.txt')
lines = f.readlines()

def process_line(line):
    policy, password = line.split(":")

    # Quitamos el espacio de la password
    password = password.lstrip()

    char_needed = policy[-1] # el ultimo caracter es el que tiene que aparecer en la pwd
    policy = policy.split(' ')[0] # esto me deja un string 1-3

    # convert policy to tuple
    splitted = policy.split('-')
    policy = (int(splitted[0]), int(splitted[1]))

    return policy, char_needed, password


def valid_part_1(policy, char_needed, password):
    if password.count(char_needed) >= policy[0] and password.count(char_needed) <= policy[1]:
        return 1
    else:
        return 0

def valid_part_2(policy, char_needed, password):
    if password[policy[0]-1] == char_needed and not password[policy[1]-1] == char_needed:
        return 1
    elif not password[policy[0]-1] == char_needed and password[policy[1]-1] == char_needed:
        return 1
    else:
        return 0


def solve1():
    valid_passwords = 0
    for line in lines:
        policy, char_needed, password = process_line(line)
        valid_passwords += valid_part_1(policy, char_needed, password)

    return valid_passwords

def solve2():
    valid_passwords = 0
    for line in lines:
        policy, char_needed, password = process_line(line)
        valid_passwords += valid_part_2(policy, char_needed, password)

    return valid_passwords

if __name__ == '__main__':
    valid_passwords = solve1()
    print("Number of valid passwords in input file: " + str(valid_passwords))

    valid_passwords_2 = solve2()
    print("Number of valid passwords in input file (2nd part): " + str(valid_passwords_2))
