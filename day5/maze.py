def main():
    print(get_amount_steps_increase('puzzle_input.csv'))
    print(get_amount_steps_decrease_increase('puzzle_input.csv'))

def get_amount_steps_decrease_increase(file_name):

    maze = get_maze_from_file(file_name)
    amount_steps = 0

    index = 0
    while index in range(len(maze)):
        jump = maze[index]

        if maze[index] < 3:
            maze[index] +=1
        else:
            maze[index] -=1

        index += jump
        amount_steps += 1

    return amount_steps

def get_amount_steps_increase(file_name):

    maze = get_maze_from_file(file_name)
    amount_steps = 0

    index = 0
    while index in range(len(maze)):
        jump = maze[index]
        maze[index] +=1
        index += jump
        amount_steps += 1

    return amount_steps

def get_maze_from_file(file_name):

    maze = []

    with open(file_name) as f:
        for line in f:
            maze.append(int(line.strip()))

    return maze


if __name__ == '__main__':
    main()
