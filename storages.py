from abc import ABC, abstractmethod
from typing import List, Optional

from data_classes import Task, TaskId


class Base(ABC):

    @abstractmethod
    async def push(self, task: Task) -> None:
        """ Записывает задачу в хранилище.
        """

    @abstractmethod
    async def pop(self, task_id: TaskId) -> Task:
        """ Достает задачу  из хранилища.
        """

    @abstractmethod
    async def pop_all(self) -> List[Task]:
        """ Достает все задачи из хранилища.
        """

    @abstractmethod
    async def list_all(self) -> List[Task]:
        """ Показывает все задачи в хранилище.
        """


class Simple(Base):

    def __init__(self):
        self.storage = {}

    async def push(self, task: Task) -> None:

        self.storage[task.id] = {
            'starting': task.starting,
            'body': task.body,
        }
        print(f"Поступила на хранение задача: {task.body}")

    async def pop(self, task_id) -> Optional[Task]:

        task = self.storage.pop(task_id, None)
        print(f"Из хранилища забрана задача: {task}")

        return None if task is None else Task(
            id=task_id, starting=task['starting'], body=task['body']
        )

    async def pop_all(self) -> List[Task]:

        return [await self.pop(task_id) for task_id in self.storage.keys()]

    async def list_all(self) -> List[Task]:

        return[
            Task(id=key, starting=value['starting'], body=value['body'])
            for key, value in self.storage.items()
        ]


class TasksStorage(Simple):
    pass
