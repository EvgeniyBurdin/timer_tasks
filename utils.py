from datetime import datetime

from data_classes import TaskTime


def get_current_time() -> TaskTime:
    return int(datetime.utcnow().timestamp())


def make_start_time(timer: int) -> TaskTime:
    return int(get_current_time()+timer)
