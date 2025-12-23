from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from core.database import Base

class Task(Base):
    __tablename__ = "task"

    id =Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    due_time = Column(DateTime, nullable=False)
    priority = Column(String(20), default="medium")
    status = Column(String(20), default="pending")
    last_notified = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.now)