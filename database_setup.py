from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import create_engine
 
Base = declarative_base()

class Restaurant(Base):
    __tablename__ = 'restaurant'
   
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    user_email = Column(String(100))
    user_image= Column(String(250))
    username= Column(String(100))

    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'id'           : self.id,
       }
 
class MenuItem(Base):
    __tablename__ = 'menu_item'


    name =Column(String(80), nullable = False)
    id = Column(Integer, primary_key = True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer,ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant, backref=backref('menu_item', cascade='all,delete'))


    @property
    def serialize(self):
       """Return object data in easily serializeable format"""
       return {
           'name'         : self.name,
           'description'         : self.description,
           'id'         : self.id,
           'price'         : self.price,
           'course'         : self.course,
       }



engine = create_engine('sqlite:///restaurantmenu.db')
 

Base.metadata.create_all(engine)
