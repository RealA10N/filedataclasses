from .file import FileDataclass

try:
    from toml import loads, dumps

except ImportError as error:
    raise ImportError(
        "Missing required modules. "
        "To support TOML, install with the [toml] extras."
    ) from error


class TomlDataclass(FileDataclass):

    def _loads(self, data: str) -> dict:
        return loads(data)

    def _dumps(self, data: dict) -> str:
        return dumps(data)
