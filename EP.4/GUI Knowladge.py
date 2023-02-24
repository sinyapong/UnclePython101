from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import info
import money
from datetime import datetime

# ==================== CSV =======================================
import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8', newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)   # datalist = ['pen','pencil','eraser']
        
def readcsv():
    with open('data.csv', encoding='utf-8', newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data

# ====================================================================

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('800x400')

L1 = Label(GUI, text='การบ้าน EP.4',font=('Angsana New',30),fg='green')
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

# =============== SECTION RIGHT ============================

LF1 = ttk.LabelFrame(GUI, text='กรอกข้อมูลที่ต้องการเข้าไป')
LF1.place(x=400, y=100)

v_data = StringVar()
E1 = ttk.Entry(LF1, textvariable=v_data, font=('Angsana New', 25))
E1.pack(padx=10, pady=10)

def SaveData():
    t = datetime.now().strftime('%Y/%m/%d %H:%M:%S')
    data = v_data.get()
    text = [t, data]
    writecsv(text)
    v_data.set('')

B4 = ttk.Button(LF1, text='บันทึก', command=SaveData)
B4.pack(ipadx=20, ipady=20)



GUI.mainloop()
