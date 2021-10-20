from enum import Enum
from uuid import uuid4


class TodosModel:
    class TodoDNE(Exception):
        def __init__(self):
            self.message = "Todo doesn't exist"

    class Status(Enum):
        PENDING = "PENDING"
        DONE = "DONE"
        CANCELED = "CANCELED"

        @classmethod
        def list(self):
            """Returns all the enums as list."""

            return list(map(lambda status: status.value, self))

    def __init__(self):
        self.todos = {
            str(uuid4()): {
                "title": "todo 1",
                "status": self.Status.PENDING.value
            },
            str(uuid4()): {
                "title": "todo 2",
                "status": self.Status.DONE.value
            },
        }

    def assert_todo_exists(self, uid):
        """Throws an exception if the UID doesn't exist."""

        if uid not in self.todos:
            raise self.TodoDNE()

    def add_todo(self, title):
        """Adds a new To-Do."""

        self.todos[str(uuid4())] = {
            "title": title,
            "status": self.Status.PENDING.value
        }

    def update_todo(self, uid, new_todo):
        """Updates the To-Do's properties which are in `new_todo`."""

        self.assert_todo_exists(uid)
        self.todos[uid] = {
            "title":
            new_todo["title"] or self.todos[uid]["title"],
            "status":
            new_todo["status"] if new_todo["status"] in self.Status.list() else
            self.Status.PENDING.value
            if new_todo["status"] else self.todos[uid]["status"]
        }

    def delete_todo(self, uid):
        """Delete's a To-Do by UID."""

        self.assert_todo_exists(uid)
        self.todos.pop(uid)
