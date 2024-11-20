import pandas as pd
import tkinter as tk
df = pd.read_csv('./data/Equality_Act_Scenarios.csv')


class EqualityGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry('350x350')
        self.root.title("Equality act game")
        scenario = tk.StringVar()
        scenario_label = tk.Label(self.root, textvariable=scenario)
        self.root.mainloop()

    def new_scenario(self):
        pass



root_ = tk.Tk()
EqualityGame(root_)
