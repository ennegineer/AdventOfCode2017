# Dependencies!
import pandas as pd
import csv

# Import data
data = []
with open('./num.txt', 'r') as file:
    csvreader = csv.reader(file, delimiter = '\t')

    for row in csvreader:
        data.append([int(val) for val in row])

# Create dataframe
df = pd.DataFrame(data, columns = [f'num{i}' for i in range(16)])

def PartOne():
    df['Max'] = df.max(axis=1, numeric_only=True)
    df['Min'] = df.min(axis=1, numeric_only=True)
    df['Dif'] = df['Max'] - df['Min']
    answer = df['Dif'].sum()
    print(answer)
PartOne()