import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt


class Application:
    def __init__(self, _root):
        self.root = _root
        self.root.geometry('500x400')
        self.titlevar = tk.StringVar()
        label = tk.Label(textvariable=self.titlevar)
        self.titlevar.set('Main Menu')
        self.root.title('Reports')
        self.options_frame = tk.Frame()
        self.options_frame.grid_columnconfigure(0, weight=1)
        tk.Button(self.options_frame, text='Enter sales record', command=self.sales_record).grid(row=0, column=0)
        tk.Button(self.options_frame, text='Run reports', command=self.reports_options).grid(row=0, column=1)
        label.pack()
        self.options_frame.pack()

    def sales_record(self):
        self.options_frame.pack_forget()
        self.titlevar.set('Entering sales record')


    def reports_options(self):
        pass

    def get_dates(self):
        pass

root = tk.Tk()
app = Application(root)
root.mainloop()
