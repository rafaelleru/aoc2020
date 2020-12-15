import math

INPUT_FILE = './input/example.txt'

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


def solve_2(bus_schedule):
    timestamp = 0
    s_i = 0
    n = 1

    partial_sols = []

    for bus_id in bus_schedule:
        if type(bus_id) == int:
            n *= bus_id

    for i, bus_id in enumerate(bus_schedule):
        if bus_id == 'x':
            continue

        print("X === {} ({})".format(((bus_id-i)%bus_id), bus_id))
        s_i = pow(n//bus_id, -1, bus_id)
        partial_sols.append(((bus_id-i)%bus_id)*bus_id*s_i)

    print(sum(partial_sols))



if __name__=='__main__':
    ts, bus_schedule = parse_input()
    solve_1(ts, bus_schedule)
    solve_2(bus_schedule)
