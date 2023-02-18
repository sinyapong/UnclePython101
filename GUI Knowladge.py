from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import info
import money

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('500x400')

L1 = Label(GUI, text='การบ้าน EP.2',font=('Angsana New',30),fg='green')
L1.pack(ipadx=20, ipady=20, pady=20)


def Button1():
    name = f"{info.name} {info.lastname}"
    messagebox.showinfo('ชื่อ-นามสกุล', name)

def Button2():
    messagebox.showinfo("คุณมีเงิน 1000 บาท")


FB1 = Frame(GUI)
FB1.place(x=190, y=100)
B1 = ttk.Button(FB1, text='ชื่อนามสกุล', command=Button1)
B1.pack(ipadx=20, ipady=20)

B2 = ttk.Button(FB1, text='เงินมีอยู่กี่บาท', command=Button2)
B2.pack(ipadx=20, ipady=20)

GUI.mainloop()
