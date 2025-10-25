import pandas as pd
import matplotlib.pyplot as plt
from labellines import labelLines

df = pd.read_csv('data/Task4a_data.csv')
# print(df)
def bar():
    seperated_posts = []

    for post_type in df['Post Type'].unique():
        seperated_posts.append(df.loc[df['Post Type'] == post_type, :].transpose())

    print(seperated_posts)

    for post_type in seperated_posts:
        print(post_type.loc[post_type.index == 'Post Type'])
        plt.bar(post_type.loc[post_type.index == 'Post Type'].iloc[:,1], post_type.loc[post_type.index == 'Likes', :].values.sum())

    plt.ylabel('Likes')
    plt.show()

def post_frequency():
    day_daytes_value_storage_list_array_to_store = []
    for date in df.Date.unique():
        day_daytes_value_storage_list_array_to_store.append(df.loc[df['Date']==date])

    print(day_daytes_value_storage_list_array_to_store)

    image = []
    poll = []
    news = []
    advert = []
    for x in day_daytes_value_storage_list_array_to_store:
        print(len(x.loc[x['Post Type'] == 'Image']))
        image.append(len(x.loc[x['Post Type'] == 'Image']))
        poll.append(len(x.loc[x['Post Type'] == 'Poll']))
        news.append(len(x.loc[x['Post Type'] == 'News/update']))
        advert.append(len(x.loc[x['Post Type'] == 'Advertisement']))

    plt.plot(df['Date'].unique(), image)
    plt.plot(df['Date'].unique(), poll)
    plt.plot(df['Date'].unique(), news)
    plt.plot(df['Date'].unique(), advert)
    plt.grid(alpha=0.5)
    plt.show()


def average_post_interaction(type='Likes'):

    fig, ax = plt.subplots(2,2, figsize=(20,16))
    ax = ax.flatten()
    fig.delaxes(ax[3])
    for i, type in enumerate(['Likes', 'Shares', 'Comments']):
        maxes = []
        for post_type in df['Post Type'].unique():
            x = []
            for time in df['Time'].unique():
                #print(df.loc[df['Time'] == time].loc[df['Post Type'] == post_type])
                print(len(df.loc[df['Time']==time].loc[df['Post Type']==post_type]['Likes']))
                if len(df.loc[df['Time']==time].loc[df['Post Type']==post_type][type]):
                    x.append(df.loc[df['Time']==time].loc[df['Post Type']==post_type][type].values.sum()/len(df.loc[df['Time']==time].loc[df['Post Type']==post_type]['Likes']))
                else:
                    x.append(0)

            ax[i].plot(df['Time'].unique(), x, label=post_type)
            maxes.append(df['Time'].unique()[x.index(max(x))])

        labelLines(ax[i].get_lines(), xvals=maxes, align=False)
        ax[i].set_ylabel(f'Average {type}')
        ax[i].set_xlabel('Time of day')
        ax[i].tick_params(axis='x',rotation=45)
        ax[i].grid(alpha=0.5)
    plt.tight_layout()
    plt.show()

average_post_interaction('Comments')
#bar()
#post_frequency()