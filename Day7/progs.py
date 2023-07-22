# Import dependencies
import csv

# Import data
data = []
with open('roster.txt', 'r') as file:
    csvreader = csv.reader(file, delimiter = '\n')

    for row in csvreader:
        data.append(row[0])

programs = {}

class Program:
    def __init__(self, name, weight, supporting, supported = False):
        self.name = name
        self.weight = weight
        self.supporting = supporting
        self.supported = supported

    def printProg(self):
        print(self.name, self.supporting)

def PartOne():
    for row in data:
        prog_name = row.split(' ')[0]
        prog_weight = row[row.find('(') + 1:row.find(')')]
        prog_supports = []

        if '->' in row:
            supports = row[row.find('>')+2:len(row)+1].split(',')
            for item in supports:
                prog_supports.append(item.replace(' ', ''))
        # Parse data into fields
        programs[prog_name] = Program(prog_name, prog_weight, prog_supports)

        # Our program data is now in a dictionary! Now we need to find the program at the bottom. This program will not be supported by any other program.

        # rule out all programs listed in another's prog_supports

    # Loop through all programs and those supported by each
    for name, program in programs.items():
        for supported_program_name in program.supporting:
            # Find the supported programs' dictionary entry and update 'supported' to true
            programs[supported_program_name].supported = True

    # Filter the dictionary to locate the program that is not supported by any others
    bottom_program = [name for name, program in programs.items() if programs[name].supported == False]

    print(bottom_program)


PartOne()