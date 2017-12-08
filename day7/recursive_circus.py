def main():

    print(get_bottom_program('puzzle_input.csv'))

def get_bottom_program(file_name):
    towers_structure = {}
    towers_weight = {}
    towers_occurances = {}
    with open(file_name) as f:
        for line in f:
            data = line.strip().split()
            towers_weight[data[0]] = int(data[1][1:-1])
            towers_structure = udate_tower_structure(towers_structure, data)

    for program in towers_structure:
        if is_bottom(program, towers_structure):
            return program


def udate_tower_structure(towers_structure, data):
    hold_towers = []
    for i in range(3, len(data)):
        if data[i][-1] == ",":
            data[i] = data[i][:-1]
        hold_towers.append(data[i])
    towers_structure[data[0]] = hold_towers
    return towers_structure

def is_bottom(program, towers_structure):
    for hold_towers in towers_structure.values():
        if program in hold_towers:
            return False
    return True

if __name__ == '__main__':
    main()
