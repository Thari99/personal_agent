from typing import TypedDict,List, Optional
from models.task import Task

class AgentState (TypedDict):
    tasks : List[Task]
    current_task: Optional[Task]
    decision: Optional[str]

    