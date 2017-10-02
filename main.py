from tkinter import *


class main:
    def __init__(self, master):
        self.master = master
        self.master = rot
        self.master.geometry("350x150+520+300")
        self.master.title("SCHOOL DATABASE")
        Label(self.master, text="WHO ARE YOU?", font=("Helvetica", 30)).pack()
        self.a = Button(self.master, text="STUDENT", command=student).place(x=26, y=80)
        self.b = Button(self.master, text="TEACHER", command=teacher).place(x=230, y=80)



class student:
    def __init__(self):
        rot.destroy()
        self.stu = Tk()
        self.stu.geometry("300x180+520+300")
        self.stu.title("STUDENT")
        Label(self.stu, text="FIRST NAME").place(x=20, y=20)
        Label(self.stu, text="LAST NAME").place(x=20, y=40)
        Label(self.stu, text="CLASS").place(x=20, y=60)
        Label(self.stu, text="SECTION").place(x=20, y=80)
        Label(self.stu, text="ROLL NUMBER").place(x=20, y=100)
        self.fn = Entry(self.stu)
        self.fn.focus()
        self.ln = Entry(self.stu)
        self.cl = Entry(self.stu)
        self.se = Entry(self.stu)
        self.rn = Entry(self.stu)
        self.fn.place(x=120, y=20)
        self.ln.place(x=120, y=40)
        self.cl.place(x=120, y=60)
        self.se.place(x=120, y=80)
        self.rn.place(x=120, y=100)
        self.submit = Button(self.stu, text="SUBMIT", command=self.two).place(x=110, y=130)

    def two(self):
        self.ss()
        self.stu.quit()

    def ss(self):
        data = open("/root/python/school/database", "a")
        data.write("""
                """)
        data.write("First Name- ")
        data.write(self.fn.get())
        data.write("""
                """)
        data.write("Last Name- ")
        data.write(self.ln.get())
        data.write("""
                """)
        data.write("Class- ")
        data.write(self.cl.get())
        data.write("""
                """)
        data.write("Section- ")
        data.write(self.se.get())
        data.write("""
                """)
        data.write("Roll Number- ")
        data.write(self.rn.get())
        data.write("""
        ---------------------------------
        """)
        self.stu.destroy()
        print("------Given Information Saved------")

class teacher:
    def __init__(self):
        rot.destroy()
        self.tea = Tk()
        self.tea.title("TEACHER LOG IN")
        self.tea.geometry("300x180+520+300")
        Label(self.tea, text="NAME").place(x=20, y=40)
        Label(self.tea, text="PASSWORD").place(x=20, y=60)
        self.name = Entry(self.tea)
        self.name.focus()
        self.name.place(x=120, y=40)
        self.pas = Entry(self.tea, show="*")
        self.pas.place(x=120, y=60)
        Button(self.tea, text="LOGIN", command=self.ts).place(x=110, y=90)
        self.data = open("/root/python/school/database", "r+")

    def ts(self):
        if self.pas.get() == "rishu":
            self.tea.destroy()
            self.last = Tk()
            self.text = self.data.read()
            Label(self.last, text=self.text).grid(row=0, column=0)


rot = Tk()
gui = main(rot)
rot.mainloop()
