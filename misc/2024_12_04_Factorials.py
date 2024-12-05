import sys
from matplotlib import pyplot as plt
import numpy as np


def factorial(n):
    if n == 1:
        ans = 1
    else:
        ans = n*factorial(n-1)

    return ans


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


r = 100
arr = []
high = []
min_steps = float('inf')

for i in range(1, r+1):
    print(stepping(i, 0))
    steps = stepping(i, 0)
    high.append(stepping(i, 0))
    plt.scatter(i, stepping(i, 0))
    arr.append(min(min_steps, steps))


plt.plot(arr)
plt.xticks(np.arange(1, r+1, 1), rotation=90)
plt.yticks(np.arange(0, max(high)+10, 10))
plt.margins(x=0)
plt.show()
print(stepping(3, 0))
