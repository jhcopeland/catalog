from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

#engine = create_engine('sqlite:///usercategoryitem.db')
engine = create_engine('postgresql://catalog:sunshine25@localhost/usercategoryitem')
Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'id': self.id,
            'name': self.name,
        }


class CatUser(Base):
    __tablename__ = 'cat_user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)


class CatItem(Base):
    __tablename__ = 'cat_item'

    id = Column(Integer, primary_key = True)
    name = Column(String(80), nullable = False)
    description = Column(String(250))
    cat_id = Column(Integer,ForeignKey('category.id'))
    category = relationship(Category)
    user_id = Column(Integer,ForeignKey('cat_user.id'))
    user = relationship(CatUser)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
                'cat_id': self.cat_id,
                'id': self.id,
                'name': self.name,
                'description': self.description,
        }

Base.metadata.create_all(engine)
