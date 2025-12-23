def notify (task,level:str):
    print(
        f"[{level}] REMINDER -> {task.title} | Due at {task.due_time}"
    )