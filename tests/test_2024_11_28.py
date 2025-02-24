import tkinter as tk
# Requires ./data to call upon password.txt


class PasswordChecker:
    def __init__(self, root):
        self.root = root
        self.root.geometry('500x200')
        self.root.title("Password Checker")

        self.current_activity = tk.StringVar()
        self.current_activity.set('Password Checker')
        self.current_activity_label = tk.Label(self.root, textvariable=self.current_activity)

        self.error = tk.StringVar()
        self.error_display = tk.Label(textvariable=self.error)

        self.password_field = tk.Entry()
        self.attempts = 0
        self.start_button = tk.Button(text='Check password', command=self.password_checker)

        self.current_activity_label.pack()

        self.password_field.pack()
        self.start_button.pack()
        self.error_display.pack()

        self.data = open('data/passwords.txt', 'r')
        self.f = [line.strip('\n') for line in self.data.readlines()]

    def password_checker(self):
        symbols = ['!', '"', '£', '$', '%', '^', '&', '*', '(', ')', '_', '-']
        symbol_count = 0
        password = self.password_field.get()
        flag = False

        error_string = ''

        if len(password) < 6:
            error_string += 'Password must be of length 6 or higher\n'
            flag = True

        if password.lower() == password:
            error_string += 'Password must contain at least one uppercase character\n'
            flag = True

        for symbol in symbols:
            if symbol not in password:
                symbol_count += 1

        if symbol_count == len(symbols):
            error_string += 'Password must contain a symbol\n'
            flag = True

        if ' ' in list(password.strip()):
            error_string += 'Password must not contain spaces\n'
            flag = True

        if password in self.f:
            error_string += 'Password already exists.\n'
            flag = True

        if self.attempts < 5 and flag:
            self.attempts += 1
            error_string += f'You have {5 - self.attempts} attempt(s) left'
            self.error.set(error_string)

        if self.attempts == 5:
            print('Too many attempts')
            root_.destroy()

        if not flag:
            print('Password ok!')
            self.error.set('Password ok!')
            self.password_field.configure(state="disabled")


root_ = tk.Tk()
PasswordChecker(root_)
root_.mainloop()
