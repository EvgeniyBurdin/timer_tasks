from abc import ABC, abstractmethod
from typing import List, Optional

from data_classes import Task, TaskId


class Base(ABC):

    @abstractmethod
    async def push(self, task: Task) -> None:
        """
            Записывает задачу в хранилище.
        """
        pass

    @abstractmethod
    async def pop(self, task_id: TaskId) -> Task:
        """
            Достает задачу  из хранилища.
        """
        pass

    @abstractmethod
    async def pop_all(self) -> List[Task]:
        """
            Достает все задачи из хранилища.
        """
        pass

    @abstractmethod
    async def list_all(self) -> List[Task]:
        """
            Показывает все задачи в хранилище.
        """
        pass


class Simple(Base):
    """
        Простое хранилище, только для демонстрации работы.
        На основе словаря в памяти.
    """
    def __init__(self):
        self.storage = {}

    async def push(self, task: Task) -> None:
        """
            Записывает задачу в хранилище.
        """
        self.storage[task.id] = {
            'starting': task.starting,
            'body': task.body,
        }
        print(f"Поступила на хранение задача: {task.body}")

    async def pop(self, task_id) -> Optional[Task]:
        """
            Достает задачу  из хранилища.
        """
        task = self.storage.pop(task_id, None)
        print(f"Из хранилища забрана задача: {task}")

        return None if task is None else Task(
            id=task_id, starting=task['starting'], body=task['body']
        )

    async def pop_all(self) -> List[Task]:
        """
            Достает все задачи из хранилища.
        """
        return [await self.pop(task_id) for task_id in self.storage.keys()]

    async def list_all(self) -> List[Task]:
        """
            Показывает все задачи в хранилище.
        """
        return[
            Task(id=key, starting=value['starting'], body=value['body'])
            for key, value in self.storage.items()
        ]


class TasksStorage(Simple):
    pass
