'''
Created on 2016年3月30日

@author: lyt1987
'''
import tkinter
from tkinter.constants import BOTH,X,Y
import os
class LanguageFrame(tkinter.Frame):
    
    def __init__(self, master=None):  
        tkinter.Frame.__init__(self, master)  
#         self.grid(row=0, column=0, sticky="nsew")  
        self.createFrame()  
  
    def createFrame(self):   

#         标题工具栏
        label_frame_top = tkinter.LabelFrame(self,height=30)  
        testBtn=tkinter.Button(label_frame_top,text="测试")
        testBtn.pack()
        label_frame_top.pack(fill=X)
        
#         主模块栏
        label_frame_bottom = tkinter.LabelFrame(self) 
        testBtn2=tkinter.Button(label_frame_bottom,text="测试")
        testBtn2.pack()
        label_frame_bottom.pack(fill=BOTH)
        
        
#         分类导航栏
        label_frame_knowlegeType = tkinter.LabelFrame(label_frame_bottom)  
        knowledgeTypeListBox=tkinter.Listbox(label_frame_knowlegeType)
        os.system("ls /Users/lyt1987/Library/Mobile\ Documents/com~apple~TextEdit/Documents/study/Language/Python/")
        
        
        knowledgeTypeListBox.insert(0)
        label_frame_knowlegeType.pack(fill=Y) 
        
#         内容显示栏
        label_frame_center = tkinter.LabelFrame(label_frame_bottom)  
        label_frame_center.pack(fill=BOTH)  
   
  
        
        pass  