# Import dependencies
import csv

# Import data
data = []
with open('passcodes.txt', 'r') as file:
    csvreader = csv.reader(file, delimiter = '\n')

    for row in csvreader:
        data.append(row[0])

def PartOne():
    valids = 0
    # Loop through the list of data.
    for passcode in data:
    # Each item in the list has a series of words.
    # Check to see if any words are repeated.
        if len(set(passcode.split(' '))) == len(passcode.split(' ')):
            valids += 1

    print(valids)
PartOne()