from sqlalchemy import text, ForeignKey
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(48))
    fullname = Column(String(48))
    nickname = Column(String(48))

    posts = relationship('Post', back_populates= 'user')


    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" %(self.name, self.fullname, self.nickname)


class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String(100))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='posts')


engine = create_engine('mysql+pymysql://root:Siriusa1.615@localhost:3306/mysql_db')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine).


session = Session()