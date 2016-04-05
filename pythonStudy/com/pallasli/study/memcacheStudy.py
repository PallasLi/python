'''
Created on 2016年3月23日

@author: lyt
'''
import memcache


def get_data():
    mc = memcache.Client(['127.0.0.1:11211'],debug=1)
    value = mc.get('zhoujinyia') 
    print (value)
    mc.set('zhoujinyia',"周金亚",60)
    value = mc.get('zhoujinyia') 
    print (value)
if __name__ =='__main__':
    get_data()
    
