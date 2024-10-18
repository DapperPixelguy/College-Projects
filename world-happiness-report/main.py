import pandas as pd
from matplotlib import pyplot as plt
from tkinter import *

root = Tk()
root.geometry('200x200')
col1var = StringVar()
col1var.set('Ladder score')
col2var = StringVar()
col2var.set('Logged GDP per capita')
options = [
    'Ladder score',
    'Logged GDP per capita',
    'Social support',
    'Healthy life expectancy'

]


def plot(col1, col2):
    pass


col1entry = OptionMenu(root, col1var, *options)
col2entry = OptionMenu(root, col2var, *options)
confirm_btn = Button(root, text='Plot', command=lambda: plot(col1var, col2var))

df = pd.read_csv('WHR2023.csv')

print(f'Correlation between Healthy life expectancy and Social support: {df["Healthy life expectancy"].corr(df["Social support"]).round(2)}')
print(f'Correlation between Generosity and Perception of corruption: {df["Generosity"].corr(df["Perceptions of corruption"]).round(2)}')
print(f'Correlation between Freedom to make life choices and Social support: {df["Freedom to make life choices"].corr(df["Social support"]).round(2)}')
print(f'Correlation between Freedom to make life choices and Social support: {df["Freedom to make life choices"].corr(df["Social support"]).round(2)}')
print(f'Correlation between Generosity and Logged GDP per capita: {df["Generosity"].corr(df["Logged GDP per capita"]).round(2)}')
print(f'Correlation between Ladder score and Perception of corruption: {df["Ladder score"].corr(df["Perceptions of corruption"]).round(2)}')

def scatterplt(col1,col2):
    plt.scatter(df[col1],df[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()
# scatterplt('Generosity','Ladder score')


col1entry.grid(column=0, row=0, sticky='w')
col2entry.grid(column=0, row=1, sticky='w')
confirm_btn.grid(column=0, row=2, sticky='w')
root.mainloop()

