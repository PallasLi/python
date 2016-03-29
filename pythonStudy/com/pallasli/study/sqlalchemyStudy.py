'''
Created on 2016年3月23日

@author: lyt
'''
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base() 

class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))

engine = create_engine('mysql+mysqlconnector://root:XXXXX@localhost:3306/TUZHI')
DBSession = sessionmaker(bind=engine)

session = DBSession()
new_user = User(id='4', name='Huangyi')
session.add(new_user)
session.commit()
#session.close()

##进行查询
#session = DBSession()
user = session.query(User).filter(User.id=='4').one()
print ('type:', type(user))
print ('name:', user.name)
session.close()