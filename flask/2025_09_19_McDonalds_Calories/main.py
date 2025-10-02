import base64

from flask import Flask
from flask import render_template
import pandas as pd
import matplotlib.pyplot as plt
import io
from flask import request
df = pd.read_csv('menu.csv')

app = Flask(__name__)

def get_categories():
    return df.loc[:, 'Category'].unique()

def get_items(category):
    return df.loc[df['Category']==category, 'Item'].unique()


def makegraph(category):
    fig = plt.Figure(figsize=(8,10))
    ax = fig.subplots()
    ax.bar(get_items(category), df.loc[df['Category']==category, 'Calories'])
    ax.set_xlabel('Item')
    ax.set_ylabel('Calories')
    ax.tick_params("x", rotation=90)
    ax.set_title(f'How many calories each {category} item contains')
    fig.tight_layout()
    buf = io.BytesIO()
    fig.savefig(buf, format="png")
    data = base64.b64encode(buf.getbuffer()).decode('ascii')
    return data


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form.get('query')
        print(query)
        items = df.loc[df['Item'].str.contains(query), ['Item','Calories']]
        print(items)
        graph_data = makegraph(query)
        return render_template('subpage.html', category=query,
                               items=zip(get_items(category), df.loc[df['Category'] == category, 'Calories']),
                               graph=graph_data)

    return render_template('index.html', categories=get_categories())

@app.route('/<category>')
def category(category):
    category = next(item for item in get_categories() if category in item)
    graph_data = makegraph(category)
    print(graph_data)
    return render_template('subpage.html', category=category, items=zip(get_items(category),df.loc[df['Category']==category, 'Calories']), graph=graph_data)

app.run(debug=True)