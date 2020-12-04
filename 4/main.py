INPUT_FILE = './input/input.txt'

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
    return [valid_passport(p, {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}) for p in passports].count(True)

if __name__ == '__main__':
    passports = read_passwords()
    print(solve1(passports))
