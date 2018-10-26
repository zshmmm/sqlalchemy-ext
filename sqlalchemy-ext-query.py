# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def conntodb():
    dbconnurl = ('mysql+pymysql://{user}:{passwd}@{host}:{port}'
                '/{db}?charset=utf8&connect_timeout=10').format(
            user = 'root',
            passwd = '******',
            host = '127.0.0.1',
            port = 3306,
            db = 'testtable'
        )
    engine = create_engine(dbconnurl)
    DBSession = sessionmaker(bind=engine)
    return DBSession()

dbsession = conntodb()

class ConnectToDB(object):
    def __init__(self):
        self.session = dbsession

    def __enter__(self):
        return self.session

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.session.close()
    

class _QueryProperty(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, obj, cls):
        with ConnectToDB() as session:
            return self.func(cls, session)

class TableModelExt(object):

    @_QueryProperty
    def query(cls, session):
        return session.query(cls)

    def save(self):
        with ConnectToDB() as session:
            session.add(self)
            session.commit()

    def delete(self):
        with ConnectToDB() as session:
            session.delete(self)
            session.commit()

