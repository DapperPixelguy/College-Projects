import pandas as pd
import tkinter as tk


class EqualityGame:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x200')
        self.root.title("Equality act game")

        self.df = pd.read_csv('./data/Equality_Act_Scenarios.csv')

        self.current_activity = tk.StringVar()
        self.current_activity.set('Equality act game')
        self.current_activity_label = tk.Label(self.root, textvariable=self.current_activity)

        self.scenario = tk.StringVar()
        self.scenario.set('No scenario')
        self.scenario_label = tk.Label(self.root, textvariable=self.scenario, pady=30, wraplength=450)

        self.start_button = tk.Button(text='Start new scenario', command=lambda: self.change_packing('scenario'))
        self.exit_button = tk.Button(text='Exit program', command=exit)
        self.break_button = tk.Button(text='Breaks act')
        self.exempt_button = tk.Button(text='Exempt from act')

        self.current_activity_label.pack()

        self.scenario_label.pack()
        self.start_button.pack()
        self.exit_button.pack()

    def change_packing(self, pack_set):
        if pack_set == 'scenario':
            self.start_button.pack_forget()
            self.exit_button.pack_forget()
            self.break_button.pack()
            self.exempt_button.pack()
            self.new_scenario()

        if pack_set == 'intermission':
            self.break_button.pack_forget()
            self.exempt_button.pack_forget()
            self.start_button.pack()
            self.exit_button.pack()

    def new_scenario(self):
        self.start_button.pack_forget()
        self.break_button.pack()
        self.exempt_button.pack()

        self.current_activity.set('Reviewing scenario')
        random_state = self.df.sample(1)
        self.scenario.set(str(random_state.iloc[0]['scenario']))
        correct_answer = random_state.iloc[0]['breaksAct/exempt']
        print(correct_answer)

        self.break_button.configure(command=lambda: self.check_ans('Breaks Act', correct_answer))
        self.exempt_button.configure(command=lambda: self.check_ans('Exempt', correct_answer))

    def check_ans(self, answer, correct):
        if answer == correct:
            self.current_activity.set('Correct answer!')
        else:
            self.current_activity.set('Incorrect answer.')

        self.scenario.set('No scenario')
        self.change_packing('intermission')


root_ = tk.Tk()
EqualityGame(root_)
root_.mainloop()
