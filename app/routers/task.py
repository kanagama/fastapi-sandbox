from typing import List
from fastapi import APIRouter

import schemas.task as task_schema

router = APIRouter()

@router.get("/task", response_model=List[task_schema.Task])
def list_tasks():
    return [
        task_schema.Task(
            id=1,
            title="1つ目のTODOタスク"
        )
    ]

@router.get("/test")
def test():
    return {
        "Hello": "test16",
    }
