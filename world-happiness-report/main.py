import pandas as pd
from matplotlib import pyplot as plt
from tkinter import *

root = Tk()
root.geometry('300x200')
col1var = StringVar()
col1var.set('Logged GDP per capita')
col2var = StringVar()
col2var.set('Ladder score')
options = [
    'Ladder score',
    'Logged GDP per capita',
    'Social support',
    'Healthy life expectancy',
    'Generosity',
    'Freedom to make life choices',
    'Generosity',
    'Perceptions of corruption',
    'Ladder score in Dystopia'

]


def plot(col1, col2):
    plt.clf()
    plt.scatter(df[col1], df[col2])
    plt.xlabel(col1)
    plt.ylabel(col2)
    plt.show()


col1entry = OptionMenu(root, col1var, *options)
col2entry = OptionMenu(root, col2var, *options)
confirm_btn = Button(root, text='Plot', command=lambda: plot(col1var.get(), col2var.get()), width=20)

df = pd.read_csv('WHR2023.csv')

print(f'Correlation between Healthy life expectancy and Social support: {df["Healthy life expectancy"].corr(df["Social support"]).round(2)}')
print(f'Correlation between Generosity and Perception of corruption: {df["Generosity"].corr(df["Perceptions of corruption"]).round(2)}')
print(f'Correlation between Freedom to make life choices and Social support: {df["Freedom to make life choices"].corr(df["Social support"]).round(2)}')
print(f'Correlation between Freedom to make life choices and Social support: {df["Freedom to make life choices"].corr(df["Social support"]).round(2)}')
print(f'Correlation between Generosity and Logged GDP per capita: {df["Generosity"].corr(df["Logged GDP per capita"]).round(2)}')
print(f'Correlation between Ladder score and Perception of corruption: {df["Ladder score"].corr(df["Perceptions of corruption"]).round(2)}')

root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1, weight=1)
col1entry.grid(column=0, row=0, sticky='ew')
col2entry.grid(column=1, row=0, sticky='ew')
confirm_btn.grid(column=0, row=2, columnspan=2, sticky='new')
root.mainloop()

