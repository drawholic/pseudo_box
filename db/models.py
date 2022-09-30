from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey
Base = declarative_base()



class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(Integer)

    items = relationship('Item', back_populates='user')



class Item(Base):
    __tablename__ = 'items'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    url = Column(String)
    
    parent = relationship('Item', remote_side=[id])
    parent_id = Column(Integer, ForeignKey('items.id'), nullable=True)
    items = relationship('Item', back_populates='parent')

    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='items')
