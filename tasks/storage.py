from typing import List, Tuple

_DB = []


def add_task(title: str) -> None:
    _DB.append({"title": title, "completed": False})


def remove_task(index: int) -> None:
    _DB.pop(index)


def mark_task_completed(index: int, completed: bool) -> None:
    _DB[index]["completed"] = completed


def get_all_tasks() -> List[Tuple[int, str, bool]]:
    res = []
    for i, task in enumerate(_DB):
        if task['completed']:
            res.append(f"[V] {i} - {task['title'] }")
        else:
            res.append(f"[ ] {i} - {task['title'] }")
    return res
