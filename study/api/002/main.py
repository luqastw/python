from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List

app = FastAPI()

class Task(BaseModel):
    id: int
    name: str = Field(
        example="Estudar.",
        description="Nome da tarefa."
    )
    description: str = Field(
        example="Revisar sobre API's REST.",
        description="Descrição da tarefa."
    )
    complete: bool = False    

tasks: List[Task] = []

@app.get("/tasks")
def list_tasks():
    return {"all tasks": tasks}

@app.post("/tasks")
def add_task(task: Task):
    tasks.append(task)
    return {"message": "Tarefa adicionada!", "added task": task}

@app.get("/tasks/{Task_id}")
def view_task(Task_id: int):
    for t in tasks:
        if t.id == Task_id:
            return t
        
    return {"error": "Tarefa não existente."}

@app.put("/tasks/{Task_id}/complete")
def complete_task(Task_id: int):
    for t in tasks:
        if t.id == Task_id:
            t.complete = True
            return {"message": f"Tarefa {Task_id} concluída!"}
        
    return {"error": "Tarefa não encontrada."}

@app.delete("/tasks/{Task_id}/delete")
def delete_task(Task_id: int):
    for i, t in enumerate(tasks):
        if t.id == Task_id:
            removed = tasks.pop(i)
            return {"message": f"Tarefa {Task_id} deletada."}

    return {"error": "Tarefa não encontrada."}