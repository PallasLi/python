'''
Created on 2016年3月17日

@author: lyt
'''
# 
# 
# 字典类型即json对象   list(json)将json转换为list
# 字典  setDefault(key[,defaultVale])设置默认值，setDefault()恢复默认值
# 
# 集合set(list)  set(str)   一组无重复的无序对象
# 
# 
# 
# 
# 
# 
# 





def testReturnMul():
    return (1,2)

def insertData2listData(listData,data,index):
    print(index)
    if  index<len(listData):
        listData.insert(index, data)
    else:
        listData.append(data)
    
def setlistData(listData,data,begin,end):
    listData[begin:end]=data;
    
def createEmptyListData(): 
    tmp=(1,2,3,4)
    tmp=tmp[:2]+('0',)+tmp[2:]
    print(tmp)
    return [1,34]

def createNotAllowAlterList():
    return (1,)

# 如果参数设置默认值，而后面的参数没有默认值，则调用时不能省略该参数
# 单可以通过指定参数来设置
def testfor(listData=[3,4,5],nex=2):
    print(nex)
    for i in iter(listData):
        print(i)
#         print(listData[i])

createEmptyListData()
testfor(nex=4)