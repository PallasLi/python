'''
Created on 2016年3月24日

@author: lyt
'''
import tkinter

root = tkinter.Tk()

canvas = tkinter.Canvas(root, width=600, height=480, bg='white')
img = tkinter.PhotoImage(file = '1.png')
canvas.create_image(300, 50, image=img)
canvas.create_text(300, 75, text='Use Canvas', fill='blue')
canvas.create_text(302, 77, text='Use Canvas', fill='gray')
canvas.create_polygon(290, 114, 316, 114, 330, 130, 310, 146, 284, 146, 270, 130)
canvas.create_oval(280, 120, 320, 140, fill='white')
canvas.create_line(250, 130, 350, 130)
canvas.create_line(300, 100, 300, 160)
canvas.create_rectangle(90, 190, 510, 410, width=5)
canvas.create_arc(100, 200, 500, 400, start=0, extent=240, fill='pink')
canvas.create_arc(103, 203, 500, 400, start=241, extent=118, fill='red')
canvas.pack()

root.mainloop()


import tkinter

class MyButton:
    def __init__(self, root, canvas, label, type):
        self.root = root
        self.canvas = canvas
        self.label = label
        if type == 0:
            button = tkinter.Button(root, text='Draw Line', command=self.DrawLine)
        elif type == 1:
            button = tkinter.Button(root, text='Draw Arc', command=self.DrawArc)
        elif type == 2:
            button = tkinter.Button(root, text='Draw Rec', command=self.DrawRec)
        else:
            button = tkinter.Button(root, text='Draw Oval', command=self.DrawOval)
        button.pack(side = 'left')
    def DrawLine(self):
        self.label.text.set('Draw Line')
        self.canvas.SetStatus(0)
    def DrawArc(self):
        self.label.text.set('Draw Arc')
        self.canvas.SetStatus(1)
    def DrawRec(self):
        self.label.text.set('Draw Rectangle')
        self.canvas.SetStatus(2)
    def DrawOval(self):
        self.label.text.set('Draw Oval')
        self.canvas.SetStatus(3)

class MyCanvas:
    def __init__(self, root):
        self.status = 0
        self.draw = 0
        self.root = root
        self.canvas = tkinter.Canvas(root, bg='white', width=600, height=480)
        self.canvas.pack()
        self.canvas.bind('<ButtonRelease-1>', self.Draw)
        self.canvas.bind('<Button-2>', self.Exit)
        self.canvas.bind('<Button-3>', self.Del)
        self.canvas.bind_all('<Delete>', self.Del)
        self.canvas.bind_all('<KeyPress-d>', self.Del)
        self.canvas.bind_all('<KeyPress-e>', self.Exit)
    def Draw(self, event):
        if self.draw == 0:
            self.x = event.x
            self.y = event.y
            self.draw = 1
        else:
            if self.status == 0:
                self.canvas.create_line(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 1:
                self.canvas.create_arc(self.x, self.y, event.x, event.y)
                self.draw = 0
            elif self.status == 2:
                self.canvas.create_rectangle(self.x, self.y, event.x, event.y)
                self.draw = 0
            else:
                self.canvas.create_oval(self.x, self.y, event.x, event.y)
                self.draw = 0
    def Del(self, event):
        items = self.canvas.find_all()
        for item in items:
            self.canvas.delete(item)
    def Exit(self, event):
        self.root.quit()
    def SetStatus(self, status):
        self.status = status

class MyLabel:
    def __init__(self, root):
        self.root = root
        self.canvas = canvas
        self.text = tkinter.StringVar()
        self.text.set('Draw Line')
        self.label = tkinter.Label(root, textvariable=self.text, fg='red', width=50)
        self.label.pack(side='left')

root = tkinter.Tk()
canvas = MyCanvas(root)
label = MyLabel(root)
MyButton(root, canvas, label, 0)
MyButton(root, canvas, label, 1)
MyButton(root, canvas, label, 2)
MyButton(root, canvas, label, 3)
root.mainloop()

 