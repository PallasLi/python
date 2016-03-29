'''
Created on 2016年3月18日

@author: lyt
'''
l=[122]
# list,dict,int,Long,float,complex,bool,str,unicode,tuple,xrange,set（集合）,frozenset(不可变集合),type(None)数据类型常量
print(isinstance(l, list))
b=None
print( type(None))
print( type(1))
print(isinstance(b, type(None))) 


class int(int):
    def __add__(self,other):# 偷偷重写Python一些内置算术运算，让程序出现意想不到的结果
        return int.__sub__(self,other)
a=int(3)
b=int(1)
c=a+b
print(a+b)# 调用第一个对象的add 结果为求差
print(1+a)# 调用第一个对象的add 结果为求和
print(b+1)
print(1+8)
print(10/8)
print(10//8)

# 内嵌函数
def fun1(x):
    def fun2(y):
        return  y
    print(fun2(x))

# 闭包
def fun3(x):
    def fun2(y):
        return x*y
    return fun2 
fun1(2) 
print(fun3(2)(3))


class CapStr(str):
    def __new__(cls,string):#对于不可变类型继承时需要对__new__进行重写 
        string=string.upper()
        print(type(string))
        print(str)
        return  str.__new__(str,string)
    def __del__(self):pass#所有引用被删除后执行
    def __init__(self):pass#初始化

print(CapStr("ss"))