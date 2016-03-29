'''
Created on 2016年3月18日

@author: lyt
''' 
import math
import random
import re
import decimal
import fractions
import easygui

def openfile1():
    try:
        f=open('G:/new_frame/pyTest/com/pallasli/study/list2.py', 'w')
        for line in f:
            print(line)
    except OSError as e:
        print(e)
    else:
        print("no exception")
    finally:
        f.close()
def openfile2():
    try:
#         使用with则会自动关闭文件
        with open('G:/new_frame/pyTest/com/pallasli/study/list.py', 'r',encoding='utf-8') as f:
#           open(file, mode='r', buffering=_1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
            for line in f:
                print(line)
    except OSError as e:
        print(e)
    else:
        print("no exception") 
openfile1()
openfile2()
d='ddaf'

m=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
print([row[1] for row in m])
print([row[1]**2 for row in m])
print({row[1]**2 for row in m})
print([row[1] for row in m if row[0]<6])



print(dir(d))