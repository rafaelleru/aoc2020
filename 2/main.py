import re
f = open('./input/input.txt')

def process_line(line):
    policy, password = line.split(":")

    # Quitamos el espacio de la password
    password = password.lstrip()

    char_needed = policy[-1] # el ultimo caracter es el que tiene que aparecer en la pwd
    policy = policy.split(' ')[0] # esto me deja un string 1-3

    # convert policy to tuple
    splitted = policy.split('-')
    policy = (int(splitted[0]), int(splitted[1]))

    if password.count(char_needed) >= policy[0] and password.count(char_needed) <= policy[1]:
        return 1
    else:
        return 0



def solve():
    valid_passwords = 0
    for line in f.readlines():
        valid_passwords += process_line(line)

    return valid_passwords

if __name__ == '__main__':
    valid_passwords = solve()
    print("Number of valid passwords in input file: " + str(valid_passwords))
