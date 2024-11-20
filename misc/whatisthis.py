from pyinflect import *

def d():
    name, a, b, c = input('name'), int(input('num1')), int(input('num2')), int(input('num3'))

    print(f'Avg score for {name}: {(a+b+c)/3:.2f}')

    x = 912.3145678
    print(f'{x:.2f}, {x:.3e}, {x:.9f}')


print(getInflection(input('Enter noun:' ), 'NNS'))