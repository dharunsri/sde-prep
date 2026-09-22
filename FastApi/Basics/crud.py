from FastApi.Basics.models import Tasks
from FastApi.Basics.database import session
import FastApi.Basics.db_model as db_model
from sqlalchemy.orm import Session


default_task_list = [
    Tasks(id=1, title="Coding", description="FastApi hands-on coding", completed=True),
    Tasks(id=2, title="Cleaning", description="clean the room", completed=True),
    Tasks(id=3, title="Purchase", description="Buy new gadgets", completed=False),
    Tasks(id=4, title="Shopping", description="Buy groceries", completed=False),
    Tasks(id=5, title="Learning", description="Learn new skill", completed=True),
]

def init_db():
    db = session()
    count = db.query(db_model.Tasks).count()
    if count == 0:
        for task in default_task_list:
            db.add(db_model.Tasks(**task.model_dump()))
        db.commit()


def get_all_tasks(db: Session):
    return db.query(db_model.Tasks).all()

def get_task(id, db: Session):
    task = db.query(db_model.Tasks).filter(db_model.Tasks.id == id).first()
    if task:
        return task
    return "Task Not Found"

def add_task(task: Tasks, db: Session):
    db.add(db_model.Tasks(**task.model_dump()))
    db.commit()
    return task

def update_task(id, task: Tasks, db: Session):
    db_task = db.query(db_model.Tasks).filter(db_model.Tasks.id == id).first()
    if db_task:
        db_task.title = task.title
        db_task.description = task.description
        db_task.completed = task.completed
        db.commit()
        return db_task
    else:
        return "No task found"

def delete_task(id, db: Session):
    db_task = db.query(db_model.Tasks).filter(db_model.Tasks.id == id).first()
    if db_task:
        db.delete(db_task)
        db.commit()
    else:
        return "No task found"


