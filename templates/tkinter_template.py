import tkinter as tk


class ExampleGUI:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x200')
        self.root.title("Example Title")

        self.current_activity = tk.StringVar()
        self.current_activity.set('Example activity')
        self.current_activity_label = tk.Label(self.root, textvariable=self.current_activity)

        self.example_field = tk.Entry()
        self.example_button = tk.Button(text='Example Button', command=self.example_function)

        self.current_activity_label.pack()

        self.current_activity_label.pack()
        self.example_button.pack()

    def example_function(self):
        pass


root_ = tk.Tk()
ExampleGUI(root_)
root_.mainloop()
