'''
Created on 2016年3月24日

@author: lyt
'''
import tkinter
from tkinter import filedialog, StringVar 

def openfile():
    r = filedialog.askopenfilename(title='打开文件', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*')])
    print(r)
root = tkinter.Tk()
 
menu = tkinter.Menu(root)
submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='Open',command=openfile)
submenu.add_command(label='Save'  )
submenu.add_command(label='Close')
menu.add_cascade(label='File', menu=submenu)

submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='Copy')
submenu.add_command(label='Paste')
submenu.add_separator()
submenu.add_command(label='Cut')
menu.add_cascade(label='Edit', menu=submenu)

submenu = tkinter.Menu(menu, tearoff=0)
submenu.add_command(label='About')
menu.add_cascade(label='Help', menu=submenu)
variable=StringVar()
variable.set("3") 
tkinter.OptionMenu(root,variable , "one","two","3").pack()
root.config(menu=menu)
root.mainloop()