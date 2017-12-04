from math import sqrt
from math import floor
from math import ceil

def get_manhattan_distance(square):

    x, y = get_coordinates(square)

    return abs(x) + abs(y)

def get_coordinates(square):

    base = ceil(sqrt(square))
    if base%2 == 0:
        base += 1

    next_right_down_corner = base**2
    side_length = base - 1

    x = floor(side_length/2)
    y = (-1) * floor(side_length/2)
    moves_amount = next_right_down_corner - square

    print(x, y)
    print(moves_amount)

    x = move_backward(x, moves_amount, side_length)
    moves_amount = decrease(moves_amount, side_length)

    print(x, y)
    print(moves_amount)

    y = move_forward(y, moves_amount, side_length)
    moves_amount = decrease(moves_amount, side_length)
    print(x, y)
    print(moves_amount)

    x = move_forward(x, moves_amount, side_length)
    moves_amount = decrease(moves_amount, side_length)
    print(x, y)
    print(moves_amount)

    y = move_backward(y, moves_amount, side_length)
    moves_amount = decrease(moves_amount, side_length)
    print(x, y)
    print(moves_amount)

    return x, y

def move_backward(coor, moves_amount, side_length):
    if moves_amount > side_length:
        coor -= side_length
    else:
        coor -= moves_amount

    return coor

def move_forward(coor, moves_amount, side_length):
    if moves_amount > side_length:
        coor += side_length
    else:
        coor += moves_amount

    return coor

def decrease(moves_amount, side_length):
    if moves_amount > side_length:
        moves_amount -= side_length
    else:
        moves_amount = 0

    return moves_amount

def main():

    square = int(input("Enter the number of square: "))
    print(get_manhattan_distance(square))

if __name__ == '__main__':
    main()
