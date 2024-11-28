import random
import tkinter as tk

# I could add multiple users using lists and a counter, but I probably don't have time now
# I would also add variable ranges using lambda functions with the button but not enough time now

root = tk.Tk()
root.geometry('350x225')
root.title('Number guessing game')
title = tk.Label(text='Number guessing game!\n')
info = tk.Label(text='Enter a number between 1 and 100:\n')
entry_field = tk.Entry()
h_l = tk.Label()


n = 0
tries = 0


def setup():
    global n
    global tries
    n = random.randint(1, 100)
    h_l.config(text='New game!')
    confirmBtn.config(text='Submit Answer')
    tries = 0


def get_val():
    x = entry_field.get()
    print(entry_field.get())
    entry_field.delete(0, 'end')
    return x


def main(event):

    global tries
    try:
        g = int(get_val())
    except ValueError:
        h_l.config(text='Enter a number!')
        return

    if g > n:
        h_l.config(text='Too high!')
        tries += 1

    if g < n:
        h_l.config(text='Too low!')
        tries += 1

    if g == n:
        tries += 1
        h_l.config(text=f'Correct! {get_val()} was the answer!\nIt took you {tries} tries to guess the answer.\n '
                        f'Click New Game to start another game!')
        confirmBtn.config(command=setup, text='New Game')


confirmBtn = tk.Button()
root.bind('<Return>', main)
confirmBtn.bind('<Button-1>', main)
title.pack()
info.pack()
h_l.pack()
entry_field.pack()
confirmBtn.pack()
setup()
print('Setup complete')
root.mainloop()
