
import json
from datetime import datetime


class Hello(object):

    def __init__(
            self, firstname: str, lastname: str, age: int, created_at: str = str(datetime.now())
    ):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.created_at = created_at

    def __str__(self) -> str:
        return json.dumps(self.__dict__)

    def __hash__(self) -> int:
        return (
            hash(self.firstname) ^
            hash(self.lastname) ^
            hash(self.age) ^
            hash((self.firstname, self.lastname, self.age))
        )

    def __eq__(self, other):
        def compare(that):
            keys = set(self.__dict__) & set(that)
            modified = {
                k: (self.__dict__[k], that[k])
                for k in keys if self.__dict__[k] != that[k] and k != 'created_at'
            }

            return modified

        if isinstance(other, type(self)):
            return self.__dict__ == other.__dict__

        return len(compare(other)) == 0

    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, dictionary: dict):
        allowed_keys = ['firstname', 'lastname', 'age']
        df = {k: v for k, v in dictionary.items() if k in allowed_keys}
        return cls(**df)
