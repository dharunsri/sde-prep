from fastapi import FastAPI, Depends
import FastApi.Basics.crud as crud
import FastApi.Basics.db_model as db_model
from FastApi.Basics.database import session, engine
from sqlalchemy.orm import Session
from FastApi.Basics.models import Tasks

app = FastAPI()

db_model.Base.metadata.create_all(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return "Hello All! It's just a FastApi Hands-On Practice - Task Manager"

crud.init_db()

@app.get("/tasks")
def get_all_tasks(db: Session = Depends(get_db)):
    return crud.get_all_tasks(db=db)


@app.get("/task/{id}")
def get_task(id, db: Session = Depends(get_db)):
    return crud.get_task(id, db=db)

@app.post("/task/add")
def add_task(task: Tasks, db: Session = Depends(get_db)):
    return crud.add_task(task, db)

@app.put("/task/update/{id}")
def update_task(id, task: Tasks, db: Session = Depends(get_db)):
    return crud.update_task(id, task, db)

@app.delete("/task/delete/{id}")
def delete_task(id, db: Session = Depends(get_db)):
    return crud.delete_task(id, db)






