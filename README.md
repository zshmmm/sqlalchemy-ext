# sqlalchemy-ext-query
通过继承 TableModelExt 为每一个表类增加了3个属性
query
save
delete

在使用sql查询时可以直接使用
cls.query
而无需管理 db 连接 session，在每次处理完成后会自动 close session

注意: 没有任何异常处理

使用方式

from sqlalchemy-ext-query import TableModelExt
from sqlalchemy import Column, String
from sqlalchemy.dialects.mysql import INTEGER

class GroupInfo(Base, TableModelExt):
    __tablename__ = 'group_info'

    id = Column(INTEGER(11), primary_key=True)
    company = Column(String(32), nullable=False)
    project = Column(String(64), nullable=False)
    use_type = Column(String(32), nullable=False)
    group_name = Column(String(128), nullable=False, unique=True)
    

GroupInfo.query.all()

使用的方式类似于 flask_sqlalchemy
