import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

pd.set_option("display.max_columns", None, "display.width", 99999)

df = pd.read_csv('Prerelease_data.csv')
def cumulative_shipping_costs(df):
    df = df.sort_values(by=['shipping_date'])
    df = df.loc[df['delivery_status']=='Delivered']
    total = np.cumsum(df['shipping_cost'])
    dates = pd.to_datetime(df['shipping_date'])

    print(df)

    plt.plot(dates, total)
    plt.grid(alpha=0.5)
    plt.xticks(rotation=45)
    plt.xlabel('Date')
    plt.ylabel('Cumulative shipping costs')
    plt.show()

def average_weight(df):
    df.sort_values(by=['package_weight_kg'])
    weights=df['package_weight_kg'].sort_values().unique()
    x=[]
    for weight in weights:
        subset = df.loc[df['package_weight_kg']==weight]
        cost = subset['shipping_cost'].sum() / len(subset)
        x.append(cost)

    plt.plot(weights, x)
    plt.xlabel('Average weight in Kg')
    plt.ylabel('Average shipping cost')
    plt.grid(alpha=0.5)
    plt.show()

average_weight(df)
