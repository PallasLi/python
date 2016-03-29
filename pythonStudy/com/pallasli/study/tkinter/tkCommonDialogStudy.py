#coding=utf-8
import tkinter.messagebox
def show():
    tkinter.messagebox.showinfo(title='aaa', message='bbb')
def creatfram():
    root = tkinter.Tk()
    b = tkinter.Button(root,text="关于",command=show)
    b.pack()
    root.mainloop()
creatfram()

import tkinter
from tkinter import messagebox

def cmd():
    global n
    global buttontext
    n += 1
    if n==1:
        messagebox.askokcancel('Python Tkinter', 'askokcancel')
        buttontext.set('askquestion')
    elif n==2:
        messagebox.askquestion('Python Tkinter', 'askquestion')
        buttontext.set('askyesno')
    elif n==3:
        messagebox.askyesno('Python Tkinter', 'askyesno')
        buttontext.set('showerror')
    elif n==4:
        messagebox.showerror('Python Tkinter', 'showerror')
        buttontext.set('showinfo')
    elif n==5:
        messagebox.showinfo('Python Tkinter', 'showinfo')
        buttontext.set('showwarning')
    else:
        n = 0
        messagebox.showwarning('Python Tkinter', 'showwarning')
        buttontext.set('askokcancel')

n = 0
root = tkinter.Tk()
buttontext = tkinter.StringVar()
buttontext.set('askokcancel')
button = tkinter.Button(root, textvariable=buttontext, command=cmd)
button.pack()
root.mainloop()
import tkinter
from tkinter import simpledialog

def inputStr():
    r = simpledialog.askstring('Python Tkinter', 'Input String', initialvalue = 'Python Tkinter')
    print(r)
def inputInt():
    r = simpledialog.askinteger('Python Tkinter', 'Input Integer')
    print(r)
def inputFloat():
    r = simpledialog.askfloat('Python Tkinter', 'Input Float')
    print(r)

root = tkinter.Tk()
btn1 = tkinter.Button(root, text='Input String', command=inputStr)
btn2 = tkinter.Button(root, text='Input Integer', command=inputInt)
btn3 = tkinter.Button(root, text='Input Float', command=inputFloat)

btn1.pack(side='left')
btn2.pack(side='left')
btn3.pack(side='left')

root.mainloop()

import tkinter
from tkinter import filedialog

def openfile():
    r = filedialog.askopenfilename(title='打开文件', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*')])
    print(r)
def savefile():
    r = filedialog.asksaveasfilename(title='保存文件', initialdir='d:\mywork', initialfile='hello.py')
    print(r)

root = tkinter.Tk()
btn1 = tkinter.Button(root, text='File Open', command=openfile)
btn2 = tkinter.Button(root, text='File Save', command=savefile)

btn1.pack(side='left')
btn2.pack(side='left')
root.mainloop()