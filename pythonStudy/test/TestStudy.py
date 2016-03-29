'''
Created on 2016年3月17日

@author: lyt
'''
import unittest

from  com.pallasli.simple.importFile import *;
from  com.pallasli.study.list import *; 
import com.pallasli.study.MyClass   as mycls
class TestCase(unittest.TestCase):
    def setUp(self):
        print("start") 
        global listData
        listData=[1,2]
        unittest.TestCase.setUp(self)

    def tearDown(self):
        print("end")
        unittest.TestCase.tearDown(self)

    def testMet1(self):
        print("test")
#         print(listData)
        listData=createEmptyListData()
        print(listData)
        insertData2listData(listData,5,2)
        assert(listData,[])
        insertData2listData(listData,45,3)
        insertData2listData(listData,55,4)
        insertData2listData(listData,52,6)
        setlistData(listData,[3,6,9,8],2,5)
        finallyList=createNotAllowAlterList()
#         finallyList[0]=2
        print(finallyList)
        print(listData)
        exec('print("exec")')
        importFn()
        testfor(listData)
        first,second=testReturnMul()
        print(first,second)
        mycls=  mycls().add();
        mycls().minus(mycls())
        createEmptyListData()
        pass

if __name__ == '__main__':
    unittest.main()