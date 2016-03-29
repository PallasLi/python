#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      lyt
#
# Created:     16/03/2016
# Copyright:   (c) lyt 2016
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from  com.pallasli.simple.importFile import *;

def main():
    a=10
    b=a*a-7
    print(b)
    if b>10:
        print("b>10")
    else:
        print(b<=10)
    c=[1,'q']
    print(c)
    b=c#b与c指向同一列表
    print(b)
    b[0]=23
    print(c)
    d=range(7)#从0开始（包含0），到7结束（不含7），步数为1
    e=range(3,9)#从3开始（包含3），到9结束（不含9），步数为1
    f=range(3,9,3)#从3开始（包含3），到9结束（不含9），步数为3
    for i in d :
        print(i)
    for i in range(1,len(d)) :
        print(i)
    for i in e :
        print(i)
    for i in f :
        print(i)
    print(len(d))
    i=3
    while i<len(d):
        print(i)
        i=i+1
    hello_string="hello world"
    strlist=hello_string.split(' ');
    print(strlist)
    print(hello_string.find('*'))
    print(hello_string.find('l'))
    print(hello_string.index('l'))
    print(hello_string.count('l'))
    print(eval("3+4"))
    print(type("3+4"))
    pass
##阶乘函数
def factorial(i):
    if i==1:
        return i
    else:
        return i*(factorial(i-1))

def testprint(i):
    print(input("输入一个数字"))
    print(eval(input("输入一个可使用i的表达式")))
if __name__ == '__main__':
    main()
    print(factorial(4))
    importFn()
##    testprint(4)