from pydantic import Field
from src.models import CustomModel
from enum import Enum
from uuid import UUID, uuid4


class Operation(str, Enum):
    PLUS = "+"
    MINUC = "-"
    MULTY = "*"
    DEVISION = "/"


class StatusEnum(int, Enum):
    CREATED = 0
    RUNING = 1
    DONE = 2
    NOT_FINISHED = 3


class InputTask(CustomModel):
    id: UUID = Field(default=uuid4, title="Task unique id")
    x: int = Field(title="The first value for the task")
    y: int = Field(title="The second value for the task")
    operation: Operation = Field(title="The operation", max_length=1)


class OutputTask(CustomModel):
    id: UUID = Field(title="Task unique id")
    x: int = Field(title="The first value for the task")
    y: int = Field(title="The second value for the task")
    operation: Operation = Field(title="The operation", max_length=1)
    result: float | None = Field(title="Result of the operation")
    status: StatusEnum = Field(title="Status of the task")


class Status(CustomModel):
    status: StatusEnum = Field(title="Status of the task")
