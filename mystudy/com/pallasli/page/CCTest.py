'''
Created on 2016年3月29日

@author: lyt1987
'''
from com.pallasli.page.LanguageStudyTest import LanguageFrame
import tkinter
class CCTestFrame(LanguageFrame):
    def diffrent(self):
        tkinter.Label(self,text="c++").pack()
    pass