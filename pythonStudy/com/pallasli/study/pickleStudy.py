'''
Created on 2016年3月23日

@author: lyt

python的pickle模块实现了基本的数据序列和反序列化。通过pickle模块的序列化操作我们能够将程序中运行的对象信息保存到文件中去，永久存储；通过pickle模块的反序列化操作，我们能够从文件中创建上一次程序保存的对象。

　　基本接口：

　　pickle.dump(obj, file, [,protocol])
　　注解：将对象obj保存到文件file中去。
　　　　　protocol为序列化使用的协议版本，0：ASCII协议，所序列化的对象使用可打印的ASCII码表示；1：老式的二进制协议；2：2.3版本引入的新二进制协议，较以前的更高效。其中协议0和1兼容老版本的python。protocol默认值为0。
　　　　　file：对象保存到的类文件对象。file必须有write()接口， file可以是一个以'w'方式打开的文件或者一个StringIO对象或者其他任何实现write()接口的对象。如果protocol>=1，文件对象需要是二进制模式打开的。

　　pickle.load(file)
　　注解：从file中读取一个字符串，并将它重构为原来的python对象。
　　file:类文件对象，有read()和readline()接口。
'''
import pickle  
import pprint
t1 = ('this is a string', 42, [1, 2, 3], None)  
a1 = 'apple'  
b1 = {1: 'One', 2: 'Two', 3: 'Three'}  
c1 = ['fee', 'fie', 'foe', 'fum']  
f1 = open('temp.pkl', 'wb')  
pickle.dump(a1, f1, True)  
pickle.dump(b1, f1, True)  
pickle.dump(c1, f1, True)  
f1.close()  
f2 = open('temp.pkl', 'rb')  
a2 = pickle.load(f2)  
print(a2)   
b2 = pickle.load(f2)  
print(b2  )
c2 = pickle.load(f2)  
print(c2  ) 
f2.close()  
print(pickle.format_version ) 
print(pickle.compatible_formats  )

data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()


pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()