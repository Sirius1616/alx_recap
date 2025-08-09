from sqlalchemy import text
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(48))
    fullname = Column(String(48))
    nickname = Column(String(48))


    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" %(self.name, self.fullname, self.nickname)


engine = create_engine('mysql+pymysql://root:Siriusa1.615@localhost:3306/mysql_db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()


user = User(name='John', fullname='John Ezekiel', nickname='Sirius_A')
session.add(user)

session.commit()
