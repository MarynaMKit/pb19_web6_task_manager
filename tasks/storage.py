from typing import List, Tuple

_DB = []


def add_task(title: str) -> None:
    _DB.append({"title": title, "completed": False})


def remove_task(index: int) -> None:
    _DB.pop(index)


def mark_task_completed(index: int, completed: bool) -> None:
    _DB[index]["completed"] = completed


def get_all_tasks() -> List[Tuple[int, str, bool]]:
    return [(i, task["title"], task["completed"]) for i, task in enumerate(_DB)]


def check_if_task_in_DB(index: int) -> bool:
    if index < len(_DB):
        return True
