from .file import FileDataclass

try:
    from yaml import safe_load, safe_dump

except ImportError:
    raise ImportError(
        "Missing required modules. "
        "To support YAML, install with the [yaml] extras."
    ) from None


class YamlDataclass(FileDataclass):

    def _loads(self, data: str) -> dict:
        return safe_load(data)

    def _dumps(self, data: dict) -> str:
        return safe_dump(data)
