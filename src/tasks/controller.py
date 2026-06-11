from sqlalchemy.orm import Session
from src.tasks.dtos import TaskSchema
from src.tasks.models import TaskModel
from fastapi import HTTPException
from src.user.models import UserModel


def create_task(body: TaskSchema, db: Session , user: UserModel):
    data = body.model_dump()
    #now convert data to store in db using model so create object of taskModel
    new_task = TaskModel(title=data['title'], description=data['description'], is_completed=data['is_completed'], user_id=user.id)
    db.add(new_task)
    db.commit()
    #refresh krne ke baad db mein jo data hai woh data new_task mein ayega nahi object ka data
    db.refresh(new_task)
    return new_task

def get_tasks(db : Session , user: UserModel):
    tasks = db.query(TaskModel).filter(TaskModel.user_id == user.id).all()
    return tasks

def get_one_tasks(task_id: int, db:Session):
    one_task = db.query(TaskModel).get(task_id)
    #id incorrect
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")

    return one_task


def update_task(task_id: int, body: TaskSchema, db: Session, user:UserModel):
    one_task = db.query(TaskModel).get(task_id)
    #id incorrect
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if one_task.user_id != user.id:
        raise HTTPException(status_code=404, detail="You are not allowed to perform this action")
    body = body.model_dump() # this is the dict
    for field, value in body.items():
        setattr(one_task, field, value)

    db.add(one_task)
    db.commit()
    db.refresh(one_task)
    return one_task

def delete_task(task_id: int, db: Session, user: UserModel):
    one_task = db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code=404, detail="Task not found")

    if one_task.user_id != user.id:
        raise HTTPException(status_code=404, detail="You are not allowed to perform this deletion")
    db.delete(one_task)
    db.commit()

    return None