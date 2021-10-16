import tkinter


def hello(event):
    name = entry1.get()
    label1['text'] = 'Hello ' + name


print(tkinter.TkVersion)

root = tkinter.Tk()
root.geometry('600x300')

label1 = tkinter.Label(master=root, text='Hello! Enter your name', fg='green', font='Arial 12')
entry1 = tkinter.Entry(master=root, width=10, font='Arial 20')
button1 = tkinter.Button(master=root, text='Ok', width=10, font='Arial 20')

# label1.bind()
button1.bind('<Button-1>', hello)

label1.place(x=120,y=20)
entry1.place(x=286,y=20)
button1.place(x=170,y=100)

root.mainloop()