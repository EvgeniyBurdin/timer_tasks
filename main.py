import asyncio

from data_classes import Task
from storages import TasksStorage
from utils import make_start_time, get_current_time

storage = TasksStorage()


async def send_task(task: dict):
    """ Отправляет задачу далее по назначению.
    """
    print(f"Задача {task} отправлена, {get_current_time()}.")


async def delayed_send(timer: int, task: Task) -> None:
    """ Обеспечивает отправку задачи через время указанное в timer.
    """

    task.starting = make_start_time(timer)
    await storage.push(task)

    task_id = task.id
    del task

    await asyncio.sleep(timer)

    task = await storage.pop(task_id)

    if task is not None:
        await send_task(task.body)


async def delay_task(timer: int, task: Task) -> None:
    """ Откладывает задачу на время указанное в timer.
    """
    asyncio.create_task(delayed_send(timer, task))


async def demo():

    # Имеются 3 задачи с разной паузой перед отправкой
    task_1 = Task(body={'task_1': '11111'})
    task_2 = Task(body={'task_2': '2222'})
    task_3 = Task(body={'task_3': '333'})

    # Отдадим их на ожидание после которого они будут отправлены
    await delay_task(timer=8, task=task_1)
    await delay_task(timer=5, task=task_2)
    await delay_task(timer=2, task=task_3)

    # Подождем пока истечет время ожидания всех задач
    await asyncio.sleep(10)


if __name__ == "__main__":

    asyncio.run(demo())
