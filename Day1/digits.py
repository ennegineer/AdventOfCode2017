# Given a series of numbers, look to see if each matches the next. If so, add the number and move on.
# If the number doesn't match the next, move on.
# Remember to check if the last number matches the first.


# Import data
data = []
with open('digits.txt') as csv_data:
  # Pull in raw data as strings in a list.
  data = [val for val in next(csv_data)]


def PartOne():
    answer = 0
    for index, i in enumerate(data):
        nextnum = index + 1

        # account for the last digit!
        if nextnum >= len(data):
            nextnum = 0

        if int(i) == int(data[nextnum]):
            answer += int(i)

    print(answer)
    # 10548 is too high.
    # 1203 was correct!
# PartOne()

def PartTwo():
    answer = 0
    x = len(data)
    nextnum = 0
    for index, i in enumerate(data):
        nextnum = int((x/2) + index)

        if nextnum >= len(data):
            nextnum = int((x/2) + index - len(data))

        if int(i) == int(data[nextnum]):
            answer += int(i)

    print(answer)

PartTwo()