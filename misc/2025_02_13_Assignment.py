import tkinter as tk
from tkinter import ttk
from datetime import date

class MobilePhone:
    has_touchscreen = True

    def __init__(self, brand, model, new_price, new_year):
        self.brand = brand
        self.model = model
        self.new_price = new_price
        self.new_year = new_year

    def os(self):
        if self.brand == "Apple":
            #print ("iOS")
            return 'iOS'
        else:
            #print ("Android")
            return 'Android'

class MobileViewer:
    def __init__(self, _root):
        self.root = _root
        self.geometry = self.WIDTH, self.HEIGHT = 400, 400
        self.root.geometry(f'{self.geometry[0]}x{self.geometry[1]}')
        self.title_var = tk.StringVar()
        self.title_var.set('Main Menu')
        self.title = tk.Label(root, textvariable=self.title_var)
        self.menubar = tk.Frame(root)
        self._f = tk.Frame(root)
        self.view_frame = tk.Frame(root)
        self.title.pack()
        self.buttons = []
        self.change_packing('main')



    def change_packing(self, layout):
        if layout == 'main':
            self.root.title('Main Menu')
            edit = ttk.Button(self.menubar, text='Add', command=self.edit)
            view = ttk.Button(self.menubar, text='View', command=self.view)
            edit.grid(row=0, column=0)
            view.grid(row=0, column=1)
            self.menubar.grid_columnconfigure(0, weight=1)
            self.menubar.pack()
            self._f.destroy()
            self._f = tk.Frame(root)
            self.view_frame.destroy()
            self.view_frame = tk.Frame(root)


    def view(self):
        self.menubar.pack_forget()
        self.view_frame.pack()
        self.root.title('Viewing Phones')
        self.title_var.set('Viewing Phones')
        self.buttons = []
        for p in phones:
            _ = ttk.Button(self.view_frame, text=f'{p.brand} {p.model} [{MobilePhone.os(p)}]', command=lambda _p=p: print_info(_p))
            _.pack()
            self.buttons.append(_)

        def print_info(phone):
            print(f'New Price: £{phone.new_price}')
            print(f'New Year: {phone.new_year}\n')
            current_year = date.today().year
            print(f'Current Year: {current_year}')
            current_price = float(phone.new_price) * (0.8 ** (date.today().year - phone.new_year))
            print(f'Current value: £{current_price}\n')
            sales_price = current_price*1.1
            print(f'Sales price: £{sales_price}')
            purchase_price = current_price*0.6
            print(f'Purchase price: £{purchase_price}')

            print('Phone sold!')
            phones.remove(phone)
            self.change_packing('main')
            self.view()
            print('')

        def leave_view():
            self.buttons = []
            self.change_packing('main')

        tk.Button(self.view_frame, text='Return', command=leave_view).pack()


    def edit(self):
        self.menubar.pack_forget()
        self.root.title('Adding Phone')
        self.title_var.set('Adding Phone')
        fields = ['Brand', 'Model', 'Original New Price', 'New Year']
        entries = {}
        for i, field in enumerate(fields):
            tk.Label(self._f, text=field).grid(row=i, column=0)
            entries[field] = tk.Entry(self._f)
            entries[field].grid(row=i, column=1)
        self._f.pack()

        def get_text(_entries):
            for field, entry in _entries.items():
                if entry.get():
                    print(entry.get())
                else:
                    return
            print(f'Brand: {_entries['Brand'].get()}')
            phones.append(MobilePhone(_entries['Brand'].get(), _entries['Model'].get(), int(_entries['Original New Price'].get().strip('$£')), int(_entries['New Year'].get())))
            self.change_packing('main')

        confirm = tk.Button(self._f, text='Enter', command=lambda:get_text(entries))
        confirm.grid(column=0, columnspan=2)


phones = []
Jim_phone = MobilePhone("Apple", "iPhone 15", 659, 2020)
Aisha_phone = MobilePhone("Samsung", "Galaxy S22", 549, 2015)

MobilePhone.os(Jim_phone)

phones.append(Jim_phone)
phones.append(Aisha_phone)

root = tk.Tk()
MobileViewer(root)
root.mainloop()
