import pandas as pd

df = pd.read_csv('data/messy.csv')

print(df)

def clean(field):
    field = df[field]
    x = []
    for person in field:
        if not isinstance(person, str) or not person.strip():
            x.append('[NO DATA]')
            continue
        person = person.strip().lower()
        print(person)
        x.append(person)
    return pd.Series(x)

for col in df:
    df[col] = clean(col)

df['Name'] = df['Name'].apply(lambda person: person.capitalize() if person != '[NO DATA]' else person)
df['Country'] = df['Country'].str.upper()
df['Email'] = df['Email'].str.replace(' ', '')
df['JoinDate'] = df['JoinDate'].str.replace('/', '-')
df['Salary'] = df['Salary'].str.replace('k', '000')
print(df)
