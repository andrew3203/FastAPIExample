from uuid import UUID
from fastapi import APIRouter, status
from src.tasks.schemas import Status, InputTask, OutputTask
from src.tasks.service import create_task, get_task, tasks_list

router = APIRouter()


@router.post("/create", status_code=status.HTTP_201_CREATED)
async def set_task(task: InputTask) -> Status:
    result = await create_task(task)
    return result


@router.get("/get", status_code=status.HTTP_200_OK)
async def get_task_result(task_id: UUID) -> OutputTask:
    result = await get_task(task_id)
    return result


@router.get("/list", status_code=status.HTTP_200_OK)
async def get_tasks_list() -> list[OutputTask]:
    result = await tasks_list()
    return result
