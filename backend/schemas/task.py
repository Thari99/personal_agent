from pydantic import BaseModel
from datetime import datetime

class TaskCreate(BaseModel):
    title:str
    due_time: datetime
    priority:str = "medium"