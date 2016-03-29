'''
Created on 2016年3月22日

@author: lyt
'''
import tkinter   
from tkinter.constants import LEFT, END, SINGLE, RIGHT, Y, BOTH, HORIZONTAL
from sqlalchemy.sql.expression import column
from tkinter import StringVar
from pymongo.common import validate
from select import select

class myApp: 
    def __init__(self,master):
        frame=tkinter.Frame(master)
        tklable1=tkinter.Label(frame,text="作品")
        tklable1.grid(row=0,column=0)
#         tklable1.pack() 
        v=StringVar()
        def test(content,reason,name):
            print("%p "+content)
            print("%v "+reason)
            print("%s "+name)
            print(content=='1')
            if content=='1' :
                return True
            else:
                return False 
        testCMD=frame.register(test)
        self.tkinput1=tkinter.Entry(frame ,textvariable=v,validate="focusout",validatecommand=(testCMD,'%P','%v',"%W"))
        self.tkinput1.grid(row=0,column=1)
#         self.tkinput1.pack()
        tklable2=tkinter.Label(frame,text="描述")
        tklable2.grid(row=1,column=0)
#         tklable2.pack() 
        self.tkinput2=tkinter.Text(frame )
        self.tkinput2.grid(row=1,column=1)
#         self.tkinput2.pack()
        tkbutto=tkinter.Button(frame,width=10,text="info",bg="red",fg="blue",padx=10,command=lambda: self.info(self.tkinput1))
        tkbutto.grid(row=2,column=1)
        def func1(event):
            print("按下")
        def func2(event):
            print("按下")
            # <Button-1>：鼠标左击事件
            # <Button-2>：鼠标中击事件
            # <Button-3>：鼠标右击事件
            # <Double-Button-1>：双击事件
            # <Triple-Button-1>：三击事件
        tkbutto.bind('<Button-1>', func1, True)
        tkbutto.bind('<Button-3>', func2, True) 
#         tkbutto.pack(side=LEFT) 
        frame.pack( )
    def info(self,tkinput):
        print(tkinput.get( )) 
        print(self.tkinput2.get('0.0',END)) 

app = tkinter.Tk()
# Code to add widgets will go here...


tklable=tkinter.Label(app,text="书籍") 
tklable.pack() 

tkscroll=tkinter.Scrollbar(app)
tkscroll.pack(side=RIGHT,fill=BOTH)

tkList=tkinter.Listbox(app,selectmode=SINGLE,yscrollcommand=tkscroll.set)
tkList.pack(side=LEFT,fill=BOTH)
for i in range(1,20):
    tkList.insert(END, '1'+str(i)+"firstafffffffffffffffffffffffffffffffffffffffffffffffffff")
    tkList.insert(END, '1'+str(i)+"second")
 

root = tkinter.Tk()

w = tkinter.Canvas(root, width=200, height=100)
w.pack()

# 画一条黄色的横线
w.create_line(0, 50, 200, 50, fill="yellow")
# 画一条红色的竖线（虚线）
w.create_line(100, 0, 100, 100, fill="red", dash=(4, 4))
# 中间画一个蓝色的矩形
w.create_rectangle(50, 25, 150, 75, fill="blue")
  
root = tkinter.Tk()

w1 = tkinter.Message(root, text="这是一则消息", width=100)
w1.pack()

w2 = tkinter.Message(root, text="这是一则骇人听闻的长长长长长消息！", width=100)
w2.pack()
 
w = tkinter.Spinbox(app, from_=0, to=10)
w.pack()
 
tkinter.Scale(app, from_=0, to=42).pack()
tkinter.Scale(app, from_=0, to=200, orient=HORIZONTAL).pack()
 
def create():
    top = tkinter.Toplevel()
    top.title("FishC Demo") 
    msg = tkinter.Message(top,  text="I love FishC.com!")
    msg.pack()

tkinter.Button(app, text="创建顶级窗口", command=create).pack()

import tkinter.messagebox
tkinter.messagebox.askokcancel("title", "message")
myApp(app)
tkinter.mainloop()
