from collections import defaultdict

def solve_1(numbers, nturns=2020):
    history = defaultdict(list)
    for i, n in enumerate(numbers):
        history[n] = [i+1]

    last = 0
    was_new = True

    for i in range(len(numbers)+1, nturns+1):
        if was_new:
            last = 0  # se dice el numero 0
        else:
            last = history[last][-1] - history[last][-2]

        was_new = last not in history
        history[last].append(i)

    print(last)

if __name__ == '__main__':
    # numbers = [0,3,6] # Example
    numbers = [19,20,14,0,9,1] # Input
    solve_1(numbers, 2020)
    solve_1(numbers, 30000000)
