# Import dependencies
import csv

# Import data
data = []
with open('roster.txt', 'r') as file:
    csvreader = csv.reader(file, delimiter = '\n')

    for row in csvreader:
        data.append(row[0])

programs = []

class Program:
    def __init__(self, name, weight, supporting):
        self.name = name
        self.weight = weight
        self.supporting = supporting

    def printProg(self):
        print(self.name, self.supporting)

def PartOne():
    for row in data[0:15]:
        prog_name = row.split(' ')[0]
        prog_weight = row[row.find('(') + 1:row.find(')')]
        prog_supports = []
        print(row)

        if '->' in row:
            supports = row[row.find('>')+2:len(row)+1].split(',')
            for item in supports:
                prog_supports.append(item.replace(' ', ''))
            # supports = [item for item in prog_supports if item.strip()]
        programs.append(Program(prog_name, prog_weight, prog_supports)) 
        print(f'{prog_name}, {prog_weight}, {prog_supports}')

        # Our program data is now in a class! Now we need to find the program at the bottom. This program will not be supported by any other program.

        # If len(prog_supports) > 0... 
        ## rule out all programs listed in another's prog_supports

        bottom_program = []
        for prog in programs:
            if len(prog.supporting) > 0:
                bottom_program.append(prog)
        print(bottom_program)

        for item in bottom_program:
            for supported_prog in item.supporting:
                if supported_prog in item.supporting:
                # remove from the list of bottom_programs if it's being supported by another
                ## loop through bottom_program contenders to see
                    
                    pass


PartOne()