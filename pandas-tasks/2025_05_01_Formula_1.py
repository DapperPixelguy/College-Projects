import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from labellines import labelLines
from pandas.util.version import Infinity

pd.set_option("display.max_columns", None, "display.width", 99999)

df = pd.read_csv('data/Formula1_2024.csv')
class F1Plot:
    def __init__(self):
        self.fig, self.ax = plt.subplots()


    def bahrain(self):
        x= []
        for nation in df.Nationality.unique():
            drivers = df.loc[df.Nationality==nation, ['Nationality', 'Bahrain']]
            print('DRIVERS')
            print(drivers)
            print('TOTAL')
            print(drivers['Bahrain'].values.sum())
            x.append(drivers['Bahrain'].values.sum())

        plt.bar(df.Nationality.unique(), x)
        plt.xticks(rotation=45)
        plt.show()

    def avg_all_race(self):
        allscores = []

        colormap = plt.cm.get_cmap('nipy_spectral', len(df.Nationality.unique()))
        colour_map = {nat: colormap(i) for i, nat in enumerate(df.Nationality.unique())}
        for nation in df.Nationality.unique():
            scores = []
            drivers = df.loc[df.Nationality==nation]
            print('DRIVERS')
            print(drivers)

            for race in df.loc[:, 'Bahrain':]:
                print(race, drivers[race].values.sum()/len(drivers.Driver.unique()))
                scores.append(drivers[race].values.sum()/len(drivers.Driver.unique()))

            plt.scatter(df.columns[3:], scores, label=nation, color=colour_map[nation])
            plt.plot(df.columns[3:], scores, label=nation, color=colour_map[nation])
        plt.legend()
        plt.xlabel('Race')
        plt.ylabel('Average score')
        plt.title('Average scores for countries over different races')
        plt.grid()
        plt.xticks(rotation=45)
        plt.show()


            # print('TOTAL')
            # print(drivers['Bahrain'].values.sum())
            # x.append(drivers['Bahrain'].values.sum())

    def cumulative_driver(self):
        min_score = 30

        to_plot = []
        for driver in df.Driver.unique():
            # print(np.cumsum(df.loc[df['Driver']==driver, 'Bahrain':].values), df.columns[3:])
            if np.cumsum(df.loc[df['Driver']==driver, 'Bahrain':].values).max() > min_score:
                to_plot.append((np.cumsum(df.loc[df['Driver']==driver, 'Bahrain':].values), driver))
                # plt.plot( df.columns[3:], np.cumsum(df.loc[df['Driver']==driver, 'Bahrain':].values), label=driver, color=colour_map[driver])
        sorted_drivers = sorted(to_plot, key=lambda l:l[0].max(), reverse = False)
        colormap = plt.get_cmap('rainbow', len(sorted_drivers))
        colour_map = {nat[1]: colormap(i) for i, nat in enumerate(sorted_drivers)}

        for driver in sorted_drivers:
            plt.plot(df.columns[3:], driver[0], label=driver[1], color=colour_map[driver[1]])


        # plt.legend()
        plt.grid(alpha=0.5)
        plt.xticks(rotation=90)
        plt.title(f'Cumulative scores of drivers over the year ({min_score}+)')
        plt.xlabel('Race')
        plt.ylabel('Cumulative score')
        plt.tight_layout()
        lines = plt.gca().get_lines()
        labelLines(lines, align=False, outline_color='white')
        plt.show()


app = F1Plot()
app.cumulative_driver()

#avg_all_race()

