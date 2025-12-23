from fastapi import FastAPI
from core.database import Base, engine
from api.tasks import router as task_router
from agent.graph import build_agent
from apscheduler.schedulers.backgraound import BackgroundScheduler

app = FastAPI(title="Personal Reminder Agent")
