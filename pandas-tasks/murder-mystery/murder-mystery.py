from sqlite3 import *
from pandas import *
from tkinter import *

set_option('display.max_rows', 100)  # Shows all rows
set_option('display.max_columns', None)  # Shows all columns
set_option('display.width', None)
set_option('display.max_colwidth', None)
db_loc = '../data/murder-mystery.db'

conn = connect(db_loc)
cur = conn.cursor()

root = Tk()
root.geometry('300x250')


def wipe_screen():
    _list = root.winfo_children()

    widgets_to_clear = []

    for item in _list:
        widgets_to_clear.append(item)
        if item.winfo_children():
            widgets_to_clear.extend(item.winfo_children())

    for widget in widgets_to_clear:
        widget.pack_forget()


def read_table(table):
    df = read_sql_query(f'SELECT * FROM {table}', conn)
    return df


def list_tables():
    cur.execute('SELECT name FROM sqlite_master where type="table"')
    print('Available tables')
    [print(table[0]) for table in cur.fetchall()]


# print('''A crime has taken place and Curbal Crime Labs (CCL) needs your help.
#
# The crime is a murder that occurred sometime on Jan.15, 2018.
#       and a crime data analyst or curbalist as we call it at CCL,
#       is needed to help solve the case.
#
# All the crime files will be provided to you
#       but before we do that:
# ''')
# choice = input('Do you accept the challenge? (y/n)\n')
#
# if choice == 'y':
#     menu = True
# elif choice == 'n':
#     print('ok cya')
#     exit


current_selection = StringVar()


def confirm_entry(_vars, val):
    global current_selection
    print(_vars[1])
    if _vars[1] == 3:
        print('yeah')
        print(read_sql_query(
            f"SELECT description FROM crime_scene_report WHERE date = {_vars[0][0]} AND type = '{_vars[0][1]}' AND city = '{_vars[0][2]}'",
            conn))
        wipe_screen()
        title = Label(
            text=f'Showing description from the \n{_vars[0][0]} \n{_vars[0][1].capitalize()} \nIn {_vars[0][2]} ')
        description = Label(text=read_sql_query(
            f"SELECT description FROM crime_scene_report WHERE date = {_vars[0][0]} AND type = '{_vars[0][1]}' AND city = '{_vars[0][2]}'",
            conn)['description'].to_string(index=False))
        back = Button(text='Search again', command=crime_search)
        menu = Button(text='Return to main menu', command=set_menu)

        title.pack()
        description.pack()
        back.pack()
        menu.pack()
    else:
        entries = ['Enter a date in the format YYYYMMDD', 'Enter type of crime: ', 'Enter a description keyword: ',
                   'Enter a city: ']
        print('run')
        _vars[0].append(val)
        _vars[1] += 1
        current_selection.set(entries[_vars[1]])
        return _vars


def crime_search():
    global current_selection
    wipe_screen()
    title = Label(text='Searching Crime Database')
    _vars = [[], 0, 'Enter a date in the format YYMMDD']
    current_selection.set('Enter a date in the format YYMMDD')
    current_selection_label = Label(textvariable=current_selection)
    entry_box = Entry()
    confirm_button = Button(text='Confirm', command=lambda: _vars == confirm_entry(_vars, entry_box.get()))
    title.pack()
    current_selection_label.pack()
    entry_box.pack()
    confirm_button.pack()
    # df = read_table('crime_scene_report')
    # #print(df.head(5))
    # date = input('Enter a date in the format YYYYMMDD: ')
    # print(','.join(df['type'].unique()))
    # type = input('Enter type: ')
    # desc = input('Enter a description keyword: ')
    # print(','.join(df['city'].unique()))
    # city = input('Enter a city name: ')


# while menu:
#     #list_tables()
#     choice = input('''Would you like to:
#     1. Find a record in the crime database
#     2. Placeholder
#     3. Placeholder''')
#
#     if choice == '1':
#         crime_search()


def task_assign(task):
    if task == 'Find a record in the crime database':
        crime_search()


def set_menu():
    wipe_screen()
    title = Label(text='Main Menu')
    description = Label(text='Pick an option: ')

    option1 = StringVar()
    option1.set('Find a record in the crime database')
    _options = ['Find a record in the crime database',
                'Placeholder',
                'Placeholder']
    selection = OptionMenu(root, option1, *_options)

    confirm_button = Button(text='Perform task', command=lambda: task_assign(option1.get()))
    title.pack()
    description.pack()
    selection.pack()
    confirm_button.pack()


set_menu()
root.mainloop()
