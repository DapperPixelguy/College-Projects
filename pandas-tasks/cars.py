import pandas as pd
import os
from matplotlib import pyplot as plt
import numpy as np
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

for file in os.listdir('./data'):
    print(os.fsdecode(file).replace('.csv', ''))


def main(csv,col1,col2):
    df = pd.read_csv(f'data/{csv}.csv')
    df = df[[col1, col2]]
    #corr = corr[col1]/ corr[col2]
    plt.scatter(df[col1], df[col2])
    #plt.xticks(np.arange(min(df[col1]),max(df[col2])+1,2))
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.legend([f'Correlation: {df[col1].corr(df[col2])}'])
    plt.title(f'{col1} vs {col2} for {csv}')
    plt.show()


choice = input('Choose from an option above: ').lower()
df = pd.read_csv(f'data/{choice}.csv')
print(', '.join(df.columns.unique()))
col1 = input('Enter a column to chose from: ')
col2 = input('Enter a column to compare it against: ')
main(choice,col1,col2)
