from datetime import datetime, timedelta
from core.database import SessionLocal
from models.task import Task
from services.notifier import notify

def observe_task(state):
    db=SessionLocal()
    try:
        tasks = db.query(Task).filter(Task.status == "pending".all)
        return{
            **state,
            "tasks":tasks
        }
    finally:
        db.close


def think_task(state):
    if not state["task"]:
        return state
    
    task = state["tasks"][0]
    now = datetime.utcnow()
    time_left=task.due_time - now

    decision = now

    if time_left< timedelta(minutes=0):
        decision = "URGENT"
    elif task.priority == "high" and time_left < timedelta(hours=2):
        decision = "REMIND" 

    return{
        **state,
        "current_task":task,
        "decision" : decision
    }


## Decide (ROUTE)

def decide_action(state):
    if state.get("decition"):
        return "act"
    
    return "observe"

## act

def act_notify(state):
    task = state["current_task"]
    notify(task,state["decision"])
    return state

## REMEMBER

def remember(state):
    task = state.get("current_task")
    if not task :
        return state
    
    db = SessionLocal()
    try:
        task.last_notified = datetime.utcnow()
        db.merge(task)
        db.commit()
    finally:
        db.close()

    return{
        "task":[],
        "current_task":None,
        "decision":None
    }