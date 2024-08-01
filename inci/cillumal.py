from typing import Protocol

class HasJson(Protocol):
    def to_json(self) -> str:
        ...
