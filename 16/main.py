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
                    ranges.append([int(values[0]), int(values[1])])
                rules[rule_name] = ranges

            line = f.readline()

    return rules, my_ticket, nearby

def solve_1(rules, nearby_tickets):
    error_rate = []
    possible_values = []
    invalids = []
    valid_tickets = []
    for r in rules:
        for tr in rules[r]:
            possible_values.append(tr)

    for i, t in enumerate(nearby_tickets):
        all_tickets_values = True
        for v in t:
            found = False
            for test_range in possible_values:
                if test_range[0] <= v <= test_range[1]:
                    found = True
            if found == False:
                error_rate.append(v)
                invalids.append(t)
                break

    # This is tricky
    for t in nearby_tickets:
        if t not in invalids:
            valid_tickets.append(t)

    print(sum(error_rate))
    return valid_tickets

def is_right_i(tickets, rule, i):
    valid = True
    for t in tickets:
        if not ((rule[0][0] <=  t[i] <= rule[0][1]) or (rule[1][0] <=  t[i] <= rule[1][1])):
            return False
    return True


def solve_2(rules, nearby_tickets, my_ticket):
    rule_pos = {k: [] for k in rules}
    i = 0
    for i in range(20):
        for rule_name in rules:
            if is_right_i(nearby_tickets, rules[rule_name], i):
                rule_pos[rule_name].append(i)

    i = 1
    taken = set()
    sorted_rules = {}
    while i <= 20:
        for rule in rule_pos:
            if len(rule_pos[rule]) == i:
                # import pdb; pdb.set_trace()
                for v in rule_pos[rule]:
                    if v not in taken:
                        sorted_rules[rule] = v
                        taken.add(v)
                        break

        i += 1

    to_multiply = []
    for k in sorted_rules:
        if 'departure' in k:
            to_multiply.append(my_ticket[sorted_rules[k]])

    # print(to_multiply)
    n = 1
    for i in to_multiply:
        n *= i

    print(n)




if __name__ == '__main__':
    rules, my_ticket, nearby_tickets = parse_input(INPUT_FILE)
    valid_tickets = solve_1(rules, nearby_tickets)
    solve_2(rules, valid_tickets, my_ticket)
