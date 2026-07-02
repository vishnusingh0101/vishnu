from sqlalchemy import Column,Integer,String
from app.database.database import Base
class Memory(Base):
 __tablename__='memories'
 id=Column(Integer,primary_key=True)
 category=Column(String)
 key=Column(String,index=True)
 value=Column(String)
