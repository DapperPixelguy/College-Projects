import tkinter as tk

class LambdaDem:
    def __init__(self, root):
        self.root = root
        self.root.geometry('200x200')
        bg = root.cget('background')
        self.title = tk.Label(text='Lambda demonstration')
        self.bl_button = tk.Button(text='Blue', command=lambda:self.change_colour('blue'))
        self.rd_button = tk.Button(text='Red', command=lambda:self.change_colour('red'))
        self.grn_button = tk.Button(text='Green (no lambda)', command=self.change_colour('green'))
        self.root.config(background=bg)

        self.title.pack()
        self.bl_button.pack()
        self.rd_button.pack()
        self.grn_button.pack()

    def change_colour(self, colour):
        self.root.config(bg=colour)

root = tk.Tk()
LambdaDem(root)

numbers= [1,2,3,4,5,6,7,8,9]
input(f'{numbers}\nPress enter to sort ')
_sorted = list(filter(lambda x: x % 2 == 0, numbers))
print(_sorted)
_next = input('Press enter to continue ')
root.mainloop()