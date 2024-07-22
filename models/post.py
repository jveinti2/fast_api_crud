from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String
from config.database import Base

class Post(Base):
    __tablename__ = 'posts'
    id = Column(String, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(String)
    create_at = Column(DateTime, default=datetime.now)
    
    