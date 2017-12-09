
class Program:
    FILE_NAME = 'puzzle_input.csv'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def __hash__(self):
        return hash(str(self))

    def __eq__(self, other):
        return self.name == other.name

    def __ne__(self, other):
        return not (self.name == other.name)

    def __str__(self):
        return ''.join([self.name, ': ', str(self.weight)])

    @classmethod
    def load_programs(cls):
        programs = []

        with open(cls.FILE_NAME) as f:
            for line in f:
                data = line.strip().split()

                name = data[0]
                weight = int(data[1][1:-1])
                programs.append(Program(name, weight))

        return programs

class Tower:

    FILE_NAME = 'puzzle_input.csv'

    def __init__(self):
        self.programs = []
        self.hold_programs = {}
        self.structure = []

        self.load_programs()
        self.load_hold_programs()

    def get_program(self, name):
        for program in self.programs:
            if program.name == name:
                return program

    def __str__(self):
        hold_programs_str = ""
        for key_program, hold_programs in self.hold_programs.items():
            hold_programs_str += str(key_program) + ' -> '

            for program in hold_programs:
                hold_programs_str += str(program) + ', '
            hold_programs_str += '\n'

        return hold_programs_str

    def load_programs(self):
        self.programs = Program.load_programs()

    def load_hold_programs(self):

        with open(self.FILE_NAME) as f:
            for line in f:
                data = line.strip().split()
                program = self.get_program(data[0])
                hold_programs = []

                for i in range(3, len(data)):
                    if data[i][-1] == ",":
                        data[i] = data[i][:-1]
                    hold_programs.append(self.get_program(data[i]))

                self.hold_programs[program] = hold_programs

    def get_bottom_program(self):

        for program in self.programs:
            if self.is_bottom(program):
                return program

    def is_bottom(self, program):
        for hold_towers in self.hold_programs.values():
            if program in hold_towers:
                return False
        return True

def main():

    tower = Tower()
    print(tower.get_bottom_program())

if __name__ == '__main__':
    main()
