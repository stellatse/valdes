#!/usr/bin/python
# -*- coding: utf-8 -*-
import web
import settings
import hashlib
from datetime import datetime as dt
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Text

#engine = create_engine('mysql+mysqldb://root:tingfeng@localhost/express', echo=True)
engine = create_engine('sqlite:///oaksu.db')
#db = web.database(dbn='mysql', db='express', user=settings.MYSQL_USERNAME, pw=settings.MYSQL_PASSWORD)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(30))
    fullname = Column(String(50))
    password = Column(String(32), nullable = False)
    email = Column(String(50), nullable = False)
    phone = Column(String(15), nullable = False)
    address = Column(String(15))
    section = Column(Integer)
    reg_time = Column(DateTime)
    user_type = Column(Integer)
    def __init__(self, name, fullname, password, email, phone, address, section):
        pwdhash = hashlib.md5(password).hexdigest()
        self.name = name
        self.fullname = fullname
        self.password = pwdhash
        self.email = email
        self.phone = phone
        self.address = address
        self.section = section
        self.reg_time = dt.now()
    def __repr__(self):
        return "<User('%s','%s','%s', '%s', '%s', '%s', '%s')>" % (self.id, self.name, self.fullname, self.email, self.password, self.phone, self.address)
        
    def login(self, username, password):
        pwdhash = hashlib.md5(password).hexdigest()
        
        
        
users_table = User.__table__

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey("users.id"))
    order_time = Column(DateTime)
    address = Column(String(300))
    accept = Column(Boolean)
    picked = Column(Boolean)
    def __init__(self, user, address):
        self.user = user
        self.order_time = dt.now()
        self.address = address
        self.accept = False
        self.picked = False

orders_table = Order.__table__

class Logger(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    action = Column(Integer)
    user = Column(Integer, ForeignKey("users.id"))
    description = Column(Text(500))
	
logger_table = Logger.__table__
metadata = Base.metadata
if __name__ == "__main__":
    metadata.create_all(engine)
