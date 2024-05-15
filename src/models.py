from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class News(Base):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(String(255))
    source_name = Column(String(255))
    author = Column(String(255))
    title = Column(String(255))
    description = Column(String(1000))
    url = Column(String(1000))
    urlToImage = Column(String(1000))
    published_at = Column(DateTime)
    content = Column(String(1000))

