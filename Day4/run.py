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
# PartOne()


def PartTwo():
    valids_two = 0
        # Loop through the list of data.
    for passcode in data:
        tester = ''
    # Each item in the list has a series of words.
    # Check to see if any words are anagrams.
        phrase = passcode.split(' ')
        for word in phrase:
            sorted_word = ''.join(sorted(word))
            tester = tester + ' ' + sorted_word
        if len(set(tester.split(' '))) == len(tester.split(' ')):
            valids_two += 1

    print(valids_two)
PartTwo()