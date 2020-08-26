from dataclasses import dataclass, field
from uuid import UUID, uuid4
from typing import Optional

TaskId = UUID
TaskTime = int  # Timestamp в секундах


@dataclass
class Task:
    """ Датакласс ожидающей задачи.

        :id:       Уникальный идентификатор задачи.
                   Если не указан при создании экземпляра, то будет присвоен
                   автоматически.
        :starting: Время, когда задача должна быть взята из хранилища и
                   отправлена на выполнение. По умолчанию None. Поле должно
                   получить значение перед сохранением задачи в хранилище.
        :body:     Словарь с данными задачи.
    """
    body: dict
    id: TaskId = field(default_factory=uuid4)
    starting: Optional[TaskTime] = None
