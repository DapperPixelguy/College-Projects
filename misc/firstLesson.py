import tkinter as tk
import math
import time
from pyinflect import getInflection
from matplotlib import pyplot as plt
import numpy as np
root = tk.Tk()
root.geometry('250x250')


def perfect_find():
    perfect = []
    for i in range(1,10000):
        number = i
        sum = 0
        if i % 2 == 0:
            for f in range (1,number):
                if number % f == 0:
                    sum += f

            if sum == number:
                print(f'FOUND! {number}')
                perfect.append(number)
        else:
            continue

    print('Finished!')
    [print(x) for x in perfect]


def prime_find():
    active = True
    while active:
        try:
            number = int(input('Enter number to check: '))
            active = False
        except ValueError:
            print('Enter a number, not a string or float.')

        if number > 2 and number % 2 == 0:
            print(f'{number} is not a prime number.')
        else:
            count = 0
            for i in range(1,number):
                if number % i == 0:
                    count += 1
            if count > 1:
                print(f'{number} is not a prime number.')
            if count == 1:
                print(f'{number} is a prime number')


def quadratic_solver():                         # x=   -b +/- ROOT  b^2 - 4ac OVER 2a
    results = []
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))
    d = (b * b) - (4 * a * c)
    print(d)
    if d >= 0:
        d = math.sqrt(d)
        print((-b + d) / (2 * a))
        print((-b - d) / (2 * a))


def fibonacci():
    sequence = [0,1]
    for i in range(0,100):
        sequence.append(sequence[-1]+sequence[-2])
        print(sequence[-1])
        time.sleep(0.1)


def array_sort():
    numbers = [9,4,5,3,2,8,6,1,0,7]
    print(numbers)
    sorted = []
    while len(numbers) > 0:
        sorted.append(numbers.pop(numbers.index(min(numbers))))
    print(sorted)


def gerund_finder():
    verb = input('Enter a verb: ')
    print(getInflection(verb, 'VBG'))


def mandelbrot():
    limit = 50
    res = 500
    colourmap = 'magma'

    xr = np.linspace(-2, 1, res)
    yr = np.linspace(-1.5, 1.5, res)

    iterArray = []
    for y in yr:
        row = []
        for x in xr:
            c = complex(x,y)
            z = 0
            for i in range(limit):
                if abs(z) >= 2:
                    row.append(i)
                    break
                else:
                    z = z**2 + c
            else:
                row.append(0)
        iterArray.append(row)
    for i in range(len(iterArray)):
        print(iterArray[i])
    ax = plt.axes()
    ax.set_aspect('equal')
    graph = ax.pcolormesh(xr, yr, iterArray, cmap= colourmap)
    bar = plt.colorbar(graph)
    plt.gcf().set_size_inches(10,8)
    plt.show()


perfect = tk.Button(root, command= perfect_find, text='Perfect number lister')
prime = tk.Button(root, command= prime_find, text='Prime number finder')
quadratic = tk.Button(root, command= quadratic_solver, text='Quadratic equation solver')
fibonacci = tk.Button(root, command= fibonacci, text='Fibonacci sequence lister')
sort = tk.Button(root, command = array_sort, text='Array sorter')
gerund = tk.Button(root, command=gerund_finder, text='Gerund finder')
mandelbrot = tk.Button(root, command=mandelbrot, text='Mandelbrot display')
quadratic.pack()
perfect.pack()
prime.pack()
fibonacci.pack()
sort.pack()
gerund.pack()
mandelbrot.pack()
root.mainloop()
