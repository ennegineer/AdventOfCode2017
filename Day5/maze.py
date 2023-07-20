# Import dependencies
import csv

# Import data
instructions = []
with open('jump.txt', 'r') as file:
    csvreader = csv.reader(file, delimiter = '\n')

    for row in csvreader:
        instructions.append(row[0])

def PartOne():
    # Start with line 1 and move the number shown, then increment the number + one.
    # Next move is from the line we stop on - moving the number shown, incrementing the number at that stop.
    # How many steps do we take before we exit the maze?
    step = 0
    location = 0

    while location in range(0, len(instructions)):
        if location >= 0 and location <= len(instructions):
            # grab/update the current instruction to the new location
            current_instruction = int(instructions[location])
            # add 1 to the value at the current location
            instructions[location] = int(instructions[location]) + 1
            # update our location
            location = location + current_instruction
            # increase our step by 1
            step += 1
            # print(f'Step: {step}: Location {location}, moving {current_instruction}')
        else:
            print(step + 1)
    print(f'Step: {step}: Location {location}, moving {current_instruction}')


def PartTwo():
    # How many steps do we take before we exit the maze?
    step = 0
    location = 0

    while location < len(instructions):
        if location >= 0 and location <= len(instructions):
            # grab/update the current instruction to the new location
            current_instruction = int(instructions[location])
            # update the value at the current location
            if current_instruction >= 3:
            # remove 1 from the value at the current location
                instructions[location] = int(instructions[location]) - 1
            else:
            # add 1 to the value at the current location
                instructions[location] = int(instructions[location]) + 1
            # update our location
            location = location + current_instruction
            # increase our step by 1
            step += 1
            # print(f'Step: {step}: Location {location}, moving {current_instruction}')
        else:
            print(step + 1)
    print(f'Step: {step}: Location {location}, moving {current_instruction}')

PartTwo()