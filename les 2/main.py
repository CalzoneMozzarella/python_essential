import tkinter

user_login = 'Alex'
user_pass = '12345'
button_handler_i = 0


def forget_widgets():
    sign_in_label.place_forget()
    login_label.place_forget()
    login_entry.place_forget()
    pass_label.place_forget()
    pass_entry.place_forget()
    submit_button.place_forget()
    remember_checkbutton.place_forget()
    attempt_label.place_forget()


def button_handler(event):
    global button_handler_i
    global login_label
    login = login_entry.get()
    password = pass_entry.get()

    if login == user_login and password == user_pass:
        forget_widgets()
        welcome_label['text'] = 'Welcome,\n {}!'.format(user_login)
        welcome_label.place(x=50, y=30)
    else:
        if login != user_login:
            login_label['fg'] = 'red'
        else:
            login_label['fg'] = 'black'

        if login != user_pass and password != user_pass:
            pass_label['fg'] = 'red'
        else:
            pass_label['fg'] = 'black'

        attempt_label['text'] = '{} attempts left'.format(3 - button_handler_i)

        if button_handler_i == 0:
            attempt_label.place(x=150, y=300)
            button_handler_i += 1
        elif button_handler_i <= 2:
            button_handler_i += 1
        elif button_handler_i > 2:
            forget_widgets()
            welcome_label['text'] = 'You are \n  a looser...'
            welcome_label.place(x=50, y=30)


root = tkinter.Tk()
root.geometry('400x500')

sign_in_label = tkinter.Label(master=root, text='Sign in', font='Arial 25')
login_label = tkinter.Label(master=root, text='login:', font='Arial 15')
login_entry = tkinter.Entry(master=root, width=15, font='Arial 15')
pass_label = tkinter.Label(master=root, text='password:', font='Arial 15')
pass_entry = tkinter.Entry(master=root, width=15, font='Arial 15')
submit_button = tkinter.Button(master=root, text='Submit', width=10, font='Arial 15')
remember_checkbutton = tkinter.Checkbutton(master=root, text='Remember me', font='Arial 12')
attempt_label = tkinter.Label(master=root, text='{} attempts left'.format(3 - button_handler_i),
                              font='Arial 8', fg='red')
welcome_label = tkinter.Label(master=root, text='Welcome', font='Arial 40')

submit_button.bind('<Button-1>', button_handler)

sign_in_label.place(x=10, y=10)
login_label.place(x=10, y=80)
login_entry.place(x=120, y=80)
pass_label.place(x=10, y=130)
pass_entry.place(x=120, y=130)
remember_checkbutton.place(x=10, y=180)
submit_button.place(x=120, y=230)

root.mainloop()
