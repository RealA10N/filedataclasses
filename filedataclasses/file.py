from os import path
from abc import ABC, abstractmethod
from typing import List


class FileDataclass(ABC):
    """ An abstract file dataclass that automatically initializes itself with
    with the values that are given in the file that represents the file.
    If the file doesn't contain all required values for the dataclass, or the
    file doesn't exist at all, the default values for the missing fields are
    being loaded instead (all fields are required to have default values). 
    The format of saving and loading data from files isn't specified in the
    implementation of this class, and it should be specified in an object that
    inheres from this 'FileDataclass'. """

    def __init__(self, filepath: str) -> None:
        self.__filepath = filepath

        if not path.isfile(filepath):
            return  # if file doesn't exist yet, we are finished

        try:
            with open(filepath, 'r') as f:
                raw = f.read()

        except (FileNotFoundError, OSError):
            # We load the default values if a file can't be opened,
            # or if it doesn't exist.
            # TODO: think about a way of warning the user about a OSError
            pass

        for field, value in self._loads(raw).items():
            if field in self._fields():
                self.__setattr__(field, value)

    @classmethod
    def _fields(cls) -> List[str]:
        return [
            f for f in dir(cls)
            if not f.startswith('_')
            if not callable(getattr(cls, f))
        ]

    def save(self) -> None:
        with open(self.__filepath, 'w') as file:
            file.write(self._dumps({
                f: getattr(self, f)
                for f in self._fields()
            }))

    @abstractmethod
    def _loads(self, data: str) -> dict:
        pass

    @abstractmethod
    def _dumps(self, data: dict) -> str:
        pass
