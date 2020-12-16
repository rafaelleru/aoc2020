INPUT_FILE = './input/input.txt'

def parse_input(input_file):
    rules = {}
    nearby = []
    pasring_nearby = False

    with open(input_file) as f:
        line = f.readline()
        # la primera linea siempre es una regla

        while line:
            if line == '\n':
                line = f.readline()
                continue
            if 'your ticket:' in line:
                line = f.readline()
                my_ticket = [int(x) for x in line.strip().split(',')]
                line = f.readline()
                continue
            elif 'nearby tickets:' in line:
                pasring_nearby = True
                line = f.readline()
                continue

            if pasring_nearby:
                nearby.append([int(x) for x in line.strip().split(',')])
            else:
                rule_name, values_spec = line.split(':') # 'class', '1-3 or 5-7'
                ranges = []
                for spec in values_spec.split('or'):
                    spec = spec.strip()
                    values = spec.split('-')
                    ranges.extend([x for x in range(int(values[0]), int(values[1])+1)])
                rules[rule_name] = ranges

            line = f.readline()

    return rules, my_ticket, nearby

def solve_1(rules, nearby_tickets):
    error_rate = []
    possible_values = []
    for r in rules.values():
        possible_values.extend(r)
    valid = True
    for ticket in nearby_tickets:
        for v in ticket:
            if v not in possible_values:
                error_rate.append(v)
                break

    print(sum(error_rate))


if __name__ == '__main__':
    rules, my_ticket, nearby_tickets = parse_input(INPUT_FILE)
    solve_1(rules, nearby_tickets)
