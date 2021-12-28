from .file import FileDataclass
from json import loads, dumps


class JsonDataclass(FileDataclass):

    def _loads(self, data: str) -> dict:
        return loads(data)

    def _dumps(self, data: dict) -> str:
        return dumps(data, indent=4)
