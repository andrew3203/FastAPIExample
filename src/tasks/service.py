from src.tasks.schemas import InputTask, OutputTask, Status
from fastapi import BackgroundTasks
from uuid import UUID


async def create_task(task: InputTask) -> Status:
    pass


async def get_task(task_id: UUID) -> OutputTask:
    pass


async def tasks_list() -> list[OutputTask]:
    pass
