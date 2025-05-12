# Venv Snippets
# python3 -m venv myenv
# source myenv/bin/activate
# deactivate
# fastapi dev ./src/main.py 

import uvicorn
from fastapi import FastAPI, HTTPException
from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field

app = FastAPI()


class Priority(IntEnum):
    HIGH = 1
    MEDIUM = 2
    LOW = 3


class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=512, description='Name of todo')
    todo_description: str = Field(..., description='Description of the todo')
    priority: Priority = Field(default=Priority.LOW, description='Priority of the todo')


class Todo(TodoBase):
    todo_id: int = Field(..., description='Unique identifier of a todo item')


class TodoCreate(TodoBase):
    pass


class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=512, description='Name of todo')
    todo_description: Optional[str] = Field(None, description='Description of the todo')
    priority: Optional[Priority] = Field(None, description='Priority of the todo')

PORT = 8000

all_todos = [
    Todo(todo_id=1, todo_name="Eat food", todo_description="Go and warm Eba.", priority=Priority.MEDIUM),
    Todo(todo_id=2, todo_name="Wash clothes", todo_description="Time to wash your clothes.", priority=Priority.LOW),
    Todo(todo_id=3, todo_name="Sleep time", todo_description="Time to go and sleep.", priority=Priority.HIGH)
]


@app.get('/')
def health():
    return {'Healthy'}


@app.get('/todos', response_model=List[Todo])
def get_todos(limit: int = None):
    if limit:
        return all_todos[:limit]
    else:
        return all_todos


@app.get('/todos/{todo_id}', response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            return todo


@app.post('/todos', response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo.todo_id for todo in all_todos) + 1
    new_todo = Todo(todo_id=new_todo_id, todo_name=todo.todo_name, todo_description=todo.todo_description)
    all_todos.append(new_todo)

    return new_todo


@app.put('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo.todo_id == todo_id:
            todo.todo_name = updated_todo.todo_name
            todo.todo_description = updated_todo.todo_description
            todo.priority = updated_todo.priority
            return todo

    raise HTTPException(status_code=404, detail='Todo not found.')


@app.delete('/todos/{todo_id}', response_model=Todo)
def update_todo(todo_id: int):
    # Solution 1
    for index, todo in enumerate(all_todos):
        if todo.todo_id == todo_id:
            deleted_todo = all_todos.pop(index)
            return deleted_todo

    raise HTTPException(status_code=404, detail='Todo not found.')

    # Alternative solution
    # delete_todo = [todo for todo in all_todos if todo['id'] == todo_id][0]
    # try:
    #   all_todos.pop(all_todos.index(delete_todo))
    #   return all_todos
    # except:
    #   print('Something went wrong.')


if __name__ == '__main__':
    print(f'App running on port {PORT}')
    uvicorn.run('main:app', host='127.0.0.1', port=PORT, log_level='info')
