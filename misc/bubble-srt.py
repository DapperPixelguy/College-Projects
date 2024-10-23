import random
import time
from matplotlib import pyplot as plt
import pandas as pd

df = pd.DataFrame(data=[], columns=['time', 'checks'])
for i in range(500):
    time.sleep(0.1)
    start_time = time.time()
    values = random.sample(range(100), 100)
    checks = 0
    pos = 0

    for value in values:
        pos += 1
        for i in range(len(values)-1):
            checks += 1
            print(f'checking {len(values)-(1+pos)}')
            if values[i] > values[i+1]:
                values[i], values[i+1] = values[i+1], values[i]
            else:
                pass
    endtime = time.time()-start_time
    df.loc[len(df.index)] = [endtime, checks]
    print(values)


print(df.sort_values('checks', ascending=False).head(15))
df.to_csv('checks.csv')
plt.scatter(df['checks'], df['time'])
plt.xlabel('Checks')
plt.ylabel('Time')
plt.show()

print(f'{round(endtime, 5)}s')
print(f'Ran {checks} checks')
print(values)

