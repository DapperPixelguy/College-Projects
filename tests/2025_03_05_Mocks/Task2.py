from datetime import datetime
from copy import copy
from math import isnan

products = [['Desktop', 799.00, 5], ['Laptop A', 1200.00, 6]]
sales = []


def stock_check():
    print("[Type, Cost, stock]")
    for i in products:
        print(i)


def add_stock():
    data = []
    existing = False
    p = None
    stock_type = input("Enter product name: ").capitalize()
    for product in products:
        if product[0] == stock_type:
            existing = True
            p = product
            break
    check = False
    while not check and not existing:
        try:
            cost1 = float(input("Enter Product cost up to 2 Decimal Places: "))
            cost = round(cost1, 2)
            check = True
        except:
            print("Entered value is not in required format.")

    check_1 = False
    while not check_1:
        try:
            stock = int(input("Enter the amount of stock: "))
            check_1 = True
        except:
            print("Entered value is not in required format.")
    if existing:
        p[2] += stock
    else:
        data.append(stock_type)
        data.append(cost)
        data.append(stock)
        products.append(data)


def addition():
    s_check = False
    q_check = False
    data1 = []
    while not s_check:
        s_type = input("Enter the Stock Type which you want to buy: ")

        for i in products:
            if s_type.lower() == i[0].lower():
                s_check = True

                while not q_check:
                    s_quantity = int(input("Enter the quantity for %s which you want to buy: " % s_type))
                    if s_quantity > i[2]:
                        print("Max available stock is: %s" % str(i[2]))
                    else:
                        i[2] = i[2] - s_quantity
                        q_check = True
                        break
        if not s_check:
            print("Entered stock does not exist")
        if s_check == True and q_check == True:
            data1.append(s_type.title())
            data1.append(s_quantity)
            break

    return data1


def price(value):
    for i in products:
        if value[0].lower() == i[0].lower():
            cost = value[1] * i[1]
            break
    return cost


def record_sale():
    data = []
    c_name = input("Enter Customer Name: ").title()
    comp_name = input("Enter Company Name: ").title()
    data.append(c_name)
    data.append(comp_name)
    now = datetime.now()
    date_time = now.strftime('%d/%m/%Y')
    data.append(date_time)
    print("Stock products are shown below")
    stock_check()
    items = []
    items.append(addition())
    while True:
        opt = input("Add more products? press y or n: ")
        if opt.lower() == "y":
            items.append(addition())
        elif opt.lower() == "n":
            break
        else:
            print("invalid option")
    data.append(items)
    sum = 0
    sub_total = 0
    for j in items:
        if isinstance(j, list):
            sum = sum + int(j[1])
            sub_total = sub_total + price(j)
    data.append(sub_total)
    if sum >= 5:
        final_total = sub_total - (sub_total/20)
        data.append(-(sub_total/20))
    else:
        final_total = sub_total
        data.append(-0)
    data.append(final_total)

    sales.append(data)
    print(sales[-1])
    print("Customer Receipt\n\n  Customer Name: {}\n  Company name: {}\n  Purchase date: {}\n \n "
          "Products (Type/Number) :\n {}\n \n Subtotal: £{:.2f}\n Total Minus Discount: £{:.2f} \n "
          "Final Total: £{:.2f}\n " .format(*sales[-1]))

def search_sales():
    print('Enter query values (leave blank to not apply criterion filter)')
    fields = ['customer', 'company', 'date', 'product']
    query = []
    total_fields = 0
    for field in fields:
        if field == 'product':
            _ = []
            p = ['product', 'quantity']
            for item in p:
                value = input(f'Enter {item} to search for: ').lower()
                if value:
                    _.append(value)
                else:
                    _.append(None)
        else:
            _ = input(f'Enter {field} to search for: ').lower()
        if _:
            query.append(_)
            total_fields += 1
        else:
            query.append(None)

    print(query)
    for sale in sales:
        found = 0
        for i, item in enumerate(query):
            if item:
                if isinstance(sale[i], list):
                    for entry in sale[i]:
                        for value in item:
                            if not value:
                                pass
                            elif value.isdigit():
                                if int(value) == entry[1]:
                                    found += 1
                            elif value == entry[0].lower():
                                found += 1

                else:
                    if item == sale[i].lower():
                        found += 1

        if total_fields == found:
            _ = ''
            for item in sale[3]:
                item = f'Product: {item[0]}\n Quantity: {item[1]}\n Price: £{price(item)}\n\n '
                _ += item
            temp_sale = sale.copy()
            temp_sale[3] = _.strip()
            print("Customer Receipt\n\n Customer Name: {}\n Company name: {}\n Purchase date: {}\n \n "
                  "Products (Type/Number):\n\n {}\n \n Subtotal: £{:.2f}\n Total Minus Discount: £{:.2f} \n "
                  "Final Total: £{:.2f}\n ".format(*temp_sale))


while True:
    option = int(input("Enter 1 for Stock Check \nEnter 2 for Add stock" 
                       "\nEnter 3 for Record Sale\nEnter 4 to search sales" 
                       "\nEnter 5 to exit\n"))
    if option == 1:
        stock_check()
    elif option == 2:
        add_stock()
    elif option == 3:
        record_sale()
    elif option == 4:
        search_sales()
    elif option == 5:
        break
    else:
        print("Invalid option, Select between 1 and 5")
