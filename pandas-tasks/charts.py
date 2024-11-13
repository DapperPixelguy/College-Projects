import pandas as pd
from matplotlib import pyplot as plt
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
df = pd.read_csv("data/vgsales.csv")

fig, ax = plt.subplots(2,2)
plt.subplots_adjust(hspace=0.8)

data = [df[df['Genre'] == genre]["Global_Sales"].dropna() for genre in df["Genre"].unique()]

ax[0,0].violinplot(data)
ax[0,0].set_xticks(range(1, len(df["Genre"].unique()) + 1))
ax[0,0].set_xticklabels(df["Genre"].unique(), rotation=90)
ax[0,0].set_xlabel("Genre")
ax[0,0].set_ylabel("Sales")

data = df.groupby('Publisher')['Global_Sales'].sum().sort_values(ascending=False).head(15)
ax[0,1].bar(data.index, data.values)
ax[0,1].set_xticklabels(data.index, rotation=90)
plt.show()

print(df.head())

