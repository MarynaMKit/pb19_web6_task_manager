from typing import List, Tuple

_DB = []


def add_task(title: str) -> None:
    _DB.append({"title": title, "completed": False})


def remove_task(index: int) -> None:
    _DB.pop(index-1)


def mark_task_completed(index: int, completed: bool) -> None:
    _DB[index-1]["completed"] = completed


def get_all_tasks() -> List[Tuple[int, str, bool]]:
    res = []
    for i, task in enumerate(_DB):
        if task['completed']:
            res.append(f"[V] {i+1} - {task['title'] }")
        else:
            res.append(f"[_] {i+1} - {task['title'] }")
    return res


def check_if_task_in_DB(index: int) -> bool:
    if index <= len(_DB):
        return True


def get_all_tasks_fo_exporting() -> List[Tuple[int, str, bool]]:
    return [(i+1, task["title"], task["completed"]) for i, task in enumerate(_DB)]
