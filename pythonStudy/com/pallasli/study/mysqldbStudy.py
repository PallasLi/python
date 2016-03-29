'''
Created on 2016年3月22日

@author: lyt
可以看出，连接数据库大致分为以下步骤：
  （1）建立和数据库系统的连接
  （2）获取操作游标
  （3）执行SQL，创建一个数据库（当然这一步不是必需的，因为我们可以用已经存在的数据库）
  （4）选择数据库
  （5）进行各种数据库操作
  （6）操作完毕后，提交事务（这一步很重要，因为只有提交事务后，数据才能真正写进数据库）
  （7）关闭操作游标
  （8）关闭数据库连接
  数据库连接对事务操作的方法：commit() 提交    rollback() 回滚
cursor用来执行命令的方法：
callproc(self,procname,args)
用来执行存储过程,接收的参数为存储过程名和参数列表,返回值为受影响的行数
execute(self, query, args)
执行单条sql语句,接收的参数为sql语句本身和使用的参数列表,返回值为受影响的行数
executemany(self, query, args)
执行单挑sql语句,但是重复执行参数列表里的参数,返回值为受影响的行数
nextset(self)
移动到下一个结果集
cursor用来接收返回值的方法：
fetchall(self)
接收全部的返回结果行
fetchmany(self, size=None)
接收size条返回结果行.如果size的值大于返回的结果行的数量,则会返回cursor.arraysize条数据
fetchone(self)
返回一条结果行
scroll(self, value, mode='relative')
移动指针到某一行，如果mode='relative',则表示从当前所在行移动value条,如果 mode='absolute',则表示从结果集的第一行移动value条。
'''
import pymysql 
try:
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='test',
    db='mysql')
    cur = conn.cursor()
    cur.execute("SELECT * FROM user")
    for r in cur.fetchall():
               print(r)
               
    cur.execute("insert ..")
    conn.commit()
    cur.close()
    conn.close()
except pymysql.Error as e:
    conn.rollback()

# blob=pymysql.escape_string(img)将二进制图片流转换为Blob
# cur.execute("insert into imges set Data='%s'" % blob)

# file.write(cur.fechone()['Data'])从数据库读取并存图片


with conn:
    cur=conn.cursor();
    cur.execute("create table...")
    cur.execute("insert ...")
    cur.execute("insert ...s% .....s%",("",""))#以prepared statement执行
    conn.commit()
    
    cur.execute("select ...")
    rows=cur.fetchall()
    rowCount=int(cur.rowcount)
    desc=cur.description#获取单个连接对象的描述，表头信息（字段）desc[0][0]，desc[0][1]
    for row in rows:
        print(row)
    for i in range(rowCount):
        row=cur.fechone()
        print(row[0],row[1])
        print(row["id"])