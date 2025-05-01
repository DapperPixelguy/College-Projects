import pandas as pd
import tkinter as tk
from matplotlib import pyplot as plt
import numpy as np

df = pd.read_csv('data/Task4a_data 2023 06(in).csv')
# print(df)

class Application:
    def __init__(self, _root):
        self.root = _root
        self.root.geometry('600x400')


    def menu(self):
        option = input("1. Lunch"
                       "2. Dinner")
        pass

def graph():
    lunchitems = df.loc[df['Service']=='Lunch']
    x = []
    y = []
    print(lunchitems)
    for col in lunchitems.iloc[:, 2:]:
        print(lunchitems[col].sum())
        x.append(col)
        y.append(lunchitems[col].values.sum())
    print(x)
    print(y)
    plt.plot(x, y)
    plt.show()

def itemsbar():
    lunchitems = df.loc[df['Service']=='Lunch']
    dinneritems = df.loc[df['Service']=='Dinner']
    plt.bar(lunchitems['Menu Item'], lunchitems['3/3/2023'])
    plt.bar(dinneritems['Menu Item'], dinneritems['3/3/2023'], bottom=lunchitems['3/3/2023'].values)
    plt.legend(['Lunch', 'Dinner'])
    plt.xlabel('Menu Item')
    plt.ylabel('Total Sales')
    plt.title('Total sales for items across menus for data 3/3/2023')
    plt.show()

def cumulative():
    d1, d2 = '3/3/2023', '10/3/2023'
    lunchitems = df.loc[df['Service'] == 'Lunch', d1:d2]
    dinneritems = df.loc[df['Service'] == 'Dinner', d1:d2]
    print(lunchitems)

    plt.plot([pd.to_datetime(column, dayfirst=True).strftime('%d-%m-%Y') for column in lunchitems.columns], np.cumsum([lunchitems[column].values.sum() for column in lunchitems.columns]), marker='o')
    plt.plot([pd.to_datetime(column, dayfirst=True).strftime('%d-%m-%Y') for column in dinneritems.columns], np.cumsum([dinneritems[column].values.sum() for column in dinneritems.columns]), marker='o')
    plt.legend(['Lunch', 'Dinner'])
    plt.grid()
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.show()

itemsbar()
cumulative()
# graph()
#root = tk.Tk()
#app = Application(root)