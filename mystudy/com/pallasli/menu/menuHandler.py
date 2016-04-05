'''
Created on 2016年3月29日
主菜单处理
@author: lyt1987
'''

import tkinter  
from com.pallasli.page.LanguageStudyTest import LanguageFrame
from com.pallasli.page.JavaTest import JavaTestFrame
from com.pallasli.page.CCTest import CCTestFrame
from com.pallasli.page.CTest import CTestFrame
from com.pallasli.page.LuaTest import LuaTestFrame
from com.pallasli.page.PerlTest import PerlTestFrame
from com.pallasli.page.GoTest import GoTestFrame
from com.pallasli.page.ScalaTest import ScalaTestFrame
from com.pallasli.page.ShellTest import ShellTestFrame
from com.pallasli.page.JavascriptTest import JavascriptCTestFrame
from com.pallasli.page.PHPTest import PHPTestFrame
from com.pallasli.page.PythonTest import PythonTestFrame
from com.pallasli.page.RTest import RTestFrame
from com.pallasli.page.RubyTest import RubyTestFrame
from com.pallasli.page.ClojureTest import ClojureTestFrame

from com.pallasli.knowledge.PythonKnowledgeFrame import PythonKnowledgeFrame

from array import array
import os

def openFrame(lang,frame):
    keys=[]
    i=0
    for f in frame.children:
        print("第",i,"个")
        keys.append(f)
#         keys[i]=f
        i+=1
    for f in keys:
        frame.children[f].destroy()
    main_frame = eval(lang+"TestFrame")(frame)  
    main_frame.pack(fill="both")#mainloop() 
    pass
def openKnowledgeFrame(lang,frame):
    keys=[]#frame.children.keys()
    i=0
    for f in frame.children:
        print("第",i,"个")
        keys.append(f)
#         keys[i]=f
        i+=1
    for f in keys:
        frame.children[f].destroy()
    main_frame = eval(lang+"KnowledgeFrame")(frame)  
    main_frame.pack(fill="both")#mainloop() 
    pass

def rebuild():
#     os.system("pwd")
# #     os.system("cd /Users/lyt1987/Desktop/Github/python/mystudy")
#     os.system("rm -rf build dist")
#     os.system("/usr/local/bin/python3.5 setup.py py2app")
# #     os.system("cd /Users/lyt1987/Desktop/Github/python/mystudy/dist")
#     os.system("open dist/mystudy.app")
#     main_frame.quit()
    pass

def createMenuBar(frame,main_frame):
    
    menubar = tkinter.Menu(frame)
    fileSubMenu = tkinter.Menu(menubar, tearoff=0)
    fileSubMenu.add_command(label='Open')
    fileSubMenu.add_command(label='Save'  )
    fileSubMenu.add_command(label='Close')
    zskSubMenu=tkinter.Menu(menubar,tearoff=0)
    zskSubMenu.add_command(label="Java")
    zskSubMenu.add_command(label="Python",command=lambda:openKnowledgeFrame("Python",main_frame))
    zskSubMenu.add_command(label="Perl")
    zskSubMenu.add_command(label="Lua")
    zskSubMenu.add_command(label="PHP")
    zskSubMenu.add_command(label="Go")
    zskSubMenu.add_command(label="R")
    zskSubMenu.add_command(label="Ruby")
    zskSubMenu.add_command(label="shell")
    zskSubMenu.add_command(label="swift")
    zskSubMenu.add_command(label="C")
    zskSubMenu.add_command(label="C++")
    zskSubMenu.add_command(label="Ojbective-C")
    zskSubMenu.add_command(label="Scala")
    zskSubMenu.add_command(label="Clojure")
    zskSubMenu.add_command(label="javascript")
    zskSubMenu.add_command(label="android")
    cesiSubMenu=tkinter.Menu(menubar,tearoff=0)
    cesiSubMenu.add_command(label="Java",command=lambda:openFrame("Java",main_frame))
    cesiSubMenu.add_command(label="Python",command=lambda:openFrame("Python",main_frame))
    cesiSubMenu.add_command(label="Perl",command=lambda:openFrame("Perl",main_frame))
    cesiSubMenu.add_command(label="Lua",command=lambda:openFrame("Lua",main_frame))
    cesiSubMenu.add_command(label="PHP",command=lambda:openFrame("PHP",main_frame))
    cesiSubMenu.add_command(label="Go",command=lambda:openFrame("Go",main_frame))
    cesiSubMenu.add_command(label="R",command=lambda:openFrame("R",main_frame))
    cesiSubMenu.add_command(label="Ruby",command=lambda:openFrame("Ruby",main_frame))
    cesiSubMenu.add_command(label="shell",command=lambda:openFrame("Shell",main_frame))
    cesiSubMenu.add_command(label="C",command=lambda:openFrame("C",main_frame))
    cesiSubMenu.add_command(label="C++",command=lambda:openFrame("CC",main_frame))
    cesiSubMenu.add_command(label="Scala",command=lambda:openFrame("Scala",main_frame))
    cesiSubMenu.add_command(label="Clojure",command=lambda:openFrame("Clojure",main_frame))
    cesiSubMenu.add_command(label="javascript",command=lambda:openFrame("Javascript",main_frame))
    helpSubMenu=tkinter.Menu(menubar,tearoff=0)
    helpSubMenu.add_command(label="重新编译打开",command=rebuild)
    menubar.add_cascade(label='文件', menu=fileSubMenu)
    menubar.add_cascade(label='知识库', menu=zskSubMenu)
    menubar.add_cascade(label='测试环境', menu=cesiSubMenu)
    menubar.add_cascade(label='帮助', menu=helpSubMenu)
    frame.config(menu=menubar)
    pass