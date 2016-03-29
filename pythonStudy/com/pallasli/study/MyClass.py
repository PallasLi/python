'''
Created on 2016年3月17日

@author: lyt
'''

# '''和"""可处理带格式的字符串
# '和"不带格式

class MyClass(object):
    "描述"
    '''
    classdocs
    '''

    def __init__(self, params):
        '''
        Constructor
        '''
    def minus(self):
        print(self)
    @staticmethod
    def add( ):
        "方法描述"
        try:
            c=1/1
            pass
        except RuntimeError as e:
            print(e)
        except IOError as e:
            print(e)
print(MyClass.__doc__)
print(MyClass.add.__doc__)
print(MyClass.__init__.__doc__)