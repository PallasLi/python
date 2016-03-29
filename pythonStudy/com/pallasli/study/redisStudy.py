import redis 
# with  open('aa.txt',"w") as f:
#     f.close
f = open('aa.txt')
while True:
    line = f.readline().strip().split(' # ')
    if line == ['']:
        break
    UserName,Pwd,Email = line
#    print name.strip(),pwd.strip(),email.strip()
    rc = redis.StrictRedis(host='127.0.0.1',port=6379,db=15)
    rc.hset('Name:' + UserName,'Email',Email)
    rc.hset('Name:' + UserName,'Password',Pwd)
f.close()
alluser = rc.keys('*')
#print alluser
print ("===================================读出存进去的数据===================================")
for user in alluser:
    print (' # '.join((user.split(':')[1],rc.hget(user,'Password'),rc.hget(user,'Email'))))