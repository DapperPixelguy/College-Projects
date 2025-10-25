import pandas as pd
import random

problems = ('Parcel damaged', 'Failed address verification', 'User account issue', 'Wrong item sent', 'Lost in transit', 'Transit issue')
resolutions = ('Full refund', 'Customer credit', 'Cancelled order', 'Partial refund', 'Reshipment')
rows=300
startdate = pd.to_datetime('20-05-2025', dayfirst=True)
print(startdate+pd.Timedelta(days=30))


data = {
    "Problem": [random.choice(problems) for _ in range(rows)],
    "How resolved": [random.choice(resolutions) for _ in range(rows)],
    "No of parcels": [random.randint(1,6) for _ in range(rows)],
    "No of days": [random.randint(1,7) for _ in range(rows)],
    "Date": [pd.to_datetime(startdate+pd.Timedelta(days=random.randint(0,180))).strftime('%d-%m-%Y') for _ in range(rows)]
}

df = pd.DataFrame(data)
df.to_csv('example_data.csv')