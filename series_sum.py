from tkinter import *

def series1_sum():
    ent2.delete(0, 'end')
    n = int(ent1.get())
    ent2.insert(0, int((n * (n + 1)) / 2))

def series2_sum():
    ent2.delete(0, 'end')
    n = int(ent1.get())
    if n % 2 == 0:
        n -= 1
    ent2.insert(0, int(((n + 1) / 2) ** 2))

def series3_sum():
    ent2.delete(0, 'end')
    n = int(ent1.get())
    ent2.insert(0, int((n / 2) * ((n / 2) + 1)))

def series4_sum():
    ent2.delete(0, 'end')
    n = int(ent1.get())
    ent2.insert(0, int((n * (n + 1) * ((2 * n) + 1)) /6))

def clear():
    ent2.delete(0, 'end')
    ent1.delete(0, 'end')

app = Tk()
app.configure(bg="#ffe599")
app.maxsize(width=600, height=600)
app.minsize(width=600, height=600)

lbl1 = Label(app, text="Sum of the Series", font=("Bold", 26), bg="#ffe599", borderwidth= 3, relief=RAISED)
lbl1.place(x = 160)

lbl2 = Label(app, text="N",padx=57, pady=10, font=("Bold", 15), bg="#ffe599", borderwidth= 3, relief=RIDGE)
lbl2.place(x=50, y = 50)

ent1 = Entry(app, width=32, font="Helvetica 15") # input entry
ent1.place(x=190, y= 50, height= 48)
ent1.focus()

lbl3 = Label(app, text="RESULT",padx=26, pady=10, font=("Bold", 15), bg="#ffe599", borderwidth= 3, relief=RIDGE)
lbl3.place(x=50, y = 100)

ent2 = Entry(app, width=32,font="Helvetica 15") # output entry
ent2.place(x=190, y= 100, height= 48)

series1 = Button(app,bg="#ffdf7f",activebackground="#bfe9f7", text="1 + 2 + 3 + 4 + . . . . . + N",font=("Bold",16), width=69, height=2, command=series1_sum)
series1.place(x=50, y=170, width=495)

series2 = Button(app,bg="#ffdf7f",activebackground="#bfe9f7", text="1 + 3 + 5 + 7 + . . . . . + N",font=("Bold",16), width=69, height=2, command=series2_sum)
series2.place(x=50, y=250, width=495)

series3 = Button(app,bg="#ffdf7f",activebackground="#bfe9f7", text="2 + 4 + 6 + 8 + . . . . . + N",font=("Bold",16), width=69, height=2, command=series3_sum)
series3.place(x=50, y=330, width=495)

series4 = Button(app,bg="#ffdf7f",activebackground="#bfe9f7", text="1^2 + 2^2 + 3^2 + 4^2 + . . . . . + N",font=("Bold",16), width=69, height=2, command=series4_sum)
series4.place(x=50, y=410, width=495)

btn1 = Button(app, text="CLEAR",activebackground="green",font=("Bold", 11), width=20, height=3, command=clear, bg="#99cccc")
btn1.place(x=70, y=500)
btn2 = Button(app, text="EXIT",font=("Bold", 11),activebackground="red",width=20, height=3, command=exit, bg="#f05dc5")
btn2.place(x= 340, y = 500)

app.mainloop()

# Author: Md. Mursalatul Islam Pallob
# email: mursalatul.pallob@gmail.com