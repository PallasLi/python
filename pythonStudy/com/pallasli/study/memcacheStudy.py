'''
Created on 2016年3月23日

@author: lyt
'''
import pymysql
import memcache
import sys
import time
def get_data(mysql_conn):
#    nn = raw_input("press string name:")
    mc = memcache.Client(['127.0.0.1:11211'],debug=1)
    t1 =time.time()
    value = mc.get('zhoujinyia') 
    if value == None:
        t1 = time.time()
        print (t1)
        query = "select company,email,sex,address from uc_user_offline where realName = 'zhoujinyia'"
        cursor= mysql_conn.cursor()
        cursor.execute(query)
        item = cursor.fetchone()
        t2 = time.time()
        print (t2)
        t = round(t2-t1)
        print ("from mysql cost %s sec" %t )
        print (item)
        mc.set('zhoujinyia',item,60)
    else :
        t2 = time.time()
        t=round(t2-t1)
        print ("from memcache cost %s sec" %t)
        print (value)
if __name__ =='__main__':
    mysql_conn = pymysql.connect(host='127.0.0.1',user='root',passwd='123456',db='member',port=3306,charset='utf8')
    get_data(mysql_conn)