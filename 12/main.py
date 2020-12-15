INPUT_FILE = './input/input.txt'

def solve_1(movements):

    coord = (0,0)
    facing = 0

    mov_facing = {
        0 : lambda x: (coord[0]+x, coord[1]), #east
        1 : lambda y: (coord[0], coord[1]-y), #south
        2 : lambda x: (coord[0]-x , coord[1]), #west
        3 : lambda y: (coord[0] , coord[1]+y) #north
    }

    mov_ship = {
        'E': lambda x: (coord[0]+x, coord[1]),
        'S': lambda y: (coord[0], coord[1]-y),
        'W': lambda x: (coord[0]-x , coord[1]),
        'N': lambda y: (coord[0] , coord[1]+y)
    }

    rotations = {
        90: 1,
        180: 2,
        270: 3,
        360: 0,
    }

    for m in movements:
        # import pdb; pdb.set_trace()
        units = int(m[1:])
        if 'F' in m:
            coord = mov_facing[facing](units)
        elif 'R' in m:
            facing = (facing + rotations[units])%4
        elif 'L' in m:
            facing =  (facing - rotations[units])%4
        elif 'N' in m:
            coord = mov_ship['N'](units)
        elif 'S' in m:
            coord = mov_ship['S'](units)
        elif 'E' in m:
            coord = mov_ship['E'](units)
        elif 'W' in m:
            coord = mov_ship['W'](units)

    return abs(coord[0]) + abs(coord[1])


def solve_2(movements):
    coord = (0,0)
    waypoint = [10,1]
    facing = 0

    mov_waypoint = {
        'E': lambda x: (waypoint[0]+x, waypoint[1]),
        'S': lambda y: (waypoint[0], waypoint[1]-y),
        'W': lambda x: (waypoint[0]-x , waypoint[1]),
        'N': lambda y: (waypoint[0], waypoint[1]+y)
    }

    for m in movements:
        units = int(m[1:])
        if 'F' in m:
            coord = coord[0]+units*waypoint[0], coord[1]+units*waypoint[1]
        elif 'N' in m:
            waypoint = mov_waypoint['N'](units)
        elif 'S' in m:
            waypoint = mov_waypoint['S'](units)
        elif 'E' in m:
            waypoint = mov_waypoint['E'](units)
        elif 'W' in m:
            waypoint = mov_waypoint['W'](units)
        else:
            if 'L' in m:
                units = -units

            for i in range(int(units/90)%4):
                # Rotacion de un vector
                waypoint = [waypoint[1], -waypoint[0]]

    return abs(coord[0]) + abs(coord[1])



if __name__ == '__main__':
    with open(INPUT_FILE) as f:
        movements = [l.strip() for l in f.readlines()]

    manhattan = solve_1(movements)
    print(manhattan)
    manhattan = solve_2(movements)
    print(manhattan)
