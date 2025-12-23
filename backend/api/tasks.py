from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from core.database import SessionLocal
from models.task import Task
from schemas.task import TaskCreate

router = APIRouter(prefix = "/tasks", tags=["Tasks"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_task(task: TaskCreate, db:Session = Depends(get_db)):
    new_task = Task(**task.dict())
    db.add(new_task)
    db.commit
    return {"message":"Task create"}