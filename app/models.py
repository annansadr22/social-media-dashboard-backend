# app/models.py

from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, DateTime, Text
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, nullable=False)
    bio = Column(Text, nullable=True)      
    age = Column(Integer, nullable=True)    
    hobbies = Column(Text, nullable=True)   
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)

    posts = relationship("Post", back_populates="owner")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    platform = Column(String, nullable=False)
    scheduled_time = Column(DateTime, nullable=True)
    status = Column(String, default="Scheduled")
    user_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="posts")
    analytics = relationship("Analytics", back_populates="post", uselist=False)


class Analytics(Base):
    __tablename__ = "analytics"

    id = Column(Integer, primary_key=True, index=True)
    post_id = Column(Integer, ForeignKey("posts.id"))
    likes = Column(Integer, default=0)
    shares = Column(Integer, default=0)
    views = Column(Integer, default=0)

    post = relationship("Post", back_populates="analytics")
