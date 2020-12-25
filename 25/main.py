from collections import namedtuple

PairEncrytionCodes = namedtuple('PairEncrytionCodes', ['card_code', 'door_code'])


def transform_subject_number(value, subject_number):
    return (value*subject_number) % 20201227


def get_loop_size(public_code):
    transformed = 1
    loop_size = 0

    while transformed != public_code:
        loop_size += 1
        transformed = transform_subject_number(transformed, 7)

    return loop_size


def solve_1(input_codes):
    """Solve day 25 part 1

    :input_codes: tuple containing door and card generated public codes
    """
    card_loop_size = get_loop_size(input_codes.card_code)
    # door_loop_size = get_loop_size(input_codes.door_code)

    door_generated_code = 1

    for i in range(card_loop_size):
        door_generated_code = transform_subject_number(door_generated_code, input_codes.door_code)

    print("Generated code for door is:", door_generated_code)


if __name__ == "__main__":
    ex_input = PairEncrytionCodes(5764801, 17807724)  # => 5764801, 17807724
    prod_input = PairEncrytionCodes(2069194, 16426071)

    solve_1(prod_input)
