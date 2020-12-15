import math
from functools import reduce

INPUT_FILE = './input/input.txt'

def parse_input():
    with open(INPUT_FILE) as f:
        ts = int(f.readline())
        line = f.readline().split(',')
        buses = []

        for b in line:
            if b != 'x':
                buses.append(int(b))
            else:
                buses.append(b)

    return ts, buses

def solve_1(ts, bus_schedule):
    wait = bus_schedule[0]
    bus_id = bus_schedule[0]

    for b in bus_schedule:
        if b == 'x':
            continue
        if b - int(ts%b) < wait:
            bus_id = b
            wait = b - int(ts%b)

    print(bus_id*wait)

# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


if __name__=='__main__':
    ts, bus_schedule = parse_input()
    solve_1(ts, bus_schedule)

    n = [x for x in bus_schedule if type(x) == int]
    a = [(x-bus_schedule.index(x)-x)%x for x in n]
    print(chinese_remainder(n, a))
