items = [1,2,3,4,5,6,7,8,9]
squares = []

for i, item in enumerate(items):
    squares.append(item**2)
    items.remove(item)

print(squares)

a1 = [1,4,9,16,25]
# a2 = [1,9,25,49,81]
a3 = 'Throws an error'
a4 = [1,4,9,16,25,36,49,64,81]

import tkinter as tk
items = ['Apple', 'Banana', 'Orange', 'Pear']
root = tk.Tk()

for item in items:
    button = tk.Button(text=item, command=lambda:print(item))
    button.pack()

root.mainloop()

a1 = 'Apple'
a2 = 'Orange'
# a3 = 'Pear'
a4 = 'Throws an error'
