from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, String, ForeignKey


MYSQL_HOST = "172.17.0.2"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PWD = "secret"
MYSQL_DB = "users"

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}:{}/{}".format(MYSQL_USER,
                                MYSQL_PWD,
                                MYSQL_HOST,
                                MYSQL_PORT,
                                MYSQL_DB)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)

session = Session()

Base = declarative_base()




class User(Base):
    """
    Cette classe correspond à la version objet de notre table user
    """

    __tablename__ = "user"
    
    id = Column(String(120), unique=True, nullable=False, primary_key=True)
    nom = Column(String(80), nullable=False)
    genres = Column(String(80), nullable=False)
    songs = Column(String(80), nullable=False)
    popularity = Column(String(80), nullable=False)
    link = Column(String(80), nullable=False)


def add_user(id, nom, genres, songs, popularity, link):
    try:
        user = User(id=id, nom=nom, genres=genres, songs=songs, popularity=popularity, link=link)
        session.add(user)
        session.commit()

        return True

    except Exception as e:
        print(e)

        return False

def get_user_by_id(id):
    try:
        result = session.query(User).filter_by(id=id).first()
        return result
    except Exception as e:
        print(e)
        return False

def get_all_users():
    try:
        result = session.query(User).filter_by()

        return result
    except Exception as e:
        print(e)
        return False

def delete_user_by_id(id):
    try:
        user_to_delete = get_user_by_id(id)
        if user_to_delete :
            session.delete(user_to_delete)
            session.commit()
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False

def update_attribute(id, attributes):

    try:
        user_to_update = get_user_by_id(id)
        if user_to_update :
            for k,v in attributes.items():
                setattr(user_to_update, k, v)
            session.commit()
            return user_to_update
        else:
            return False
    except Exception as e:
        print(e)
        return False