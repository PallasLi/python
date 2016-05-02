#coding=utf-8
'''
Created on 2016年3月24日
@author:lyt
'''
import tkinter2  
from com.pallasli.menu.menuHandler import createMenuBar

  
class MainFrame(tkinter.Frame):  
    def __init__(self, master=None):  
        tkinter.Frame.__init__(self, master)  
        self.grid(row=0, column=0, sticky="nsew")  
        self.createFrame()  
  
    def createFrame(self):  
                
        pass  
    
    
def main():  
    root = tkinter.Tk()  
    root.title("学习工具")
    root.columnconfigure(0, weight=1)  
    root.rowconfigure(0, weight=1)  
    root.geometry('1326x760')  #设置了主窗口的初始大小960x540 800x450 640x360  
  
  
    main_frame = MainFrame(root)  
    createMenuBar(root,main_frame)
    main_frame.mainloop()
    
if __name__ == "__main__":  
    main()  
    pass  