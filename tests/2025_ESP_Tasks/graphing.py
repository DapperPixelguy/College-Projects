import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('example_data.csv',index_col=0)
unique_problems = df['Problem'].unique()

def resolutions():
    for resolution in df['How resolved'].unique():
        plt.bar(resolution, len(df.loc[df['How resolved']==resolution]))

    plt.show()

def problems():
    fig, ax = plt.subplots(ncols=len(df['Problem'].unique()), sharey=True)
    ax = ax.flatten()

    for i, problem in enumerate(df['Problem'].unique()):
        for resolution in df['How resolved'].unique():
            ax[i].bar(resolution, len(df.loc[(df['Problem']==problem)& (df['How resolved']==resolution)]))
            ax[i].set_title(problem)
            ax[i].tick_params(axis='x', rotation=45)
    fig.supylabel('Number of occurrences')
    fig.supxlabel('Resolution method')
    fig.subplots_adjust(wspace=0)
    plt.show()

def problem_pie():
    vals = []
    prob = []
    for problem in unique_problems:
        vals.append(len(df.loc[df['Problem']==problem]))
        prob.append(problem)
    plt.pie(vals, labels=prob, autopct='%1.2f%%', explode=[0.05 for i in vals], shadow=True)
    #plt.title(pad=0.2)
    plt.show()

resolutions()
problem_pie()
problems()
#print(df)