'''
Created on 2016年3月29日

@author: lyt1987
'''
import tkinter
class LanguageFrame(tkinter.Frame):
    
    def __init__(self, master=None):  
        tkinter.Frame.__init__(self, master)  
        self.grid(row=0, column=0, sticky="nsew")  
        self.createFrame()  
#         self.diffrent()
  
    def createFrame(self):   

        label_frame_top = tkinter.LabelFrame(self,height=30)  
        testBtn=tkinter.Button(label_frame_top,text="测试")
        testBtn.pack()
        label_frame_top.pack(fill="x")
  
        label_frame_center = tkinter.LabelFrame(self)  
        label_frame_center.pack(fill="x")  
  
        lfc_field_1 = tkinter.LabelFrame(label_frame_center)  
        lfc_field_1.pack(fill="x")  
        lfc_field_1_l = tkinter.Label(lfc_field_1, text="文件路径：", width=10)  
        lfc_field_1_l.pack(fill="y", expand=0, side=tkinter.LEFT)  
  
        lfc_field_1_b = tkinter.Button(lfc_field_1, text="清除：", width=10, height=1 )  
        lfc_field_1_b.pack(fill="none", expand=0, side=tkinter.RIGHT, anchor=tkinter.SE)  
  
        ##########文本框与滚动条  
        lfc_field_1_t_sv = tkinter.Scrollbar(lfc_field_1, orient=tkinter.VERTICAL)  #文本框-竖向滚动条  
        lfc_field_1_t_sh = tkinter.Scrollbar(lfc_field_1, orient=tkinter.HORIZONTAL)  #文本框-横向滚动条  
  
        lfc_field_1_t = tkinter.Text(lfc_field_1, height=15, yscrollcommand=lfc_field_1_t_sv.set,  
                                          xscrollcommand=lfc_field_1_t_sh.set, wrap='none')  #设置滚动条-不换行  
        #滚动事件  
        lfc_field_1_t_sv.config(command=lfc_field_1_t.yview)  
        lfc_field_1_t_sh.config(command=lfc_field_1_t.xview)  
  
        #布局  
        lfc_field_1_t_sv.pack(fill="y", expand=0, side=tkinter.RIGHT, anchor=tkinter.N)  
        lfc_field_1_t_sh.pack(fill="x", expand=0, side=tkinter.BOTTOM, anchor=tkinter.N)  
        lfc_field_1_t.pack(fill="x", expand=1, side=tkinter.LEFT)  
   
  
        label_frame_bottom = tkinter.LabelFrame(self) 
        testBtn2=tkinter.Button(label_frame_bottom,text="测试")
        testBtn2.pack()
        label_frame_bottom.pack(fill="x")
        
        pass  