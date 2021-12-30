# file dataclasses

## Example

In the following examples we will use the `JsonDataclass` object.
The behavior of `TomlDataclass` and `YamlDataclass` is similar, however using
them requires additional dependencies (see installation details below).

```python
from filedataclasses import JsonDataclass


class MyAppConfiguration(JsonDataclass):
    # Define your own dataclass using the Python class syntax!
    # All values in the dataclass must have default values.
    # Those values will be loaded if those fields are missing in datafile,
    # or if the datafile doesn't exist at all.

    path = '/default/path'
    passcode: str = '1234'  # type annotations are optional.


if __name__ == '__main__':

    # Load data from 'config.json'
    config = MyAppConfiguration('config.json')

    # Easily access and change fields in the dataclass
    config.passcode = input('Enter new passcode: ')

    # Write data back to the 'config.json' file.
    config.save()
```

## Installation

By default, *filedataclasses* comes with support for JSON files only.
To support other formats like *YAML* and *TOML*, *filedataclasses* requires
additional dependencies to be installed.

To install *filedataclasses* with JSON support only, use:
```bash
pip install filedataclasses # only json supported
```

To install *fileclasses* with *YAML* or *TOML* support, use:
```bash
pip install filedataclasses[yaml]  # for toml use: [toml]
```

To install *fileclasses* with support for all available file formats, use:
```bash
pip install filedataclasses[all]  # [toml, yaml] works too!
```
