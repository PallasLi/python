'''
Created on 2016年3月23日

@author: lyt
'''
import sqlite3
 
db = r"D:\pyWork\test.db"  #pyWork目录下test.db数据库文件
drp_tb_sql = "drop table if exists staff"
crt_tb_sql = """
create table if not exists staff(
  id integer primary key autoincrement unique not null,
  name varchar(100),
  city varchar(100)
);
"""
 
#连接数据库
con = sqlite3.connect(db)
cur = con.cursor()
 
#创建表staff
cur.execute(drp_tb_sql)
cur.execute(crt_tb_sql)
 
#插入记录
insert_sql = "insert into staff (name,city) values (?,?)"  #?为占位符
cur.execute(insert_sql,('Tom','New York'))
cur.execute(insert_sql,('Frank','Los Angeles'))
cur.execute(insert_sql,('Kate','Chicago'))
cur.execute(insert_sql,('Thomas','Houston'))
cur.execute(insert_sql,('Sam','Philadelphia'))
 
con.commit()
 
#查询记录
select_sql = "select * from staff"
cur.execute(select_sql)
 
#返回一个list，list中的对象类型为tuple（元组）
date_set = cur.fetchall()
for row in date_set:
  print(row)
 
cur.close()
con.close()