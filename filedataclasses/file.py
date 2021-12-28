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
            # TODO: think about a way of warning the user about a OSError.
            # maybe it can be done using builtin warnings module, although I
            # wouldn't want it to print the warning (at least not by default)
            pass

        data = self._loads(raw)
        if data:
            for field, value in data.items():
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
        # TODO: handle events in which the parse fails to parse the data
        # Similarly to the previues comment, it possibly can be done by catching
        # the raised exceptions here and converting them into warnings.
        pass

    @abstractmethod
    def _dumps(self, data: dict) -> str:
        # TODO: don't erase existing data that isn't part of the dataclass
        # in the file.
        pass
