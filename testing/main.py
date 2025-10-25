import datetime
import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime as dt

df = pd.read_csv('Task_4a_data.csv', index_col='ID')

#main menu
def menu():
    print("\t\t****MAIN MENU****")
    print('1) Enter sales records')
    print('2) Run reports')
    x = int(input(""))
    return x

#reports menu
def menu2():
    print("**** Reports Dashboard ****")
    print("1. All Sales")
    print("2. Individual Employee Check")
    print("3. Employee Comparison")
    print("4. Bonus Reports")
    print("5. Total sale of each region within date ranges")
    x = int(input(""))
    return x


def total_each (df_r, date1, date2):
    df_r = df_r.groupby(['Region']).sum()
    df_r = df_r.iloc[:, 2:]
    print(df_r)
    df_r=df_r.T
    df_r.reset_index(inplace=True)
    print(df_r)
    #print(df_r)
    df_r['ID1'] = pd.to_datetime(df_r['index'], format='%d/%m/%Y')
    date1 = pd.to_datetime (date1, format = '%Y/%m/%d')
    date2= pd.to_datetime (date2, format = '%Y/%m/%d')
    mask = (df_r['ID1'] >= date1) & (df_r['ID1'] <= date2)
    df_search= df_r.loc[mask]
    del df_search ['ID1']
    del df_search ['index']
    print (df_search)
    k = df_search.sum()
    print(k)
    k.plot.bar()
    plt.show()

def ind_emp_check(df_r, id, date1, date2):
    df_r = df_r.loc[df.index == id]

    df_r = df_r.T[3:]
    df_r.reset_index(inplace=True)
    df_r['ID1'] = pd.to_datetime(df_r['index'], format='%d/%m/%Y')
    date1 = pd.to_datetime(date1, format='%d/%m/%Y')
    date2 = pd.to_datetime(date2, format='%d/%m/%Y')
    mask = (df_r['ID1'] >= date1) & (df_r['ID1'] <= date2)
    df_search = df_r.loc[mask]
    print(df_search)
    print('Total by id = {} is {}'.format(id, sum(df_search[id])))

    plt.bar(df_search['index'], df_search[id])
    plt.xticks(rotation=90)
    plt.show()

y = menu()
while y == 1 or y == 2:
    if y == 1:
        try:
            ID = int(input("Enter the Staff ID "))
            if ID not in df.index.values:
                print('yes')

            date1 = input("Enter Date in dd/mm/yy: ")
            day, month, year = date1.split("/")
            date1 = datetime.date(int(year), int(month), int(day))

            if datetime.datetime.strptime(date1.strftime('%d/%m/%Y'), '%d/%m/%Y') > datetime.datetime.strptime(
                    dt.today().strftime('%d/%m/%Y'), '%d/%m/%Y'):
                print("Date is in the future")
            else:
                cost = float(input("Enter the cost : "))
                df.loc[ID, date1.strftime('%d/%m/%Y')] = cost
            # df.to_csv('test2.csv')
        except:
            print("\n\nError Occurred Please try again\n\n")
            y = menu()

    if y == 2:
        x = menu2()
        if x == 1:
            try:
                id = int(input("Enter the Employee Id : "))
                s_date = input("Enter Starting Date in dd/mm/yyyy: ")
                day, month, year = s_date.split("/")
                s_date = datetime.date(int(year), int(month), int(day))

                e_date = input("Enter Date in dd/mm/yyyy: ")
                day, month, year = e_date.split("/")
                e_date = datetime.date(int(year), int(month), int(day))

                s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
                ind_emp_check(df, id, s_date, e_date)
            except:
                print("\n\nError Occurred Please try again\n\n")
                x = menu2()

        if x == 5:
            print('regions')
          #  try:
            s_date = input("Enter Starting Date in dd/mm/yyyy: ")
            day, month, year = s_date.split("/")
            s_date = datetime.date(int(year), int(month), int(day))

            e_date = input("Enter Date in dd/mm/yyyy: ")
            day, month, year = e_date.split("/")
            e_date = datetime.date(int(year), int(month), int(day))

            s_date = datetime.datetime.strptime(s_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
            e_date = datetime.datetime.strptime(e_date.strftime('%d/%m/%Y'), '%d/%m/%Y')
            total_each(df, s_date, e_date)
            # except Exception as e:
            #     print(f'Encountered exception {e}')

        else:
            x = menu2()
    else:
        x = menu()
    x = menu()
