import math

INPUT_FILE = './input/input.txt'

def parse_input():
    with open(INPUT_FILE) as f:
        ts = int(f.readline())
        line = f.readline().split(',')
        buses = []

        for b in line:
            if b != 'x':
                buses.append(int(b))

    return ts, buses

def solve_1(ts, bus_schedule):
    wait = bus_schedule[0]
    bus_id = bus_schedule[0]

    for b in bus_schedule:
        if b - int(ts%b) < wait:
            bus_id = b
            wait = b - int(ts%b)

    print(bus_id*wait)

def solve_2(bus_schedule):
    pass



if __name__=='__main__':
    ts, bus_schedule = parse_input()
    solve_1(ts, bus_schedule)

    solve_2(bus_schedule)
