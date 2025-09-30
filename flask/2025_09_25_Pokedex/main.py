from flask import Flask, request
from flask import render_template
import pandas as pd
import matplotlib.pyplot as plt
import io, base64

app = Flask(__name__)
df = pd.read_csv('pokemon.csv')
df = df.sort_values(by=['Name'])

def makegraph(pokemon):
    cols = df.columns[5:-2]
    row = df.loc[df['Name']==pokemon].iloc[0,5:-2]
    fig = plt.Figure(figsize=(8,5))
    ax = fig.subplots()
    ax.bar(cols, row)
    ax.set_xlabel('Stat')
    ax.set_ylabel('Value')
    ax.tick_params("x", rotation=0)
    ax.set_title(f'Pokemon stats for {pokemon}')
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    return data

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('pokemon').lower()
        mask = df['Name'].str.lower().str.contains(query, na=False)
        pokemon = df.loc[mask, 'Name']
        type1 = df.loc[mask, 'Type 1'].fillna('None')
        type2 = df.loc[mask, 'Type 2'].fillna('None')
        total = df.loc[mask, 'Total'].fillna('None')

        packed_data = zip(pokemon, type1, type2, total)
        return render_template('index.html', packed_data=packed_data)
    else:
        pokemon = df.loc[:, 'Name']
        type1 = df.loc[:, 'Type 1'].fillna('None')
        type2 = df.loc[:, 'Type 2'].fillna('None')
        total = df.loc[:, 'Total'].fillna('None')

        packed_data = zip(pokemon, type1, type2, total)
        return render_template('index.html', packed_data=packed_data)

@app.route('/<pokemon>')
def subpage(pokemon):
    row = df.loc[df['Name'].str.lower() == pokemon.lower()]
    if row.empty:
        return 'Pokemon not found', 404
    row = row.iloc[0]
    type1 = row['Type 1'] if pd.notna(row['Type 1']) else 'None'
    type2 = row['Type 2'] if pd.notna(row['Type 2']) else 'None'
    hp = row['HP'] if pd.notna(row['HP']) else 'None'
    attack = row['Attack'] if pd.notna(row['Attack']) else 'None'
    defence = row['Defense'] if pd.notna(row['Defense']) else 'None'
    SpAttack = row['Sp. Atk'] if pd.notna(row['Sp. Atk']) else 'None'
    SpDefence = row['Sp. Def'] if pd.notna(row['Sp. Def']) else 'None'
    speed = row['Speed'] if pd.notna(row['Speed']) else 'None'
    total = row['Total'] if pd.notna(row['Total']) else 'None'


    return render_template('subpage.html', pokemon=pokemon, type1=type1, type2=type2, hp=hp, attack=attack, defence=defence, SpAttack=SpAttack, SpDefence=SpDefence, speed=speed, total=total, graph=makegraph(pokemon))

cols = df.columns[5:]
row = df.loc[df['Name']=='Pikachu'].iloc[0,5:]
print(row)
app.run(debug=True)