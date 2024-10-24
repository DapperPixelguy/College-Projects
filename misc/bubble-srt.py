import random
import time
from matplotlib import pyplot as plt
import pandas as pd

start = time.time()

df = pd.DataFrame(data=[], columns=['time', 'checks', 'swaps', 'items'])
for k in range(1000):
    #time.sleep(0.1)
    start_time = time.time()
    values = random.sample(range(k), k)
    #print(values)
    checks = 0
    swaps = 0
    pos = 0

    for value in values:
        pos += 1
        for i in range(len(values)-pos):
            checks += 1
            if values[i] > values[i+1]:
                swaps += 1
                values[i], values[i+1] = values[i+1], values[i]
    endtime = time.time()-start_time
    df.loc[len(df.index)] = [endtime, checks, swaps, k]
    #print(values)
    print(f'{1000-k} remaining')


print(df.sort_values('time', ascending=False).head(15))
fig, axs = plt.subplots(2,2)

axs[0,0].scatter(df['checks'], df['time'])
axs[0,0].set_title('Checks vs Time')
axs[0,0].set_xlabel('Checks')
axs[0,0].set_ylabel('Time')

axs[0,1].scatter(df['items'], df['swaps'])
axs[0,1].set_title('Items vs Swaps')
axs[0,1].set_xlabel('Items')
axs[0,1].set_ylabel('Swaps')

axs[1,0].scatter(df['items'], df['time'])
axs[1,0].set_title('Items vs Time')
axs[1,0].set_xlabel('Items')
axs[1,0].set_ylabel('Time')

axs[1,1].scatter(df['checks'], df['swaps'])
axs[1,1].set_title('Checks vs Swaps')
axs[1,1].set_xlabel('Checks')
axs[1,1].set_ylabel('Swaps')

plt.show()

#print(f'{round(endtime, 5)}s')
#print(f'Ran {checks} checks')
#print(values)
print(f'Took {time.time()-start}')
