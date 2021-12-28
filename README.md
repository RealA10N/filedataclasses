# file dataclasses

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
