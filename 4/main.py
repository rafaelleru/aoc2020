import re

INPUT_FILE = './input/input.txt'

validator = {
    'byr' : '(19(2|3|4|5|6|7|8|9|0)\d|200(0|1|2))',
    'iyr' : '20(1|2)\d',
    'eyr' : '20(2|3)\d',
    'hgt' : '(1(5|6|7|8|9)[0-9]cm|(5|6|7)(0|1|2|3|4|5|6)in)',
    'hcl' : '\#([a-f]|[0-9]){6}',
    'ecl' : '(amb|blu|brn|gry|grn|hzl|oth)',
    'pid' : '^[0-9]{9}$'
}

def read_passwords():
    lines = open(INPUT_FILE).readlines()
    passports = []
    passport = ''

    for l in lines:
        if l != '\n':
            passport += l.replace('\n', ' ')
        else:
            passports.append(passport)
            passport = ''

    passports.append(passport)

    parsed_passports = []
    for p in passports:
        passport = {}
        content = p.rstrip().split(' ')
        for info in content:
            k, v = info.split(':')
            passport[k] = v

        parsed_passports.append(passport)

    return parsed_passports

def valid_passport(passport, required_fields):
    return all(field in passport for field in required_fields)

def solve1(passports):
    return [valid_passport(p, {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}) for p in passports]

def valid_passport_2(passport):
    valid  = True
    for k in passport.keys():
        if k == 'cid':
            continue
        if not re.match(validator[k], passport[k]):
            valid = False
            break

    return valid


def solve2(passports, valid_passports):
    goods = []
    for i, valid in enumerate(valid_passports):
        if valid:
            goods.append(valid_passport_2(passports[i]))
    return goods

if __name__ == '__main__':
    passports = read_passwords()
    valid_1 = solve1(passports)
    print("Solution for part 1 is: {}".format(valid_1.count(True)))
    valid_2 = solve2(passports, valid_1).count(True)
    print("Solution for part 2 is: {}".format(valid_2))
