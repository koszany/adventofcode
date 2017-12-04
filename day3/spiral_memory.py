from math import sqrt
from math import floor
from math import ceil

def get_coordinates(square):

    base = ceil(sqrt(square))
    if base%2 == 0:
        base += 1

    next_right_down_corner = base**2
    side_length = base - 1

    x = floor(side_length/2)
    y = (-1) * floor(side_length/2)
    moves_amount = next_right_down_corner - square

    if moves_amount > side_length:
        x -= side_length
        moves_amount -= side_length
    else:
        x -=moves_amount
        moves_amount = 0

    if moves_amount > side_length:
        y += side_length
        moves_amount -= side_length
    else:
        y += moves_amount
        moves_amount = 0

    if moves_amount > side_length:
        x += side_length
        moves_amount -= side_length
    else:
        x +=moves_amount
        moves_amount = 0

    if moves_amount > side_length:
        y -= side_length
        moves_amount -= side_length
    else:
        y -=moves_amount
        moves_amount = 0

    return x, y


def main():
    get_coordinates(52)

if __name__ == '__main__':
    main()
