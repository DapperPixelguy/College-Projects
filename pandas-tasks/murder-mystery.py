from sqlite3 import *
from pandas import *

set_option('display.max_rows', 100)  # Shows all rows
set_option('display.max_columns', None)  # Shows all columns
set_option('display.width', None)
set_option('display.max_colwidth', None)
db_loc = 'data/murder-mystery.db'

conn = connect(db_loc)
cur = conn.cursor()


def read_table(table):
    df = read_sql_query(f'SELECT * FROM {table}', conn)
    return df


def list_tables():
    cur.execute('SELECT name FROM sqlite_master where type="table"')
    print('Available tables')
    [print(table[0]) for table in cur.fetchall()]

print('''A crime has taken place and Curbal Crime Labs (CCL) needs your help.
      
The crime is a murder that occurred sometime on Jan.15, 2018.
      and a crime data analyst or curbalist as we call it at CCL,
      is needed to help solve the case.
      
All the crime files will be provided to you
      but before we do that:
''')
choice = input('Do you accept the challenge? (y/n)\n')

if choice == 'y':
    menu = True
elif choice == 'n':
    print('ok cya')
    exit


def crime_search():
    df = read_table('crime_scene_report')
    #print(df.head(5))
    date = input('Enter a date in the format YYYYMMDD: ')
    print(','.join(df['type'].unique()))
    type = input('Enter type: ')
    desc = input('Enter a description keyword: ')
    print(','.join(df['city'].unique()))
    city = input('Enter a city name: ')

    print(read_sql_query(f"SELECT * FROM crime_scene_report WHERE date = {date} AND type = '{type}' AND city = '{city}'", conn))

while menu:
    #list_tables()
    choice = input('''Would you like to:
    1. Find a record in the crime database
    2. Placeholder
    3. Placeholder''')

    if choice == '1':
        crime_search()



#print(read_table('person'))
