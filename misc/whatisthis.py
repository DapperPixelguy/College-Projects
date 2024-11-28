from pyinflect import *
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
from os import listdir
from random import *

def d():
    name, a, b, c = input('name'), int(input('num1')), int(input('num2')), int(input('num3'))

    print(f'Avg score for {name}: {(a+b+c)/3:.2f}')

    x = 912.3145678
    print(f'{x:.2f}, {x:.3e}, {x:.9f}')


def password_checker():
    flag = True
    while flag:
        password = input('Enter password: ')

        flag = False

        if not 5 <= len(password) <= 20:
            print('Length must be over 5 and under 20')
            flag = True

        if password.lower() == password:
            print('Must contain uppercase characters')
            flag = True

        if password.upper() == password:
            print('Must contain lowercase characters')
            flag = True

        if ' ' in list(password):
            print('No spaces')
            flag = True

    print('password ok')


def poem_calc():
    #f = open("data/poem.txt", "r")

    #lines = f.readlines()

    #df = pd.DataFrame(columns=['Avg', 'Words'])
    high = [[], []]
    markers = ['o', '+', 'x', ',', '.']
    markerpoint = 0
    for file in os.listdir('data'):
        arr = []
        f = open(f'data/{file}')
        lines = f.readlines()
        for line in lines:
            avg = 0
            words = line.split(' ')
            if len(line) > 1:
                for word in words:
                    word = word.strip(',\n:;.')
                    avg += len(word)
                    print(f'{word}, len: {len(word)}')

                avg = avg/len(words)
                arr.append([avg, len(words)])
            else:
                pass

        df = pd.DataFrame(columns=['Avg', 'Words'], data=arr)
        print(df)
        plt.scatter(df['Avg'], df['Words'], marker=markers[markerpoint])
        plt.xlabel('Average number of characters')
        plt.ylabel('Number of words')
        high[0].append(df['Avg'].max())
        high[1].append(df['Words'].max())
        markerpoint += 1
    plt.xticks(np.arange(0, max(high[0]) + 1, 0.5))
    plt.yticks(np.arange(0, max(high[1]) + 1))
    plt.legend(listdir('data'))
    plt.show()


poem_calc()
