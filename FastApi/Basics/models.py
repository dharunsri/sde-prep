from pydantic import BaseModel

class Tasks(BaseModel):
    id: int
    title: str
    description: str
    completed: bool