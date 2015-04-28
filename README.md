# frigg-settings [![Build status](https://ci.frigg.io/badges/frigg/frigg-settings/)](https://ci.frigg.io/frigg/frigg-settings/last/) [![Coverage status](https://ci.frigg.io/badges/coverage/frigg/frigg-settings/)](https://ci.frigg.io/frigg/frigg-settings/last/)
A python module for parsing and discovery of frigg settings file

## Installation
```
pip install frigg-settings
```

## Usage
The same content as t.py, thus run `python t.py` to se the output.

```python
from frigg_settings.helpers import FileSystemWrapper
from frigg_settings import build_tasks, load_settings_file, build_settings

path = os.getcwd()
runner = FileSystemWrapper()

print('Tasks: {}'.format(build_tasks(path, runner)))
print('Settings-file: {}'.format(load_settings_file('{}/.frigg.yml'.format(path), runner)))
print('Build-settings: {}'.format(build_settings(path, runner)))
```

The script prints the following:

```text
Tasks: ['tox', 'flake8']
Settings-file: {'tasks': ['tox -e py34', 'tox -e flake8', 'tox -e isort', 'coverage report -m && coverage xml'], 'coverage': {'parser': 'python', 'path': 'coverage.xml'}}
Build-settings: {'webhooks': [], 'services': [], 'tasks': ['tox -e py34', 'tox -e flake8', 'tox -e isort', 'coverage report -m && coverage xml'], 'coverage': {'parser': 'python', 'path': 'coverage.xml'}}
```

--------------

MIT © frigg.io
