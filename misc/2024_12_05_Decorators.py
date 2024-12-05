import time
from matplotlib import pyplot as plt


def timer(func):
    def wrapper(*args,**kwargs):
        now = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f'{end-now:.6f}s')
        return result
    return wrapper


@timer
def stp():
    r = 1000000
    arr = []
    high = []
    min_steps = float('inf')

    for i in range(1, r + 1):
       # print(stepping(i, 0))
        stepping(i, 0)
        # high.append(stepping(i, 0))
        # plt.scatter(i, stepping(i, 0))
        # arr.append(min(min_steps, steps))



def stepping(n, step):

    if n <= 1:
        return step

    elif n % 2 == 0:
        n = n/2
        step += 1
        step = stepping(n, step)

    elif n % 2 != 0:
        n = (3*n) + 1
        step += 1
        step = stepping(n, step)

    return step

@timer
def stepping_for():

    for i in range(0, 1000000):
        flag = True
        step = 0
        while flag:
            if i <= 1:
                flag = False
            elif i % 2 == 0:
                i = i/2
                step += 1

            elif i % 2 != 0:
                i = (3*i) + 1
                step += 1




stepping_for()
