import tkinter as tk


def context(func):
    def wrapper(*args, **kwargs):
        x = f'-----{func.__name__}-----'
        print(x)
        print(func.__doc__)
        func(*args, **kwargs)
        print('-'*len(x)+'\n')

    return wrapper

class DataTypes:
    def __init__(self, _root):
        self.root = _root
        tuple_btn = tk.Button(text='Tuple', command=self.tuple_ex)
        list_btn = tk.Button(text='List', command=self.list_ex)
        dict_btn = tk.Button(text='Dict', command=self.dict_ex)
        set_btn = tk.Button(text='Set', command=self.set_ex)

        tuple_btn.pack()
        list_btn.pack()
        dict_btn.pack()
        set_btn.pack()



    @context
    def tuple_ex(self):
        """Shows that a tuple allows duplicate values, and are immutable after creation"""
        example_tuple = (1,2,3,4,5,5)
        print(example_tuple)
        try:
            example_tuple[2] = 4
        except Exception as e:
            print(f'Error: {e}')

    @context
    def list_ex(self):
        """Shows that lists can be appended to and are allowed to contain duplicate values"""
        example_list = [1,2,3,4,5,5]
        print(f'Original list: {example_list}')
        example_list.append(6)
        print(f'Appended list: {example_list}')

    @context
    def dict_ex(self):
        """Shows the structure of a dict, and shows that you can both append to it, and reference values by their key"""
        example_dict = {
            'name': 'John Smith',
            'age': 32,
            'money': 12.30
        }
        print(example_dict)
        print('Append \'12 Example Street\' to key \'address\'\n')
        example_dict['address'] = '12 Example Street'
        print(f'{example_dict}\nexample_dict[\'address\']: {example_dict['address']}')

    @context
    def set_ex(self):
        """Shows that sets can be used to perform operations on each other"""
        example_set = {1,2,3,4,5,6,7}
        diff_set = {2,4,6,8}
        print(f'{example_set} - {diff_set} = ')
        print(example_set-diff_set)

root = tk.Tk()
DataTypes(root)
root.mainloop()