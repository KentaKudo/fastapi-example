from fastapi import FastAPI
from typing import Dict, List
import uuid
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def say_hello():
    return {"Hello": "World"}


class Todo(BaseModel):
    id: uuid.UUID
    name: str


todos: Dict[uuid.UUID, Todo] = dict()


class CreateTodoRequest(BaseModel):
    name: str


@app.post("/todos")
def create_todo(request: CreateTodoRequest):
    id = uuid.uuid4()
    todo = Todo(id=id, name=request.name)
    todos[id] = todo
    return todo


@app.get("/todos")
def list_todos():
    return list(todos.values())
